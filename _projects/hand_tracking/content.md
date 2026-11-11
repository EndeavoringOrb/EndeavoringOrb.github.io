## Project Overview {#overview}

The game I eventually want to make is a mage dueling game where you cast spells with your hands: a webcam watches your hand, you trace a spell's shape in the air, and the game recognizes it. That requires fast, reliable fingertip tracking that can run inside a C++ game loop.

This project is that tracker. It finds the thumb and index fingertips in a webcam frame, so the game can tell where you're pointing and whether you're pinching (pinch = pen down).

<!-- TODO: add a short clip of the tracker running live, e.g. ![Live tracking](/static/files/hand_tracking/demo.mp4) or a GIF -->

## Why Build My Own? {#why}

Google's MediaPipe already does hand tracking, and I use it in this project to label data. I built my own model anyway for two reasons:

- **I wanted to learn the whole pipeline**: collecting data, labeling it, cleaning it, training, and deploying. Using an off-the-shelf model skips all of that.
- **I wanted a tiny model I could run from C++** inside the game, without a Python process on the side.

## Data Pipeline {#data}

Most of the work in this project went into the data, not the model.

1. **Collection with automatic labels.** A capture script records webcam frames and runs MediaPipe on each one to get fingertip positions. My model is essentially learning to reproduce MediaPipe's output (distillation), but only for the points I need.
2. **More variety from HaGRID.** My own webcam footage is all the same room, lighting and hand, so I added frames from the [HaGRID](https://github.com/hukenovs/hagrid) hand-gesture dataset and labeled them with MediaPipe too.
3. **Review tool.** MediaPipe isn't always right, and bad labels hurt training. I wrote a review tool to step through samples, see the labels drawn on the image, and fix or throw out bad ones. It can also sort the dataset by the current model's loss on each sample, so the samples where the model and the label disagree most (often bad labels) come up first.
4. **Pinch labels.** A small Flask app for labeling the pinch point by hand, since MediaPipe doesn't give that directly.

Data is stored in chunked binary files instead of individual image files, which keeps loading fast.

## Model & Training {#model}

- **Model:** I started with very small CNNs (a few thousand parameters) and moved to a small ResNet. It outputs the (x, y) position of the thumb and index fingertips, plus a **variance for each prediction**. Training with a Gaussian negative log-likelihood loss means the model also learns to say how sure it is, which the game can use to ignore shaky frames.
- **GPU augmentation:** Random translation, crop-and-resize, rotation and color jitter. CPU-side augmentation was the bottleneck, so I wrote the geometric augmentations as **custom CUDA kernels** (as a PyTorch extension) that transform the images and keypoints together on the GPU.
- **Training setup:** Mixed precision, a low-memory mode for larger datasets, and logging of every run's config and results.
- **Hyperparameter sweeps:** A small Flask dashboard to launch runs, compare them, and run Bayesian-optimization sweeps over the hyperparameters.

## Running It in the Game {#game}

To use the model without Python, I export the trained weights to a binary file and run inference with a small **from-scratch C++ implementation** of the network (convolutions, normalization, the ResNet blocks), plus OpenCV for the camera and preprocessing.

## Where It's At {#status}

The tracker runs live on a webcam. The game itself is early: it has movement and a spell system, but the gesture-to-spell part isn't wired up yet. Building this taught me that most of the effort in an applied ML project is in the data: collecting it, finding the bad labels, and making the dataset varied enough.

## Technology Stack {#tech-stack}
- Python, PyTorch, CUDA (custom kernels), OpenCV, MediaPipe
- Flask (labeling and training dashboards), scikit-optimize
- C++ (inference in the game)
