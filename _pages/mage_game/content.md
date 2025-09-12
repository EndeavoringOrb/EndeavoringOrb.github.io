---
layout: archive
title: "mageGame"
permalink: /mage_game/
author_profile: false
---

## Overview

*mageGame* is a roguelike action game where you play as a fledgling mage defending your world from a demonic invasion. Descending into the dungeon from which the demons emerged, you must master a unique and flexible spell-crafting system to survive. The game is built from the ground up in C++ and features a custom 3D software renderer, a Verlet integration-based physics engine, and dynamic particle systems.

The core of the gameplay revolves around crafting custom spells by drawing magical symbols. Each symbol corresponds to a "word" of power, and by combining these words, you can create a vast array of unique and powerful magical effects.

### Key Features

- **Dynamic Spell Crafting**: Combine spell components—Type (Attack, Heal), Form (Projectile, Wave), and Affinity (Fire, Water)—to create unique abilities on the fly.
- **Gesture-based Casting**: Draw symbols directly on a magical canvas to build and cast your spells.
-   **Physics-Driven World**: A custom physics engine using Verlet integration governs character movement, realistic cloth simulation, and complex particle effects.
- **Custom 3D Software Renderer**: The game is rendered without relying on standard graphics APIs like OpenGL. The engine supports:
    - Dynamic lighting with multiple light sources (point and directional).
    - Cascaded shadow mapping for realistic, large-scale shadows.
    - Advanced CPU-based particle systems for fire and water effects.
- **Roguelike Progression**: Fight through procedurally generated rooms, defeat powerful minibosses to advance to new floors, and discover new spell words to expand your arcane arsenal with each run.

## Gameplay Mechanics

### The Spell Crafting System

1.  **Drawing Symbols**: Players use a [gesture-based system](/airhandwriter/) to draw symbols on a canvas. Each recognized symbol corresponds to a "word" of power.
2.  **Combining Words**: Spells are constructed from three types of words:
    - **Type**: Defines the spell's fundamental purpose (e.g., *Attack*, *Heal*, *Trap*).
    - **Form**: Dictates the spell's shape and delivery (e.g., *Sphere Projectile*, *Laser*, *Wave*).
    - **Affinity**: Imbues the spell with elemental properties (e.g., *Fire* for burning, *Water* for knockback).
3.  **Casting**: Once a spell is assembled, the player enters a "cast mode" to aim and unleash their creation at enemies. The system allows for thousands of potential spell combinations, encouraging creativity and strategic thinking.

### Combat and Progression

Combat is fast-paced and requires players to adapt their spell-crafting strategy to different enemy types and environments. Enemies have unique behaviors and elemental weaknesses. As you descend deeper into the dungeon, you'll find new, more powerful spell words, permanently expanding your capabilities for future runs.

## Technical Details

### Custom Graphics Engine

The game is powered by a bespoke 3D software renderer written entirely in C++.
- **Rasterization**: Triangles are projected from 3D world space to 2D screen space and rasterized to a pixel buffer on the CPU. The pipeline includes depth buffering, frustum culling, and triangle clipping.
- **Lighting and Shadows**: The engine supports dynamic point and directional lights. Shadows are calculated using cascaded shadow mapping for directional lights to ensure high-quality shadows across large distances, and 6-face shadow maps (cubemaps) for point lights.
- **Particle Systems**: Sophisticated particle effects for fire and water are simulated and rendered on the CPU, adding life and dynamism to the world.

### Physics Engine

The physics simulation is built on **Verlet Integration**, providing a (mostly) stable and efficient foundation for various physical phenomena:
- **Cloth Simulation**: A particle-spring system is used to simulate realistic cloth physics, which can be attached to characters or objects in the environment.
- **Collision Detection**: A custom collision system resolves interactions between particles, characters, and the game world.

## Future Work
- **GPU Acceleration**: Port the custom software renderer to a modern graphics API like OpenGL or Vulkan to leverage GPU hardware for a massive performance increase.
- **Expanded Content**: Add more spell words, enemy types, bosses, and diverse environments to deepen the gameplay loop.
- **Wave Form Attacks**: Implement new spell forms, such as the planned "wave" attack, to provide more strategic options in combat.
- **UI and Sound**: Develop a complete user interface for inventory and spell management, and add sound effects and music to enhance immersion.
- **Gesture Recognition**: Finish the [hand keypoint detection models](/airhandwriter/) and integrate them into the game.