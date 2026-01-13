import glfw
from OpenGL.GL import *
import numpy as np

WIN_W, WIN_H = 800, 600
SCALE = 0.5  # Scale for OpenGL rendering

def draw_rectangle(color, points):
    glColor3f(*color)
    glBegin(GL_QUADS)
    for i in range(4):
        glVertex2f(points[0, i], points[1, i])
    glEnd()

def main():
    if not glfw.init():
        return

    win = glfw.create_window(
        WIN_W, WIN_H,
        "2D Shearing on Rectangle (Homogeneous)",
        None, None
    )

    if not win:
        glfw.terminate()
        return

    glfw.make_context_current(win)
    glViewport(0, 0, WIN_W, WIN_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-4, 4, -4, 4, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    # ---------------- ORIGINAL RECTANGLE POINTS ----------------
    # Rectangle: bottom-left (0,0), bottom-right (2,0), top-right (2,1), top-left (0,1)
    P = np.array([
        [0, 2, 2, 0],   # x-coordinates
        [0, 0, 1, 1],   # y-coordinates
        [1, 1, 1, 1]    # homogeneous coordinate
    ], float)

    # ---------------- SHEAR MATRIX ----------------
    shx = 1.0  # shear along X-axis
    shy = 0.5  # shear along Y-axis
    Shear = np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0, 0, 1]
    ], float)

    # ---------------- SHEARED RECTANGLE ----------------
    P_sheared = Shear @ P

    # ---------------- TERMINAL OUTPUT ----------------
    print("Original Rectangle Points (Homogeneous):")
    print(P)

    print("\nShear Matrix:")
    print(Shear)

    print("\nSheared Rectangle Points = Shear × P:")
    print(P_sheared)

    while not glfw.window_should_close(win):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # Draw original rectangle (BLUE)
        draw_rectangle((0, 0, 1), P * SCALE)

        # Draw sheared rectangle (RED)
        draw_rectangle((1, 0, 0), P_sheared * SCALE)

        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
