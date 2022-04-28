
from Modelo_Grid import Grid

import PIL
from PIL import ImageOps
import glfw 
import sys
from OpenGL.GL import *
import numpy as np

class Controller(object):

    def __init__(self, S, paint, ImgData,nombre_archivo):
       self.leftClickOn = False     #está apretado el click izq
       self.rightClickOn = False    #está apretado el click der
       self.mousePos = (0.0 , 0.0)  #posicion del mouse 
       self.imgData = ImgData
       self.paint = self.imgData[0,0]           #pintura en pincel
       self.S = S
       self.nombre_archivo = nombre_archivo

    def setGrid(self,grid):
        self.grid = grid


    
    def on_key(self, window, key, scancode, action, mods):
        if not (action == glfw.PRESS or action == glfw.RELEASE):
            return
        
        if key == glfw.KEY_ESCAPE:
            glfw.set_window_should_close(window, True)

        if key == glfw.KEY_S or key == glfw.KEY_G:
            im= PIL.Image.fromarray(self.imgData)
            im= im.rotate(-90)
            im= PIL.ImageOps.mirror(im)
            im.save(self.nombre_archivo)
        
        else:
            print ('Unknown key')

    
    def cursor_pos_callback(self, window, x, y):
        self.mousePos = (x,y)

    def mouse_button_callback(self, window, button, action, mods):

        """
        glfw.MOUSE_BUTTON_1: right click
        glfw.MOUSE_BUTTON_2: left click
        glfw.MOUSE_BUTTON_3: scroll click
        """

        if (action == glfw.PRESS or action == glfw.REPEAT):
            if (button == glfw.MOUSE_BUTTON_2):
                self.leftClickOn = True
                self.paint = self.imgData[ int(glfw.get_cursor_pos(window)[0]/self.S) , int(glfw.get_cursor_pos(window)[1]/self.S) ]
                #print("Mouse click - button 2", glfw.get_cursor_pos(window)[0])
                

            elif (button == glfw.MOUSE_BUTTON_1):
                self.rightClickOn = True
                self.grid.change_ImgData( int(glfw.get_cursor_pos(window)[0]/self.S) , int(glfw.get_cursor_pos(window)[1]/self.S) , self.paint )
                #print("Mouse click - button 1:", glfw.get_cursor_pos(window)[1])


        elif (action ==glfw.RELEASE):
            if (button == glfw.MOUSE_BUTTON_1):
                self.leftClickOn = False

            elif (button == glfw.MOUSE_BUTTON_2):
                self.rightClickOn = False
