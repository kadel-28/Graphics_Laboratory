import glfw
from OpenGL.GL import *
import numpy as np

WIN_W, WIN_H = 800, 600
SCALE_VIEW = 0.5  # for OpenGL visibility


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
        "Translation (3,3) + X-Shearing (Composite)",
        None, None
    )

    if not win:
        glfw.terminate()
        return

    glfw.make_context_current(win)

    glViewport(0, 0, WIN_W, WIN_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 8, -2, 8, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    # ---------------- ORIGINAL TRIANGLE ----------------
    P = np.array([
        [0, 1, 0.5],
        [0, 0, 1],
        [1, 1, 1]
    ], float)

    # ---------------- TRANSLATION MATRIX ----------------
    tx, ty = 2, 2
    T = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ], float)

    # ---------------- X-SHEARING MATRIX ----------------
    shx = 1.0
    Shx = np.array([
        [1, shx, 0],
        [0, 1,   0],
        [0, 0,   1]
    ], float)

    # ---------------- COMPOSITE MATRIX ----------------
    # Shearing after translation
    Composite = Shx @ T
    P_transformed = Composite @ P

    # ---------------- TERMINAL OUTPUT ----------------
    print("Original Triangle Points (Homogeneous):")
    print(P)

    print("\nTranslation Matrix (3,3):")
    print(T)

    print("\nX-Shearing Matrix:")
    print(Shx)

    print("\nComposite Matrix = Shx × T:")
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
