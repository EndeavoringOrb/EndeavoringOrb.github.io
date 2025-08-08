---
layout: archive
title: "Shakespeare Generator"
permalink: /shak_gen/
author_profile: false
---

## Project Overview {#overview}

This is a language model trained on Shakespeare's works. A Shakespeare generator.

## What did I do? {#project-explanation}

### 1. I got some data {#getting-data}
I downloaded shakespeare's works from the [Folger Shakespeare Library](https://www.folger.edu/explore/shakespeares-works/download/).

### 2. I cleaned and formatted the text. {#data-cleaning}
- Plays are split up into paragraphs. Each paragraph is one training example. I clean it up a bit, like not taking the names or scene changes and whatnot.
- Each sonnet is one training example.

### 3. I tokenized the text. {#tokenizing}
- I used a character level tokenization scheme, so (a, 0), (b, 1), etc.
- There are 65 tokens, one of which I almost definitely don't need (the start token @) but it's not broken so I don't feel like changing it right now. But it would be nice to remove that start token so I can have exactly 64 tokens which is a nice number. I also want to try adding a "capital" character so "A" -> "capital"+"a" which would allow me to remove all capital letters from the vocabulary.
- I tokenized all the text and saved it in a binary file with a custom format using struct.pack to save space and stuff.
- Encoding/decoding is really easy because it is just two dictionaries string2int and int2string.

### 4. I define the model architecture. {#model-architecture}
- Nothing original, just a long short-term memory ([LSTM](https://en.wikipedia.org/wiki/Long_short-term_memory)) recurrent neural network ([RNN](https://en.wikipedia.org/wiki/Recurrent_neural_network)).

### 5. Train the model. {#training}
- Optimization! yippee
    - I implemented batch training which was kind of a pain because the sequences aren't the same length so you have to drop sequences as they run out of tokens which is fine, but then by the end of the batch when you're finishing the longest sequence you aren't getting the speedup of batch training anymore cause you're back to 1 sequence again. I've thought about maybe trying to pack sequences in together so you have one thing in the batch be lengths 2+2 and another be 4. But that's complicated especially with pytorch and making sure you don't mess up the gradients for autograd.
    - I made the training go a bit faster by precomputing a couple values at the beginning of each batch.
- Setting learning rates, finding optimal hyperparameters, waiting for forever, not even setting up a test/train split cause there isn't a lot of data and the models I'm training aren't that big anyway so they probably won't overfit too bad.

### 6. Using the trained model. {#inference}
  - Again, precompute some values to make inference faster.
  - Made a little [web app](endeavoringorb.com/shak-gen) to interface with it.

## Tech Stack {#tech-stack}
  - Python
  - Pytorch
  - Flask

## Key Concepts {#key-concepts}
AI, NLP, Web-Dev, Data Cleaning, Performance Optimization

## Future Work {#future-work}
Maybe I'll make a public github so people can train & run it locally.

## Resources {#resources}
  - Heavily inspired by [Andrej Karpathy](https://karpathy.github.io/2015/05/21/rnn-effectiveness/).
  - Shakespeare's work downloaded from [Folger Shakespeare Library](https://www.folger.edu/explore/shakespeares-works/download/).
  - [PyTorch](https://pytorch.org/get-started/locally/)