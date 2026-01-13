import glfw
import sys
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D


# -------------------- Sutherland–Hodgman Helpers --------------------

def inside(point, edge, bounds):
    x, y = point
    xm, ym, xM, yM = bounds

    if edge == 'left':
        return x >= xm
    if edge == 'right':
        return x <= xM
    if edge == 'bottom':
        return y >= ym
    if edge == 'top':
        return y <= yM


def intersect(p1, p2, edge, bounds):
    x1, y1 = p1
    x2, y2 = p2
    xm, ym, xM, yM = bounds

    if edge == 'left':
        x = xm
        y = y1 + (y2 - y1) * (xm - x1) / (x2 - x1)

    elif edge == 'right':
        x = xM
        y = y1 + (y2 - y1) * (xM - x1) / (x2 - x1)

    elif edge == 'bottom':
        y = ym
        x = x1 + (x2 - x1) * (ym - y1) / (y2 - y1)

    elif edge == 'top':
        y = yM
        x = x1 + (x2 - x1) * (yM - y1) / (y2 - y1)

    return (x, y)


def clip_polygon(polygon, bounds):
    for edge in ['left', 'right', 'bottom', 'top']:
        output = []
        s = polygon[-1]  # Previous vertex

        for e in polygon:  # Current vertex
            if inside(e, edge, bounds):
                if not inside(s, edge, bounds):
                    output.append(intersect(s, e, edge, bounds))
                output.append(e)

            elif inside(s, edge, bounds):
                output.append(intersect(s, e, edge, bounds))

            s = e

        polygon = output

    return polygon


# -------------------- Drawing Functions --------------------

def draw_polygon(polygon, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_LINE_LOOP)
    for x, y in polygon:
        glVertex2f(x, y)
    glEnd()


def draw_rectangle(xm, ym, xM, yM):
    glColor3f(0.8, 0.8, 0.2)  # Yellow clipping window
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
    "Sutherland–Hodgman Polygon Clipping",
    None, None
)

glfw.make_context_current(window)
gluOrtho2D(0, WIDTH, 0, HEIGHT)

# Clipping window bounds
xm, ym = 200, 150
xM, yM = 600, 450
bounds = (xm, ym, xM, yM)

# Polygon (partially inside)
polygon = [
    (150, 500),
    (650, 500),
    (550, 300),
    (250, 200),
    (100, 50)
]

# Apply Sutherland–Hodgman
clipped_polygon = clip_polygon(polygon, bounds)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)

    draw_rectangle(xm, ym, xM, yM)          # Clipping window
    draw_polygon(polygon, 1.0, 0.0, 0.0)    # Original polygon (red)

    if clipped_polygon:
        draw_polygon(clipped_polygon, 0.0, 1.0, 0.0)  # Clipped polygon (green)

    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
