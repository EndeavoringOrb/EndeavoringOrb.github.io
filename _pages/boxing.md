---
layout: archive
title: "Reinforcement Learning - Warrior"
permalink: /RL_warrior/
author_profile: true
---

Overview
======
My friend and I are in the process of making a simple VR game. The game is going to be a sort of free-for-all fighting game, but we wanted the opponents to be very challenging, to the point where you have to practice to beat them.
I could hard code a bunch of rules for the enemies, but I decided to see if I could train a neural network to control the enemy instead.
So this project is trying to train a neural network that is able to fight as well as, or better than, a human.

How it Works
-----
I am using [MuJoCo](https://mujoco.org/) for the training environment. Mujoco is a physics engine currently owned and maintained by DeepMind. It is very fast, and has Python bindings which makes it easy to use with [Pytorch](https://pytorch.org/), the ML framework I have chosen to use for this project.
The network controls the humanoid model with 21 values which correspond to actuators for each of the joints.
As input, the network takes (1) the position and velocity of all its joints and the joints of its opponent and (2) the distance to it's opponent. The eventual goal is to have the agent train in an environment with many agents, but for now I have simplified it to one on one competition.

At the moment I am seperating the training into phases. Each phase will have a different reward system. The idea is that the agent/network learns to do tasks with increasing levels of difficulty instead of it learning to box from scratch.
 - Phase 1 - Standing:
    - I will first train the agent to stand, the velocities and positions of the other agent will be set randomly each training step, I think this will make the model avoid developing a dependency on those inputs in this phase.
    - Rewards:
        - How high the head is
        - How upright the torso is
 - Phase 2 - Moving:
    - I will train the model to move around without falling over. Other agent's velocities and positions will still be randomized.
    - Rewards:
        - I will reward it for maintaining a certain distance from the other agent. I will move the other agent around manually, and the learning agent will have to learn how to move effectively to maintain a certain distance.
        - How high the head is (reward amount lessened, but still implemented so it doesn't completely unlearn standing)
        - How upright the torso is (reward amount lessened, but still implemented so it doesn't completely unlearn standing)
 - Phase 3 - Boxing:
    - Training the agents to box eachother.
    - Rewards:
        - Hitting the other agent with your fist
        - Negative reward for getting hit by the other agent
        - How high the head is (reward amount lessened, but still implemented so it doesn't completely unlearn standing)
        - How upright the torso is (reward amount lessened, but still implemented so it doesn't completely unlearn standing)
        - No more reward for moving, I am not sure what will happen when i take that reward away, I am also not entirely sure that reward will be helpful in the learning process. I will experiment with removing Phase 2.
 - Phase 4 - Weapons?:
    - If I am satisfied with the performance of the boxing, I will consider adding weapons.

What's next?
-----
Adding an Actor-Critic network architecture so I can have the network output continuous actions instead of discrete actions. Then I will retrain Phase 1 of the network.

GitHub Links
-----
[Github Repository](https://github.com/EndeavoringOrb/warrior)