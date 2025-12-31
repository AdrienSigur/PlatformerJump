# 🍄 Pygame Platformer Engine

A 2D platformer prototype built from scratch with **Python** and **Pygame**. 
This project focuses on learn class and loop

## 📸 Demo

<img width="1282" height="752" alt="image" src="https://github.com/user-attachments/assets/235cbf46-f2e4-4006-bb23-45752cb578db" />

## ✨ Features

* **Custom Physics Engine:** Implements gravity, acceleration, and velocity accumulation ($V_f = V_i + a \times t$).
* **Precise Collision Detection:** Uses AABB (Axis-Aligned Bounding Box) logic.
* **Axis Separation:** Handles X and Y movements independently to allow sliding against walls and perfect landing detection.
* **Debug Mode:** Visualizes hitboxes (red rectangles) to track player position and collision boundaries.
* **Sprite Handling:** Uses `surface.blit()` with distinct hitbox management for logical positioning.

## 🕹️ Controls (AZERTY Layout)

The game is currently mapped for AZERTY keyboards (standard in France):

| Action | Key |
| :--- | :--- |
| **Move Left** | `Left-arrow` |
| **Move Right** | `Right-arrow` |
| **Jump** | `SPACE` |
| **Quit** | `ESC` or Close Window |

## 🧠 How it Works

### The Physics Logic
Instead of fixed movement, the player is controlled by **forces**.
* **Gravity** is applied every frame to the vertical velocity (`velocity_y`).
* **Jumping** applies an instantaneous negative force.
* The system uses `dt` (delta time) to ensure movement is smooth regardless of the framerate.

```python
# Gravity calculation example
self.velocity_y += self.gravity * dt
self.pos.y += self.velocity_y * dt

```

