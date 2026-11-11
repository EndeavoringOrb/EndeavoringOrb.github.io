## Project Overview {#overview}

**End-to-End Causal Inference with LLM Agents via a Structured Framework**
Aaron Belikoff (WPI), Matthew Lamborne (UMass Amherst). Advisor: Prof. Raha Moraffah.
Accepted and published at [MIT URTC 2025](https://urtc.mit.edu/).

**Read the paper:** [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/11533065) · [ResearchGate](https://www.researchgate.net/publication/405310505_End-to-End_Causal_Inference_with_LLM_Agents_via_a_Structured_Framework)

**Cited by:** [A Scoping Review of Agentic AI: Applications, Emerging Trends, Risks & Future Directions](https://www.mdpi.com/2079-9292/15/21/5024) (*Electronics*, MDPI)

We built an LLM agent that takes a raw dataset and a causal question ("what is the effect of X on Y?") and answers it end to end: it works out which variables play which roles, picks an estimation method, writes the analysis code, and runs it. This was done in Prof. Moraffah's lab at WPI, where I did undergraduate research on causal reasoning and NLP from 2024 to 2026.

## The Problem {#problem}

Causal inference means estimating how much changing one variable (the *treatment*) changes another (the *outcome*). With a randomized experiment that's easy, but often you only have observational data, where something else (a *confounder*) can affect both treatment and outcome. To get the right answer you have to know the role of each variable and pick an estimation method that fits the data. Numbers alone can't tell you that; you need to understand what the variables mean.

LLMs know a lot about the world, so in principle they can supply that understanding. In practice, earlier work handed the model the hard parts: benchmarks told it which variables were confounders and which method to use, and the model only had to carry it out. We wanted the model to do the whole thing.

## Our Approach {#approach}

### 6-Step Framework {#framework}

Instead of letting the model reason freely, the prompt walks it through six steps in order:

1. Identify the treatment and outcome.
2. Pick an effect-estimation method that suits the data (outcome modeling, propensity scores, instrumental variables, etc.).
3. Identify the tools needed for that method.
4. Identify the other variables to adjust for (confounders, instruments).
5. Identify any data transformations needed (derived columns, filtering).
6. Write the code and estimate the effect.

The prompt also includes templates for 8 causal inference methods and API documentation for [DoWhy](https://github.com/py-why/dowhy)'s `CausalModel`.

### Why Rubin, Not Pearl {#why-rubin}

We first tried a two-stage pipeline built on Pearl causal models: discover the full causal graph (using statistical causal-discovery algorithms with LLM help, including one we built that adds LLM predictions to a score-based search), then estimate the effect from that graph. It didn't work well. Many different graphs can explain the same data, nearly every query had some error in the discovered graph, and those errors carried through to wrong estimates.

So we switched to Rubin causal models, which don't need the full graph, only each variable's role. Classifying roles turned out to be far more tractable for an LLM.

### Tool Calling {#tool-calling}

We compared three ways for the model to run code:

- **Ours (function-based):** The model writes one complete `solution()` function, we run it, and the return value is the answer. If it errors, the model gets up to 3 attempts to fix it.
- **ReAct:** Thought, action, observation loops in a Python terminal.
- **Program of Thoughts:** One program in one shot, with no retries.

## Benchmark {#benchmark}

We evaluated on the causal questions in [QRData](https://github.com/xxxiaol/QRData), which has numerical causal inference problems and multiple-choice causal reasoning problems, each with a dataset, a description of the variables, and a question.

We also made **QRData Instruction-Free**: the same numerical problems, but with the hints about which method to use and which role each variable plays removed. This tests whether the agent can actually do the causal reasoning, rather than just follow instructions.

All experiments used **Qwen3-14B** (6-bit quantized), served with llama.cpp on WPI's Turing cluster.

## Results {#results}

| Numerical problems | Our framework | Baseline prompt |
| :--- | :---: | :---: |
| QRData (with hints) | 37.5% | 39.1% |
| QRData Instruction-Free | 29.7% | 26.6% |
| **Drop when hints are removed** | **7.8 points** | **12.5 points** |

With hints, the baseline is slightly ahead. Without them, our framework loses much less accuracy, which suggests it helps the model reason about causal structure and method choice itself. Overall, Qwen3-14B with our framework outperformed the published GPT-4 + ReAct result on QRData, despite being a much smaller model.

<!-- TODO: add the headline overall-accuracy comparison once the number is confirmed against the published paper -->

## Takeaways {#learned}

- How the reasoning is structured mattered more than model size here.
- Classifying variable roles (Rubin) was much more practical for an LLM than recovering a full causal graph (Pearl).
- More context isn't always better: the method documentation helped on numerical problems but slightly hurt on multiple-choice ones, where it was irrelevant.

## Technology Stack {#tech-stack}
- Python, DoWhy, pandas
- Qwen3-14B, llama.cpp
- WPI Turing HPC cluster
