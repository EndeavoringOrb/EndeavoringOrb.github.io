---
layout: archive
title: "UNet-based Lossless Image Compression"
permalink: /image_compression/
author_profile: false
---

## Overview

This project implements an image compression system that uses a neural network to achieve high compression ratios. The core of the system is a UNet with an attention mechanism, which outputs per-pixel probabilities for an arithmetic coder.

### Key Features

- **Neural Compression**: Utilizes a UNet with self-attention to predict pixel probabilities, forming the basis of a learned compression scheme.
- **High Compression Ratios**: Aims for state-of-the-art lossless compression by accurately modeling complex image features.
- **Variable-Size Image Support**: An innovative pre/post-processing pipeline allows a fixed-size core model to compress images of any dimension without retraining.
- **Fast-ish Arithmetic Coding**: Arithmetic coder implemented in C++ with python bindings.
- **Attention Mechanism**: The UNet has attention layers which perform better than conv layers alone.

## How It Works

### Encoding Process

1. The input image is passed through a conv layer N times, until it is small enough to fit in the model's core resolution. I do this so the model can handle any sized input image but I can still have a fixed core resolution for the attention mechanism.
2. N DoubleConv layers. A DoubleConv layer is (conv, rms_norm, relu) x2.
3. One last DoubleConv at the bottleneck.
4. N upconv (nn.ConvTranspose2d) layers.
5. Encode the image to bits using the model's output probabilities and an arithmetic coder.
6. Store the bottleneck output, z, and the encoded image bits in a file.

### Decompression Process

1. Read bottleneck output, z, and encoded image bits from file.
2. N upconv (nn.ConvTranspose2d) layers.
3. Use the model's output probabilities and an arithmetic coder with the encoded image bits to decode the original image.

## Technical Details

### Model Architecture

(coming soon)

### Arithmetic Coding

(coming soon, but there is a great explanation here by Matt Mahoney: [Data Compression Explained](https://mattmahoney.net/dc/dce.html))

### File Format Specification

(coming soon)

## Future Work
- **Performance Optimization**: Port the entire inference and coding pipeline to C++ (with CUDA) to create a standalone, high-performance command-line tool.
- **Color Image Support**: Extend the model and data pipeline to handle 3-channel (RGB) images.
- **Lossy Compression**: Investigate lossy compression variants by quantizing the latent space.
- **LoRA/QLoRA**: Training a model LoRA per-image like [this](https://arxiv.org/abs/2412.17464).