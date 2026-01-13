import glfw
import sys
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D


def clip(x1, y1, x2, y2, xm, ym, xM, yM):
    dx = x2 - x1
    dy = y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xm, xM - x1, y1 - ym, yM - y1]

    u1, u2 = 0.0, 1.0

    for pi, qi in zip(p, q):
        if pi == 0 and qi < 0:
            return False, None

        if pi != 0:
            u = qi / pi
            if pi < 0:
                u1 = max(u1, u)
            else:
                u2 = min(u2, u)

    if u1 > u2:
        return False, None

    return True, (
        x1 + u1 * dx,
        y1 + u1 * dy,
        x1 + u2 * dx,
        y1 + u2 * dy
    )


def draw_line(x1, y1, x2, y2, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_rect(xm, ym, xM, yM):
    glColor3f(0.2, 0.6, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xm, ym)
    glVertex2f(xM, ym)
    glVertex2f(xM, yM)
    glVertex2f(xm, yM)
    glEnd()


# -------------------- Main Program --------------------

if not glfw.init():
    sys.exit()

WIDTH, HEIGHT = 800, 600
window = glfw.create_window(WIDTH, HEIGHT, "Liang–Barsky Line Clipping", None, None)
glfw.make_context_current(window)

gluOrtho2D(0, WIDTH, 0, HEIGHT)

# Clipping window
xm, ym = 200, 150
xM, yM = 600, 450

# Original line
line_original = (100, 500, 700, 100)

# Apply Liang–Barsky
visible, clipped_line = clip(*line_original, xm, ym, xM, yM)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    draw_rect(xm, ym, xM, yM)
    draw_line(*line_original, 1.0, 0.0, 0.0)   # Red original line

    if visible:
        draw_line(*clipped_line, 0.0, 1.0, 0.0)  # Green clipped line

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
