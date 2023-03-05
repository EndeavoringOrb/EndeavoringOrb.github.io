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
Right now I am working with the game Overwatch 2, once the model is functional to a satisfactory degree the plan is to extend to other games.
The core of the program is using reinforcement learning to train the model.
The reinforcement learning uses two neural networks to get the rewards from an action.
It takes an encoded representation of a screenshot of the game as input.
{% include SCAI_diagram.html %}

Sensing Damage
------
SCAI senses damage using a neural network. In Overwatch 2, you have two immediate cues to know when you have done damage. One is an audio cue which is harder to sense using a computer. The second cue is a symbol surrounding your crosshair in the middle of the screen. Depending on what type of shot you hit, the symbol will change. There are 3 main symbols,  
the kill symbol,  
![An image of the kill symbol which is a red skull.](https://github.com/EndeavoringOrb/EndeavoringOrb.github.io/blob/cb48de249f356566fbb90d3e4d632dc647d21bd5/files/kill_shot.png?raw=true)  
the headshot symbol,  
![An image of the headshot symbol which is 4 diagonal red lines going outwards, centered at the crosshair.](https://github.com/EndeavoringOrb/EndeavoringOrb.github.io/blob/cb48de249f356566fbb90d3e4d632dc647d21bd5/files/headshot_plain.png?raw=true)  
the bodyshot symbol,
![An image of the bodyshot symbol which is the same as the headshot symbol except the lines are slightly shorter and they are white instead of red.](https://github.com/EndeavoringOrb/EndeavoringOrb.github.io/blob/cb48de249f356566fbb90d3e4d632dc647d21bd5/files/body_shot.png?raw=true)  
and if there is no symbol around the crosshair, then that means you missed.  
![An image of just the crosshair because if you miss there is no symbol.](https://github.com/EndeavoringOrb/EndeavoringOrb.github.io/blob/cb48de249f356566fbb90d3e4d632dc647d21bd5/files/miss.png?raw=true)  
They symbols can also be mixed together, so if you get a kill when you headshot someone, then it combines the two symbols, and same for a bodyshot + kill. The image below is a body shot + kill.  
![An image showing a bodyshot plus a kill, which is a red skull with the white diagonal lines of a body shot.](https://github.com/EndeavoringOrb/EndeavoringOrb.github.io/blob/cb48de249f356566fbb90d3e4d632dc647d21bd5/files/bodyshot_kill.png?raw=true)  

GitHub Links
------
[Image Encoder](https://github.com/EndeavoringOrb/SCAI/blob/main/autoencoders/autoencoder_E0.h5)  
[Damage Sensor Model](https://github.com/EndeavoringOrb/SCAI/blob/main/dmg_models/dmg_model35.h5)  
[Health Sensor Model](https://github.com/EndeavoringOrb/SCAI/blob/main/health_models/health_model105.h5)
