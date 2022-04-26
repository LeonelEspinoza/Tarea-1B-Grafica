

import numpy as np
import glfw
import sys
from OpenGL.GL import *

import grafica.easy_shaders as es

from Modelo_Grid import *
from Controlador import *

if __name__ == '__main__':
            
    W=16                #cantidad columnas canvas
    H=16                #cantidad filas canvas
    S=35                #escala celda
    
    width = W*S         #Ancho pantalla  ##+ barra
    height = H*S        #alto pantalla
    transparent = [0.5,0.5,0.5]

    #Matriz
    imgData = np.zeros((W, H, 3), dtype=np.uint8)          
    
    #Pintar fondo
    imgData[:, :] = np.array([255*0.5, 255*0.5, 255*0.5], dtype=np.uint8)
    
    #colores JSON
    imgData[W-1, 0] = [255*1,255*1,255*1]
    imgData[W-1, 1] = [255*1,255*0.8,255*0.8]
    imgData[W-1, 2] = [255*0,255*0,255*0]
    imgData[W-1, 3] = [255*1,255*1,255*1]
    imgData.reshape((imgData.shape[0]*imgData.shape[1],3))
    
    #controlador 
    controlador = Controller(S,transparent,imgData)
    # Initialize glfw
    if not glfw.init():
        sys.exit()

    window = glfw.create_window(width, height, "Pixel_Paint", None, None)
    
    if not window:
        glfw.terminate()
        sys.exit()
    
    glfw.make_context_current(window)

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, controlador.on_key)

    # Connecting callback functions to handle mouse events:
    # - Cursor moving over the window
    # - Mouse buttons input
    glfw.set_cursor_pos_callback(window, controlador.cursor_pos_callback)
    glfw.set_mouse_button_callback(window, controlador.mouse_button_callback)

    # Assembling the shader program (pipeline) with both shaders
    pipeline = es.SimpleTextureShaderProgram()   #Aqui cambie el STSP por STTSP para hacer transformaciones si es necesario (espero que funcione igual solo sumando transformaciones)
    Colorpipeline2 = es.SimpleShaderProgram()

    # Setting up the clear screen color
    glClearColor(0.85, 0.85, 0.85, 1.0)

    Grid = Grid(pipeline,Colorpipeline2,W,H,imgData) #pipeline,Colorpipeline,N,imgData
    controlador.setGrid(Grid)

    while not glfw.window_should_close(window):  # Dibujando --> 1. obtener el input

        glfw.poll_events()       
        #Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)
        
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        Grid.draw()

        glfw.swap_buffers(window)

    glfw.terminate()





