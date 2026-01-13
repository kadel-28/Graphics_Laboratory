import glfw
from OpenGL.GL import *
import numpy as np
import math

WIN_W, WIN_H = 800, 600
SCALE_VIEW = 0.5  # Only for fitting into OpenGL window


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
        "Rotation (60°) + Scaling (0.5) Composite",
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

    # ---------------- ORIGINAL TRIANGLE ----------------
    P = np.array([
        [0, 1, 0.5],
        [0, 0, 1],
        [1, 1, 1]
    ], float)

    # ---------------- ROTATION MATRIX (60° ANTICLOCKWISE) ----------------
    theta = math.radians(60)
    R = np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta),  math.cos(theta), 0],
        [0,               0,               1]
    ], float)

    # ---------------- SCALING MATRIX (0.5) ----------------
    S = np.array([
        [0.5, 0,   0],
        [0,   0.5, 0],
        [0,   0,   1]
    ], float)

    # ---------------- COMPOSITE MATRIX ----------------
    # Scaling after rotation
    Composite = S @ R
    P_transformed = Composite @ P

    # ---------------- TERMINAL OUTPUT ----------------
    print("Original Triangle Points (Homogeneous):")
    print(P)

    print("\nRotation Matrix (60° anticlockwise):")
    print(R)

    print("\nScaling Matrix (0.5):")
    print(S)

    print("\nComposite Matrix = S × R:")
    print(Composite)

    print("\nTransformed Triangle Points = Composite × P:")
    print(P_transformed)

    while not glfw.window_should_close(win):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # Original triangle (BLUE)
        draw_triangle((0, 0, 1), P * SCALE_VIEW)

        # Transformed triangle (RED)
        draw_triangle((1, 0, 0), P_transformed * SCALE_VIEW)

        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
