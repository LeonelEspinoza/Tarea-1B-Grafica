

import numpy as np
import glfw
import sys
from OpenGL.GL import *
import imgui

from Modelo import *



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

    # Assembling the shader program (pipeline) with both shaders
    pipeline = es.SimpleTransformShaderProgram()

    # Telling OpenGL to use our shader program
    glUseProgram(pipeline.shaderProgram)

    # Setting up the clear screen color
    glClearColor(0.85, 0.85, 0.85, 1.0)

    # Our shapes here are always fully painted
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    buttons = buttons(pipeline,4,[1,1,1],[1, 0.8, 0.8],[0,0,0],[1,1,1])
    
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glfw.swap_buffers(window)

        # Using GLFW to check for input events
    glfw.poll_events()  # OBTIENE EL INPUT --> CONTROLADOR --> MODELOS
        
        # Clearing the screen in both, color and depth
    glClear(GL_COLOR_BUFFER_BIT)
        
    buttons.draw(pipeline)
    glfw.swap_buffers(window)

    

    while not glfw.window_should_close(window):  # Dibujando --> 1. obtener el input

        glfw.poll_events()
#        glClear(GL_COLOR_BUFFER_BIT)
#        glfw.swap_buffers(window)

        # Using GLFW to check for input events
        glfw.poll_events()  # OBTIENE EL INPUT --> CONTROLADOR --> MODELOS
        
        # Clearing the screen in both, color and depth
#        glClear(GL_COLOR_BUFFER_BIT)
#        
#        buttons.draw(pipeline)
#        glfw.swap_buffers(window)#

    glfw.terminate()




#---------------------------------------------------------------------------

#def createGrid(Nx, Ny):
#
#    vertices = []
#    indices = []
#    index = 0
#
#    # cols
#    for x in np.linspace(-1, 1, Nx + 1, True):
#        vertices += [x, -1, 0] + [0,0,0]
#        vertices += [x,  1, 0] + [0,0,0]
#        indices += [index, index+1]
#        index += 2
#
#    # rows
#    for y in np.linspace(-1, 1, Ny + 1, True):
#        vertices += [-1, y, 0] + [0,0,0]
#        vertices += [ 1, y, 0] + [0,0,0]
#        indices += [index, index+1]
#        index += 2
#
#    return Shape(vertices, indices)

#---------------------------------------------------------------------------

    

    
