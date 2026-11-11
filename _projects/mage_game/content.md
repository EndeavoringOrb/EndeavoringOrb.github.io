## Project Overview {#overview}

This is the game I eventually want to make: a mage dueling game where you cast spells with your hands. You draw spell symbols in the air in front of a webcam, and the symbols combine into spells. This project is the game and the engine I'm building for it, written from scratch in C++. That includes the renderer: there's no OpenGL or DirectX in the render path, and every pixel is computed on the CPU.

<video src="/static/files/mage_game/demo.mp4" controls autoplay muted loop playsinline style="max-width: 100%;"></video>

*The character (cyan) and its cloth cape casting shadows from the sun and from a point light above the fire on the blue cube. The black panel in the top left is a debug view of a shadow map.*

## Software Renderer {#renderer}

### Pipeline {#pipeline}

Each frame goes through these steps:

1. **Shadow maps:** Render the scene's depth from every light's point of view.
2. **Geometry:** Transform, clip and rasterize every triangle, writing color, depth, normal and world position for each pixel. Triangles crossing the camera's near plane are **clipped** into one or two smaller triangles, so geometry behind the camera never gets drawn.
3. **Lighting:** For each pixel, add up the light from every light, checking the shadow maps to see whether the pixel is in shadow.
4. **Edge shading:** A post-process pass that outlines silhouettes and creases.
5. **Effects:** Particle fire, drawn on top.

The scene renders at a low internal resolution (256 pixels tall) and is scaled up to the window, which gives it a chunky, pixel-art look and keeps the CPU cost manageable. The camera is orthographic, looking down at an angle.

### Shadows {#shadows}

Shadows use **shadow mapping**: render depth from the light's point of view, then a pixel is in shadow if something sits closer to the light than it does.

- **Directional light (the sun)** uses **cascaded shadow maps**. The camera's view is split into slices by distance, each with its own shadow map, so nearby shadows stay sharp without needing one giant map. The split points blend even and logarithmic spacing, and each cascade gets an orthographic light camera fitted tightly around its slice of the view.
- **Point lights** render **six shadow maps**, one for each face of a cube around the light, each with a 90° field of view. To shade a pixel, the renderer picks the face pointing toward that pixel.
- Shadow maps are drawn by the same CPU rasterizer as the main view. A debug mode shows the shadow maps on screen.

### Edge Shading & Look {#style}

To make shapes read clearly at low resolution, a post-process pass compares each pixel's depth and normal with its neighbors'. Where the depth jumps (a silhouette), the pixel is darkened into an outline. Where the normal changes (an edge between two faces), it's brightened into a highlight.

### Fire {#fire}

Fire is a particle effect. Each particle's color comes from a temperature-style ramp, based on real flame colors: dark red, then cherry red, orange, yellow and finally white for the hottest parts.

## Physics {#physics}

- **Verlet integration** for particles, which makes constraints simple and stable.
- **Cloth** made of particles connected by distance constraints, solved over several iterations per frame. Some particles can be pinned, which is how the character's cape attaches to the shoulders.
- **Character controller:** WASD movement and a jump with a set height and duration.

## Gameplay Prototype {#gameplay}

Before the 3D renderer, I prototyped the combat in 2D:

- Spells are built from **spell words**: a type, a form (arrow, laser, bomb, wave…) and affinities (fire, water, speed…), with affinities designed to combine into new effects.
- Laser and bomb attacks, a burn damage-over-time effect, health bars, mana, a dash, and circle and rectangle hitboxes.
- The plan is to draw each spell word with your hand: pinch your fingers to draw a symbol on a canvas, then release to cast at that point. The [hand tracking](/projects_html/hand_tracking.html) project is the input side of this.

## Where It's At {#status}

The renderer has working lighting, cascaded and point-light shadows, clipping, edge shading, cloth and fire. Water and volumetric fluid rendering are in progress. The 2D combat prototype and the 3D renderer haven't been joined into one game yet.

This grew out of an earlier, simpler engine with flat lighting and no shadows:

<video src="/static/files/mage_game/early_engine.mp4" controls muted loop playsinline style="max-width: 100%;"></video>

*The earlier engine: the character (an icosahedron for now) walking and jumping, with the blue cape simulated as cloth.*

## Technology Stack {#tech-stack}
- C++
- GLM (vector math)
- SFML (window, input, and putting the pixel buffer on screen)
