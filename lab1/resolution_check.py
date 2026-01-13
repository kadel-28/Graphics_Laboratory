import glfw
from OpenGL.GL import *

def main():
    
    if not glfw.init():
        raise Exception("GLFW cannot be initialized!")

    
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(640, 480, "Hidden", None, None)

    if not window:
        glfw.terminate()
        raise Exception("Window cannot be created!")

    glfw.make_context_current(window)

    
    monitor = glfw.get_primary_monitor()

    
    mode = glfw.get_video_mode(monitor)

    width = mode.size.width
    height = mode.size.height

    print("Your Mac screen resolution:")
    print(f"Width: {width}px")
    print(f"Height: {height}px")

    glfw.terminate()

if __name__ == "__main__":
    main()
    

