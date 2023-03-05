---
layout: archive
title: "Car"
permalink: /car_racing_model/
author_profile: true
---

Overview
======
The goal of this project is to make a car go very fast around a track without touching the sides. The car will learn how to do this through reinforcement learning.

How it Works
------
The car has 8 lines that extend outwards from it that measure distance to the nearest wall. These eight distances are used as the input to the reinforcement learning model.  
The track that it is driving on is actually just a numpy array of values, where white is 1 and black is 0. It uses a function to find the nearest black item in the numpy array in a certain direction, which gives it the distance to the wall.

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
