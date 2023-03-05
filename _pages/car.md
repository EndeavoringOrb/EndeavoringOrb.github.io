---
layout: archive
title: "Car"
permalink: /car_racing_model/
author_profile: true
---

Overview
======
The goal of this project is to make a car go as fast as possible around a track without touching the sides. The car will learn how to do this through reinforcement learning.

How it Works
------
The car has 8 lines that extend outwards from it that measure distance to the nearest wall. These eight distances are used as the input to the reinforcement learning model.  
The track that it is driving on is actually just a numpy array of values, where white is 1 and black is 0. It uses a function to find the nearest black item in the numpy array in a certain direction, which gives it the distance to the wall.  
![Image of Overwatch 2](https://github.com/EndeavoringOrb/EndeavoringOrb.github.io/blob/main/files/fullscreen_training_room2.png?raw=true)

What's next?
------
Change the rewards from dots that give a reward when you drive over them to lines that cross the track that give a reward when you drive over them.  
Add zoomed in viewer and more advanced racecourse maker. With those two things together you would be able to make racetracks larger than the screen size.  

GitHub Links
------
[Racetrack Creator](https://github.com/EndeavoringOrb/RL_car/blob/main/make_racecourse.py)  
[Racing Track for Humans](https://github.com/EndeavoringOrb/RL_car/blob/main/car_racing.py)  
[Racing Track for Robots](https://github.com/EndeavoringOrb/RL_car/blob/main/car_racing_test.py)  
[Current Best Model](https://github.com/EndeavoringOrb/RL_car/blob/main/ppo_model6/94208.zip)
[Train a model](https://github.com/EndeavoringOrb/RL_car/blob/main/SB3train.py)