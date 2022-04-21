

import numpy as np
import glfw
import sys
from OpenGL.GL import *


from Modelo import *
from Modelo_Grid import *

if __name__ == '__main__':
            
    W=32                #cantidad columnas canvas
    H=32                #cantidad filas canvas
    S=15              #tamaño celda
    
    width = W*S + 80  #Ancho pantalla= canvas + barra
    height = H*S       #alto pantalla
    
    canvasSize = (W*S,H*S)  #Medidas Canvas
    
    #Matriz
    imgData = np.zeros((W, H, 3), dtype=np.uint8)          
    
    #Pintar fondo
    imgData[:, :] = np.array([255*0.5, 255*0.5, 255*0.5], dtype=np.uint8)
    imgData.reshape((imgData.shape[0]*imgData.shape[1],3))

    # Initialize glfw
    if not glfw.init():
        sys.exit()

    window = glfw.create_window(width, height, "Pixel_Paint", None, None)
    
    if not window:
        glfw.terminate()
        sys.exit()
    
    glfw.make_context_current(window)

    # Assembling the shader program (pipeline) with both shaders
    pipeline = es.SimpleTextureShaderProgram()   #Aqui cambie el STSP por STTSP para hacer transformaciones si es necesario (espero que funcione igual solo sumando transformaciones)
    Colorpipeline = es.SimpleTransformShaderProgram()
    Colorpipeline2 = es.SimpleShaderProgram()
    # Telling OpenGL to use our shader program
    glUseProgram(Colorpipeline.shaderProgram)

    # Setting up the clear screen color
    glClearColor(0.85, 0.85, 0.85, 1.0)



    # Our shapes here are always fully painted
#    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    buttons = buttons(Colorpipeline,[1,1,1],[1, 0.8, 0.8],[0,0,0],[1,1,1])
    Grid = Grid(pipeline,Colorpipeline2,W,imgData) #pipeline,Colorpipeline,N,imgData


    while not glfw.window_should_close(window):  # Dibujando --> 1. obtener el input

        glfw.poll_events()       
        #Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        
        #TODO FUNCIONA EXEPTO DIBUJAR buttons y Grid A LA VEZ, SOLO AHI EXPLOTA AAAAAAAAAAAAAAA

        buttons.draw(Colorpipeline)
        #Grid.draw() 

        

        glfw.swap_buffers(window)

    glfw.terminate()





