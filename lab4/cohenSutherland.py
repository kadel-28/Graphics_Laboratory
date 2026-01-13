import glfw
import sys
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D


# -------------------- Region Codes --------------------

INSIDE = 0
LEFT   = 1
RIGHT  = 2
BOTTOM = 4
TOP    = 8


# -------------------- Cohen–Sutherland Helpers --------------------

def compute_code(x, y, xm, ym, xM, yM):
    code = INSIDE

    if x < xm:
        code |= LEFT
    elif x > xM:
        code |= RIGHT

    if y < ym:
        code |= BOTTOM
    elif y > yM:
        code |= TOP

    return code


def cohen_sutherland_clip(x1, y1, x2, y2, xm, ym, xM, yM):
    c1 = compute_code(x1, y1, xm, ym, xM, yM)
    c2 = compute_code(x2, y2, xm, ym, xM, yM)

    while True:
        # Trivially accept
        if not (c1 | c2):
            return True, (x1, y1, x2, y2)

        # Trivially reject
        if c1 & c2:
            return False, None

        # Choose an endpoint outside
        c_out = c1 if c1 else c2

        if c_out & TOP:
            x = x1 + (x2 - x1) * (yM - y1) / (y2 - y1)
            y = yM

        elif c_out & BOTTOM:
            x = x1 + (x2 - x1) * (ym - y1) / (y2 - y1)
            y = ym

        elif c_out & RIGHT:
            y = y1 + (y2 - y1) * (xM - x1) / (x2 - x1)
            x = xM

        else:  # LEFT
            y = y1 + (y2 - y1) * (xm - x1) / (x2 - x1)
            x = xm

        # Replace the outside point with intersection point
        if c_out == c1:
            x1, y1 = x, y
            c1 = compute_code(x1, y1, xm, ym, xM, yM)
        else:
            x2, y2 = x, y
            c2 = compute_code(x2, y2, xm, ym, xM, yM)


# -------------------- Drawing Functions --------------------

def draw_line(x1, y1, x2, y2, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_rectangle(xm, ym, xM, yM):
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
window = glfw.create_window(
    WIDTH, HEIGHT,
    "Cohen–Sutherland Line Clipping",
    None, None
)

glfw.make_context_current(window)
gluOrtho2D(0, WIDTH, 0, HEIGHT)

# Clipping window
xm, ym = 200, 150
xM, yM = 600, 450

# Original line
original_line = (300, 200, 700, 500)

# Apply Cohen–Sutherland
visible, clipped_line = cohen_sutherland_clip(
    *original_line, xm, ym, xM, yM
)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    draw_rectangle(xm, ym, xM, yM)               # Clipping window
    draw_line(*original_line, 1.0, 0.0, 0.0)     # Original line (red)

    if visible:
        draw_line(*clipped_line, 0.0, 1.0, 0.0)  # Clipped line (green)

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
