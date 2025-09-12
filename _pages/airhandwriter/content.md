---
layout: archive
title: "AirHandWriter: Real-Time Hand Tracking"
permalink: /airhandwriter/
author_profile: false
---

## Overview

AirHandWriter is a system for real-time hand tracking and pinch detection from a standard webcam feed. The system uses a neural network to detect the positions of the thumb and index fingertips and classify if they are pinching, enabling camera-only computer interaction.

The project encompasses a full machine learning pipeline, including data collection, a high-throughput CUDA-accelerated augmentation pipeline, model training, and a Flask-based web dashboard for managing experiments.

### Key Features

- **Keypoint Detection**: Utilizes a ResNet-based architecture to precisely regress the coordinates of the thumb and index fingertips.
- **Real-Time Performance**: Targeting low-latency inference on live camera feeds.
- **Pinch Gesture Recognition**: In addition to keypoints, the model classifies whether the user is performing a pinch gesture.
- **CUDA-Accelerated Augmentation**: A custom PyTorch C++/CUDA extension performs data augmentation (cropping, rotation, translation) directly on the GPU in a single kernel, dramatically accelerating the training pipeline.
- **Comprehensive Training Dashboard**: A Flask web application provides a UI for launching training runs, configuring hyperparameter sweeps, and visualizing results in real-time.
- **Robust Data Pipeline**: Includes tools for gathering data from web scraping and the HaGRID dataset, along with a custom review tool for cleaning and correcting labels.

## How It Works

The system is broken down into a data pipeline, a training process, and an inference engine.

### 1. Data Collection & Preparation
- **Data Gathering**: Initial datasets are created by scraping images from the web, processing the large-scale HaGRID dataset, or capturing new data from a live camera using MediaPipe for initial annotations.
- **Data Review**: A custom interactive tool (`reviewData.py`) allows for manual verification, correction, and deletion of incorrect labels to ensure a high-quality dataset.
- **Efficient Storage**: Data is stored in a chunked format (`.npz` for images, `.bin` for keypoints) to handle large datasets without requiring massive amounts of RAM.

### 2. Training Process
- **Data Loading**: A custom `Dataset` class loads data chunks on demand.
- **GPU Augmentation**: During training, batches of images and keypoints are passed to a custom CUDA kernel. This kernel applies a series of augmentations on the GPU.
- **Model Training**: The augmented data is fed into a `SimpleResNet` model. The model is trained to minimize the Mean Squared Error (MSE) between its predicted keypoint coordinates and the ground-truth labels. If pinch classification is enabled, a Cross-Entropy loss is added.
- **Experiment Management**: The Flask dashboard can be used to launch training jobs with different hyperparameters and monitor their progress.

### 3. Inference Process
- **Frame Capture**: The system captures a frame from a live webcam feed.
- **Preprocessing**: The frame is resized to the model's expected input size (e.g., 256x256) while preserving its aspect ratio by padding.
- **Prediction**: The trained `SimpleResNet` model processes the frame and outputs four normalized coordinate values (thumb x/y, index x/y) and, if trained for it, pinch classification logits.
- **Post-processing**: The normalized coordinates are scaled back to the original frame's pixel space, allowing the keypoints to be accurately visualized.

## Technical Details

### Model Architecture
The core of the system is a `SimpleResNet`, a lightweight variant of the popular ResNet architecture. It is designed to be efficient enough for real-time inference while being deep enough to learn complex spatial features from hand images. The final layers of the network are fully connected, outputting either 4 continuous values for keypoint regression or 6 values (4 for keypoints, 2 for pinch classification).

### CUDA-Accelerated Augmentation
To prevent the data pipeline from becoming a bottleneck during training, a custom PyTorch extension was written in C++ and CUDA (`augment.cu`). This module implements transformations like rotation, translation, and resized cropping directly on the GPU. By performing these operations in parallel on the GPU, it avoids costly CPU-to-GPU memory transfers for each augmented batch, leading to a significant speedup in training.

### Training & Experiment Dashboard
A web-based dashboard built with Flask and Chart.js serves as the control center for the project. It allows a user to:
- View and compare all past training runs.
- Launch new training jobs by specifying hyperparameters through a web form.
- Initiate Bayesian hyperparameter sweeps (using `scikit-optimize`) to automatically find the best model configurations.
- Monitor the status of currently running jobs.

## Future Work
- **Dynamic Gesture Recognition**: Incorporate an LSTM or Transformer layer to understand time-based gestures like swiping or drawing shapes.
- **Standalone C++ Inference**: Complete the C++ inference implementation (`main.cpp`) to create a high-performance, dependency-free application.
- **Model Quantization**: Apply techniques like ONNX or TensorRT quantization to optimize the model for deployment on edge devices with limited computational power.