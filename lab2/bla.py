import glfw
from OpenGL.GL import *
import time
WIDTH, HEIGHT = 800, 600

def bla(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    sx = 1 if x1 >= x0 else -1
    sy = 1 if y1 >= y0 else -1
    
    # slope m < 1
    if dy < dx: 
        err = dx // 2
        y = y0
        x = x0
        while x!= x1 +sx:
            yield x, y
            x += sx
            err -= dy 
            if err < 0:
                y +=sy
                err += dx
    else: #slope m >= 1
        err = dy // 2
        x = x0
        y = y0
        while y != y1 + sy:
            yield x, y
            y += sy
            err -= dx
            if err < 0:
                x += sx
                err += dy 
                
                
points_drawn = []

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0,0.0)
    glPointSize(5)
    
    glBegin(GL_POINTS)
    for (x,y) in points_drawn:
        glVertex2i(x,y)
    glEnd()
        
def main():
    global points_drawn
    if not glfw.init():
        raise RuntimeError("failed to initialize glfw")
    
    window= glfw.create_window(WIDTH, HEIGHT,"BLA Animation", None, None)
    if not window:
        glfw.terminate()
        raise RuntimeError("failed to create glfw window")
    
    glfw.make_context_current(window)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WIDTH,0, HEIGHT, -1,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    bla_gen = bla(700, 400, 100, 100)
    last_time = time.time()
    
    while not glfw.window_should_close(window):
        glfw.poll_events()

        now = time.time()
        if now - last_time >= 0.005:
            try:
                point = next(bla_gen)
                points_drawn.append(point)
            except StopIteration:
                pass  
            last_time = now

        draw_scene()
        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
