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
        "2D Translation + Scaling (Composite)",
        None, None
    )

    if not win:
        glfw.terminate()
        return

    glfw.make_context_current(win)

    glViewport(0, 0, WIN_W, WIN_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-4, 6, -2, 6, -1, 1)  # extend viewport for both triangles
    glMatrixMode(GL_MODELVIEW)

    # ---------------- ORIGINAL TRIANGLE POINTS ----------------
    P = np.array([
        [0, 1, 0.5],  # x-coordinates
        [0, 0, 1],    # y-coordinates
        [1, 1, 1]     # homogeneous coordinate
    ], float)

    # ---------------- TRANSLATION MATRIX ----------------
    tx, ty = 3, 3  # move right and up so triangles do not overlap
    T = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ], float)

    # ---------------- SCALING MATRIX ----------------
    S = np.array([
        [2, 0, 0],  # 2x scaling
        [0, 2, 0],
        [0, 0, 1]
    ], float)

    # ---------------- COMPOSITE MATRIX ----------------
    # Apply scaling AFTER translation: Composite = S × T
    Composite = S @ T
    P_transformed = Composite @ P

    # ---------------- TERMINAL OUTPUT ----------------
    print("Original Triangle Points (Homogeneous):\n", P)
    print("\nTranslation Matrix:\n", T)
    print("\nScaling Matrix (2x):\n", S)
    print("\nComposite Transformation Matrix (S × T):\n", Composite)
    print("\nTransformed Triangle Points = Composite × P:\n", P_transformed)

    while not glfw.window_should_close(win):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # Draw original triangle (BLUE)
        draw_triangle((0, 0, 1), P * SCALE)

        # Draw transformed triangle (RED)
        draw_triangle((1, 0, 0), P_transformed * SCALE)

        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
