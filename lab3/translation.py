import glfw
from OpenGL.GL import *
import numpy as np

WIN_W, WIN_H = 800, 600

SCALE = 0.2  # Scale integers to fit OpenGL coordinates

def draw_rectangle(color):
    glColor3f(*color)
    glBegin(GL_QUADS)

    glVertex2f(-0.2,  0.2)
    glVertex2f( 0.2,  0.2)
    glVertex2f( 0.2, -0.2)
    glVertex2f(-0.2, -0.2)

    glEnd()


def main():
    if not glfw.init():
        return

    win = glfw.create_window(
        WIN_W, WIN_H,
        "2D Translation using Homogeneous Coordinates (Integer)",
        None, None
    )

    if not win:
        glfw.terminate()
        return

    glfw.make_context_current(win)

    glViewport(0, 0, WIN_W, WIN_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    # ---------------- ORIGINAL POINT (integer) ----------------
    pos_original = np.array([
        [0],   # integer x
        [-3],  # integer y
        [1]
    ], int)

    # ---------------- TRANSLATION MATRIX (integer) ----------------
    tx, ty = 0, 5  # integer translation

    trans = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ], int)

    # ---------------- TRANSLATED POINT ----------------
    pos_translated = trans @ pos_original

    # ---------------- PRINT CALCULATION ----------------
    print("Original Position (Homogeneous):")
    print(pos_original)
    print("\nTranslation Matrix:")
    print(trans)
    print("\nTranslated Position = Translation × Original:")
    print(pos_translated)

    while not glfw.window_should_close(win):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # Draw original rectangle (BLUE)
        glPushMatrix()
        glTranslatef(pos_original[0, 0] * SCALE, pos_original[1, 0] * SCALE, 0)
        draw_rectangle((0, 0, 1))
        glPopMatrix()

        # Draw translated rectangle (GREEN)
        glPushMatrix()
        glTranslatef(pos_translated[0, 0] * SCALE, pos_translated[1, 0] * SCALE, 0)
        draw_rectangle((0, 1, 0))
        glPopMatrix()

        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
