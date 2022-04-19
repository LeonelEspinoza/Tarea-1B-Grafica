import numpy as np
import glfw
import sys
from OpenGL.GL import *



if __name__ == '__main__':

    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = 600
    height = 600

    window = glfw.create_window(width, height, "Pixel_Paint", None, None)
    if not window:
        glfw.terminate()
        sys.exit()
    
    glfw.make_context_current(window)



    while not glfw.window_should_close(window):  # Dibujando --> 1. obtener el input

        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)

        # Using GLFW to check for input events
        glfw.poll_events()  # OBTIENE EL INPUT --> CONTROLADOR --> MODELOS
        
        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)
        
        glfw.swap_buffers(window)

    glfw.terminate()
