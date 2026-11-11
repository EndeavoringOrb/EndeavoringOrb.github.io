## Project Overview {#overview}

A 3D engine written from scratch in C++, including the renderer. I built it as the base for the RPG I want to make, first inside [nextGenRPG](https://github.com/EndeavoringOrb/nextGenRPG) and later split out into its own repo.

The current demo is a third-person character you walk around and jump with, wearing a cape that is physically simulated cloth pinned to the character's shoulders.

<video src="/static/files/engine_3d/demo.mp4" controls autoplay muted loop playsinline style="max-width: 100%;"></video>

*The character (an icosahedron for now) walking and jumping, with the blue cape simulated as cloth. Every pixel is rendered on the CPU.*

## Rendering {#rendering}

There is no OpenGL or DirectX in the render path: every pixel is computed on the CPU and written into a pixel buffer, which SFML then just puts on screen. That meant writing the whole pipeline myself:

- **Camera and projection:** Transforming vertices from world space into screen space.
- **Clipping:** Triangles that cross the camera's near plane have to be clipped before projection, or they turn into garbage on screen. Getting this right (including triangles with vertices behind the camera) was one of the harder parts.
- **Rasterization:** Filling triangles pixel by pixel, with a **depth buffer** so closer surfaces hide farther ones.
- **Lighting:** Flat shading from a directional light, using each face's normal.

## Physics {#physics}

- **Verlet integration** for particles: each particle stores its current and previous position, which makes constraints simple and stable.
- **Cloth:** A grid of particles connected by distance constraints ("links"), solved over several iterations per frame. Some particles can be pinned in place, which is how the cape attaches to the character's shoulders.
- **Character controller:** WASD movement with a third-person camera that follows the character, and a jump that follows a parabolic arc with a set height and duration, so the jump can be tuned directly.

## Meshes & Geometry {#geometry}

- Generating meshes procedurally: planes, icosahedrons, extruded faces, projecting a mesh onto the unit sphere, and building the dual of a mesh.
- A scene system that can draw meshes it owns and meshes owned elsewhere (like the cloth, which updates its own vertices every frame).

## What I Learned {#learned}

Writing a renderer by hand made the graphics pipeline concrete for me: why clipping happens where it does, what a depth buffer actually costs, and why GPUs exist (a CPU rasterizer runs out of time fast as triangle counts go up). It also gave me a feel for keeping simulation stable at real-time frame rates.

## Technology Stack {#tech-stack}
- C++
- GLM (vector math)
- SFML (window, input, and putting the pixel buffer on screen)
