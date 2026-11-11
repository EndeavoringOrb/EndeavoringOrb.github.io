## Project Overview {#overview}

Tensor Graphs is a compiler and inference engine for ML models, written in C++ with Python bindings. You give it a model as a graph of tensor operations, and it works out how to run that graph on your hardware (CPU, GPU, or both): which kernels to use, which device each operation runs on, what order to run them in, where each tensor lives in memory, and what to cache between runs.

I worked on it for about 10 months (roughly 1,400 commits). It runs real models: Gemma 3 270M for text generation, EmbeddingGemma for text and audio embeddings, and an image diffusion model.

I've since stopped working on it. My conclusion is that a **universal** compiler is the hard way to get speed; an engine specialized for one model on one piece of hardware gets there faster. But it was by far the project I learned the most from, about compilers, optimization and performance engineering.

## How It Works {#how}

### Rewriting with E-Graphs {#egraphs}

The model graph goes into an **e-graph**, a data structure that stores many equivalent versions of a computation at once. Rewrite rules add alternatives: fusing several small operations into one kernel, running an operation on another device (with the copies that requires), or computing only the part of a tensor that changed since the last run, so results can be cached across calls (for example, during token-by-token text generation).

### Planning as a Search Problem {#search}

Picking the best version out of the e-graph is a combinatorial problem, so I wrote a **constraint-programming search** for it (branch and bound with propagators). For every operation it decides:

- which implementation to use,
- when it runs and on which device (CPU and GPU can run at the same time),
- where its output goes in memory (packing buffers so tensors that aren't alive at the same time can share space),
- and whether to keep the result cached for the next run.

The objective is the simulated run time. To prune the search, I derived **lower bounds** on the best possible run time, so whole branches can be skipped once they provably can't beat the best plan found so far. Because the search is easy to get subtly wrong, I also built an "oracle" test suite that brute-forces small problems in Python and checks that the C++ search finds an equally good answer.

### Kernels & Backends {#kernels}

About 100 kernels across CPU (C++ with AVX), CUDA and OpenCL, including fused kernels written for specific models (for example Gemma's RMSNorm and rotary embeddings). Kernels are benchmarked on the target hardware so the planner's cost model uses measured times instead of guesses.

## Results {#results}

Gemma 3 270M text generation on an NVIDIA Quadro M4000, as I added optimizations:

| Step | Prompt processing (5 tokens) | Generation (per token) |
| :--- | ---: | ---: |
| Baseline | 518 ms | 63.3 ms |
| Fused RMSNorm kernels | 900 ms | 50.9 ms |
| Removing copy chains between fused kernels | 755 ms | 37.1 ms |
| Fused rotary embedding kernels | 746 ms | 29.2 ms |
| Compiling exact sequence-length buckets | 63 ms | 37.1 ms |
| *Hugging Face Transformers (CUDA), for reference* | *69 ms* | *37.1 ms* |
| *llama.cpp (CUDA), for reference* | *24 ms* | *13.8 ms* |

Kernel work made generation more than 2x faster, and compiling only the sequence lengths actually needed made prompt processing about 12x faster. It ended up on par with Hugging Face Transformers, but still well behind llama.cpp, which is hand-tuned for exactly this kind of workload.

I applied the same approach to the planner's own search time: on EmbeddingGemma text, it went from **297 s to 29 s** across about 24 measured changes (keeping the ones that helped, reverting the ones that didn't), with identical output.

## How I Worked {#process}

Every optimization was measured before and after on the same benchmark, and changes that didn't help were reverted, even ones that seemed like they should work. The repo keeps a log of every attempt, failed ones included ([kernels](https://github.com/EndeavoringOrb/tensor_graphs/blob/faster-search/KERNEL_PERFORMANCE.md), [search](https://github.com/EndeavoringOrb/tensor_graphs/blob/main/SEARCH_PERFORMANCE.md)).

## What I Learned {#learned}

- Compiler techniques: e-graphs and equality saturation, rewrite rules, scheduling, memory planning.
- Constraint programming and branch-and-bound search, including deriving and testing bounds.
- GPU and CPU kernel optimization, and measuring performance carefully.

## Technology Stack {#tech-stack}
- C++, CUDA, OpenCL, AVX intrinsics
- Python (bindings, testing, benchmarking)
