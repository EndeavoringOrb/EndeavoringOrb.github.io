---
layout: archive
title: "Physics Sim"
permalink: /simple_physics_sim/
author_profile: true
---

Overview
======
A simple collision physics simulation written in C++.

How it Works
------
The program spawns in balls that can collide with each other.  
It detects collision using Pythagorean theorem, and uses basic physics principles to handle what happens when a collision is detected.

What's next?
------
Optimize collision detection. Right now each ball is checked with every other ball which is very inefficient. I would like to change it so it only checks balls near to it.   
My plan is to use a grid to divide the screen into squares then only check against balls in the adjacent squares.

Maybe also look into checking the collisions in a certain order, like from bottom of the screen up to make it so you don't need to decrease the gravity speed in order for it to be accurate. Right now if you set the gravity sub-steps too low, then the balls overlap, but if you set sub-steps higher then the simulation doesn't run in real time.

Add a real-time viscosity slider, I think that would be an interesting challenge.

GitHub Links
------
[Image Encoder](https://github.com/EndeavoringOrb/SCAI/blob/main/autoencoders/autoencoder_E0.h5)  
[Damage Sensor Model](https://github.com/EndeavoringOrb/SCAI/blob/main/dmg_models/dmg_model35.h5)  
[Health Sensor Model](https://github.com/EndeavoringOrb/SCAI/blob/main/health_models/health_model105.h5)
