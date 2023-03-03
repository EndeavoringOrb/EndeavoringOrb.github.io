---
layout: archive
title: "SCAI"
permalink: /scai/
author_profile: true
---

Overview
======
SCAI (Screenshot AI) is a project that seeks to build neural networks to play complex games based solely off the pixel values of the screen.

How SCAI Works
------
Right now I am working with Overwatch 2, once the model is functional to a satisfactory degree the plan is to extend to other games.
The core of the program is using reinforcement learning to train the model.
The reinforcement learning uses two neural networks to get the rewards from an action.
It takes an encoded representation of a screenshot of the game as input.
{% include SCAI_diagram.html %}

GitHub Links
------
[https://github.com/EndeavoringOrb/SCAI/blob/main/autoencoders/autoencoder_E0.h5]Image Encoder
[https://github.com/EndeavoringOrb/SCAI/blob/main/dmg_models/dmg_model35.h5]Damage Sensor Model
[https://github.com/EndeavoringOrb/SCAI/blob/main/health_models/health_model105.h5]Health Sensor Model