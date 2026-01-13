import glfw
from OpenGL.GL import *
import time

WIDTH, HEIGHT = 800, 600

def dda(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x0
    y = y0

    for _ in range(steps + 1):
        yield int(round(x)), int(round(y))
        x += x_inc
        y += y_inc


points_drawn = []   

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5)

    glBegin(GL_POINTS)
    for (x, y) in points_drawn:
        glVertex2i(x, y)
    glEnd()

def main():
    global points_drawn

    if not glfw.init():
        raise RuntimeError("Failed to initialize GLFW")

    window = glfw.create_window(WIDTH, HEIGHT, "DDA Animation", None, None)
    if not window:
        glfw.terminate()
        raise RuntimeError("Failed to create GLFW window")

    glfw.make_context_current(window)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClearColor(0.0, 0.0, 0.0, 1.0)

    dda_gen = dda(100, 100, 700, 400)

    last_time = time.time()

    while not glfw.window_should_close(window):
        glfw.poll_events()

        now = time.time()
        if now - last_time >= 0.005:
            try:
                point = next(dda_gen)
                points_drawn.append(point)
            except StopIteration:
                pass  
            last_time = now

        draw_scene()
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
