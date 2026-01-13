import glfw
from OpenGL.GL import *
import numpy as np

WIN_W, WIN_H = 800, 600
SCALE = 0.5  # Scale for OpenGL rendering

def draw_triangle(color, points):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    for i in range(3):
        glVertex2f(points[0, i], points[1, i])
    glEnd()

def draw_axes():
    glColor3f(1, 1, 1)  # White axes
    glBegin(GL_LINES)
    # X-axis
    glVertex2f(-4, 0)
    glVertex2f(4, 0)
    # Y-axis
    glVertex2f(0, -3)
    glVertex2f(0, 3)
    glEnd()

def main():
    if not glfw.init():
        return

    win = glfw.create_window(
        WIN_W, WIN_H,
        "2D Reflection about X-axis with Gap",
        None, None
    )

    if not win:
        glfw.terminate()
        return

    glfw.make_context_current(win)
    glViewport(0, 0, WIN_W, WIN_H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-4, 4, -3, 3, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    # ---------------- ORIGINAL TRIANGLE POINTS ----------------
    # x: 2 units away from Y-axis, y: 2 units above X-axis
    P = np.array([
        [2, 3, 2.5],  # x-coordinates
        [2, 2, 3],    # y-coordinates
        [1, 1, 1]     # homogeneous coordinate
    ], float)

    # ---------------- REFLECTION MATRIX ABOUT X-AXIS ----------------
    Rx = np.array([
        [1,  0, 0],
        [0, -1, 0],
        [0,  0, 1]
    ], float)

    # ---------------- REFLECTED TRIANGLE ----------------
    P_reflected = Rx @ P

    # ---------------- TERMINAL OUTPUT ----------------
    print("Original Triangle Points")
    print(P)

    print("\nReflection Matrix about X-axis:")
    print(Rx)

    print("\nReflected Triangle Points = Rx × P:")
    print(P_reflected)

    while not glfw.window_should_close(win):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # Draw axes
        draw_axes()

        # Draw original triangle (BLUE)
        draw_triangle((0, 0, 1), P * SCALE)

        # Draw reflected triangle (RED)
        draw_triangle((1, 0, 0), P_reflected * SCALE)

        glfw.swap_buffers(win)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
