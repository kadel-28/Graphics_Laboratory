import glfw
from OpenGL.GL import *
import time

WIDTH, HEIGHT = 800, 600

def midpoint_circle (cx, cy, r):
    x = 0
    y = r
    d = 1 - r
    
    while x <= y:
        points = [
            (cx + x, cy + y),
            (cx - x, cy + y),
            (cx + x, cy - y),
            (cx - x, cy - y),
            (cx + y, cy + x),
            (cx - y, cy + x),
            (cx + y, cy - x),
            (cx - y, cy - x)
        ]
        yield points
        
        x += 1
        if d < 0:
            d += 2*x + 1
        else:
            y -=1
            d += 2*(x - y) + 1
            
points_drawn=[]


def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glColor3f(0.0,1.0,1.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    for (x,y) in points_drawn:
        glVertex2i(x,y)
    glEnd()
    
def main():
    global points_drawn
    
    if not glfw.init():
        raise RuntimeError("failed to initialize glfw")
    
    window = glfw.create_window(WIDTH, HEIGHT, "midpoint circle drawing algorithm",None, None)
    if not window:
        glfw.terminate()
        raise RuntimeError("failed to create glfw window")
    
    glfw.make_context_current(window)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
    
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    cx, cy, r = 400, 300, 150 
    
    circle_gen = midpoint_circle(cx, cy, r)
    
    last_time= time.time()
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        
        now = time.time()
        
        if now - last_time >= 0.1:
            try:
                pts = next(circle_gen)
                points_drawn.extend(pts)
            except StopIteration:
                pass
            
            last_time = now
            
        draw_scene()
        glfw.swap_buffers(window)
        
    glfw.terminate()
    
if __name__ == "__main__":
    main()