import glfw
from OpenGL.GL import *
import numpy as np
import math

WIN_W, WIN_H = 800, 600
SCALE = 0.5  # Scale to fit OpenGL coordinates


def draw_triangle(color, points):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    for i in range(3):
        glVertex2f(points[0, i], points[1, i])
    glEnd()


def main():
    if not glfw.init():
        return

    win = glfw.create_window(
        WIN_W, WIN_H,
        "2D Rotation 60° Clockwise (Homogeneous)",
        None, None
    )

    if not win:
        glfw.terminate()
        return

    glfw.make_context_current(win)

    glViewport(0, 0, WIN_W, WIN_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    # ---------------- ORIGINAL TRIANGLE POINTS ----------------
    P = np.array([
        [0, 1, 0.5],
        [0, 0, 1],
        [1, 1, 1]
    ], float)

    # ---------------- ROTATION MATRIX 180° CLOCKWISE ----------------
    theta = math.radians(180)
    cos_t = math.cos(-theta)  # clockwise
    sin_t = math.sin(-theta)
    R = np.array([
        [cos_t, -sin_t, 0],
        [sin_t,  cos_t, 0],
        [0, 0, 1]
    ])

    # ---------------- ROTATED POINTS ----------------
    P_rotated = R @ P

    # ---------------- PRINT CALCULATION ----------------
    print("Original Triangle Points (Homogeneous):")
    print(P)

    print("\nRotation Matrix (60° clockwise):")
    print(R)

    print("\nRotated Triangle Points = R × P:")
    print(P_rotated)

    while not glfw.window_should_close(win):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # Draw original triangle (BLUE)
        draw_triangle((0, 0, 1), P * SCALE)

        # Draw rotated triangle (RED)
        draw_triangle((1, 0, 0), P_rotated * SCALE)

        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
