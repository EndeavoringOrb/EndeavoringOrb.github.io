---
layout: archive
title: "Federated Learning"
permalink: /federated_learning/
author_profile: true
---

## Overview

This is a system for training a text generation Recurrent Neural Network (RNN) using multiple clients/computers.

The system consists of a server and multiple clients that work together to train a language model. The server distributes training data and model weights to clients, while clients perform computation and send back rewards (loss values) that are used to update the model's parameters.

### Key Features

- **Distributed Training**: Leverages multiple machines to accelerate training
- **Simple RNN Language Model**: Implements a character-level language model with RNN architecture
- **Efficient Communication**: Custom protocol for sending data between server and clients
- **Gradient-based Optimization**: Uses Adam optimizer for efficient parameter updates

## How It Works

1. The server initializes model weights and starts listening for client connections
2. Clients connect to the server and receive initial weights and configuration
3. For each training step:
    - (Optional, can happen every N steps) Server distributes tokenized text data to clients
    - Clients compute loss values using the current model weights with added noise
    - Clients send loss values back to the server
    - Server normalizes the rewards and sends them back to clients
    - Clients update their local copy of the model weights based on these normalized rewards
    - Periodically, the server requests updated weights from a client to save checkpoints

## Technical Details

### Model Architecture

The system implements a recurrent neural network (RNN) language model with the following components:

- Multiple RNN layers with tanh activation functions
- Hidden state that captures context information
- Output layer that predicts probabilities for the next token
- Support for beam search during generation

### Optimization

The model is trained using:

- Distributed gradient estimation
- Adam optimizer for parameter updates
- Configurable learning rate and other hyperparameters

### Communication Protocol

The system uses a custom communication protocol with:

- Header-based messages specifying data length
- Support for different data types (text, numpy arrays, pickled objects)

More information on the math can be found in this paper I wrote for my Calc 4 final.  
[Federated Learning Project]({% link _pages/federated_learning/files/Federated_Learning_Project.pdf %})

## Future Work
- Optimize training
    - Port to C++
    - Implement sequence packing for higher average batch sizes
- Add support for different model architectures
- Add support for different datasets
- Add support for tool calling