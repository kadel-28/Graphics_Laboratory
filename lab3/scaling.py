import glfw
from OpenGL.GL import *
import numpy as np

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
        "2D Scaling 2x (Homogeneous)",
        None, None
    )

    if not win:
        glfw.terminate()
        return

    glfw.make_context_current(win)

    glViewport(0, 0, WIN_W, WIN_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 4, -2, 4, -1, 1)  # Extend the viewport to see scaling
    glMatrixMode(GL_MODELVIEW)

    # ---------------- ORIGINAL TRIANGLE POINTS ----------------
    P = np.array([
        [0, 1, 0.5],
        [0, 0, 1],
        [1, 1, 1]
    ], float)

    # ---------------- SCALING MATRIX (0.5x) ----------------
    S = np.array([
        [0.5, 0, 0],
        [0, 0.5, 0],
        [0, 0, 1]
    ], float)

    # ---------------- SCALED POINTS ----------------
    P_scaled = S @ P

    # ---------------- TERMINAL OUTPUT ----------------
    print("Original Triangle Points (Homogeneous):")
    print(P)

    print("\nScaling Matrix (0.5):")
    print(S)

    print("\nScaled Triangle Points = S × P:")
    print(P_scaled)

    while not glfw.window_should_close(win):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # Draw original triangle (BLUE)
        draw_triangle((0, 0, 1), P * SCALE)

        # Draw scaled triangle (RED)
        draw_triangle((1, 0, 0), P_scaled * SCALE)

        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
