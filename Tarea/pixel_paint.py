
import numpy as np
import glfw
import sys
import json  
from OpenGL.GL import *

import grafica.easy_shaders as es

from Modelo_Grid import *
from Controlador import *

if __name__ == '__main__':
    #ejemplo de llamada: python pixel_paint.py 16 pallete.json boo.png
    #python pixel_paint.py[0] 16[1] pallete.json[2] boo.png[3]
    archivo_json = sys.argv[2]
    nombre_archivo = sys.argv[3]
    W=int(sys.argv[1])              #cantidad columnas canvas
    H=W                             #cantidad filas canvas
    S=32                            #escala celda
    
    if W>16:
        S=24

    width = W*S                     #Ancho pantalla  ##+ barra
    height = H*S                    #alto pantalla

    #Matriz
    imgData = np.zeros((W, H, 4), dtype=np.uint8)          
    
    transparent = None
    pallete = None

    with open(archivo_json) as json_file:
        data = json.load(json_file)

        transparent = data["transparent"]
        pallete = data["pallete"]
        
        assert len(pallete) <= W
        
        #Pintar fondo
        imgData[:, :] = np.array([255*transparent[0], 255*transparent[1], 255*transparent[2], 0], dtype=np.uint8)
        
        #colores JSON
        for index, color in enumerate(pallete):
            #print(f'El color {index} de la paleta es: {color}')
            imgData[W-1,index] = [255*color[0],255*color[1],255*color[2], 255]
            

        imgData.reshape((imgData.shape[0]*imgData.shape[1],4))
    
    #controlador 
    controlador = Controller(S,transparent,imgData,nombre_archivo)

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





