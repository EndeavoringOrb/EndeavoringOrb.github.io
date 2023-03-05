---
layout: archive
title: "Car"
permalink: /RL_car/
author_profile: true
---

Overview
======
The goal of this project is to make a car go as fast as possible around a track without touching the sides. The car will learn how to do this through reinforcement learning.

How it Works
-----
The car has 8 lines that extend outwards from it that measure distance to the nearest wall. These eight distances are used as the input to the reinforcement learning model.  
The track that it is driving on is actually just a numpy array of values, where white is 1 and black is 0. It uses a function to find the nearest black item in the numpy array in a certain direction, which gives it the distance to the wall.  

The image below is a racetrack I created. The black is a wall, the white is the track, and the purple dots are the reward dots. The two green dots are the front of the car, the two blue dots are the back of the car. The red dots are the sensors, they mark the wall in a certain direction with respect to the car.  

![Image of a racetrack.](https://github.com/EndeavoringOrb/EndeavoringOrb.github.io/blob/main/files/racetrack.png?raw=true)  

If you want to play around with it a bit, then go to the link at the bottom of this page labeled "Racing Track for Humans". If you run that python file you will be able to race on that racetrack. In order to do that you need to have config2.npy, image2.npy and image2.png in order to get that specific racetrack, otherwise you have to create your own with the racetrack creator.  

Racetrack Creator
-----
When you start this program a 1000x1000 window will pop up.  
- To draw a track you left-click and drag.  
- To add the reward points, move your mouse to where you want the point then press space.  
- To add the starting point, press "s" on the keyboard ONCE.  
- To save the racetrack, press "s" again.  

Racetrack for Robots
-----
Steps for running:  
- First change the file path at the beginning of the program to the path of the model you want to use.
- Then change the img_num to the racetrack number. The img_num is the number in the config file and the image files (i.e. config2.py means img_num should be 2 if you want that racetrack).
- Other variables are explained in comments in file.

Train a model
-----
Steps for running:
- img_num should be set to the racetrack number you want to use
- steps controls the max timesteps the simulation can run before restarting
- the model number input is just for saving the models so you can have different versions
The model will be saved as a .zip file.

What's next?
-----
Change the rewards from dots that give a reward when you drive over them to lines that cross the track that give a reward when you drive over them.  
Add zoomed in viewer and more advanced racecourse maker. With those two things together you would be able to make racetracks larger than the screen size.  

GitHub Links
-----
[Racetrack Creator](https://github.com/EndeavoringOrb/RL_car/blob/main/make_racecourse.py)  
[Racetrack for Humans](https://github.com/EndeavoringOrb/RL_car/blob/main/car_racing.py)  
[Racetrack for Robots](https://github.com/EndeavoringOrb/RL_car/blob/main/car_racing_test.py)  
[Current Best Model](https://github.com/EndeavoringOrb/RL_car/blob/main/ppo_model6/94208.zip)
[Train a model](https://github.com/EndeavoringOrb/RL_car/blob/main/SB3train.py)