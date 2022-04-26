import grafica.basic_shapes as bs


from OpenGL.GL import glClearColor, GL_STATIC_DRAW
from OpenGL.GL import *
import numpy as np

SIZE_IN_BYTES = 4

class GPUShape:
    def __init__(self):
        self.vao = 0
        self.vbo = 0
        self.ebo = 0
        self.texture = 0
        self.size = 0

def toGPUShape(shape):

    vertexData = np.array(shape.vertices, dtype=np.float32)
    indices = np.array(shape.indices, dtype=np.uint32)

    # Here the new shape will be stored
    gpuShape = GPUShape()

    gpuShape.size = len(shape.indices)
    gpuShape.vao = glGenVertexArrays(1)
    gpuShape.vbo = glGenBuffers(1)
    gpuShape.ebo = glGenBuffers(1)

    # Vertex data must be attached to a Vertex Buffer Object (VBO)
    glBindBuffer(GL_ARRAY_BUFFER, gpuShape.vbo)
    glBufferData(GL_ARRAY_BUFFER, len(vertexData) * SIZE_IN_BYTES, vertexData, GL_STATIC_DRAW)

    # Connections among vertices are stored in the Elements Buffer Object (EBO)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, gpuShape.ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(indices) * SIZE_IN_BYTES, indices, GL_STATIC_DRAW)

    return gpuShape

class Grid(object):
    def __init__(self,pipeline,Colorpipeline,W,H,imgData) -> None:
        self.W = W
        self.H = H
        self.gpugrid = toGPUShape(bs.createGrid(W,H))               #CREO UNA GRILLA
        self.gpuShape = toGPUShape(bs.createTextureQuad(1,1))        #CREO UN CUADRADO DE TEXTURA 
        self.imgData = imgData
        self.Colorpipeline = Colorpipeline
        self.pipeline = pipeline
        
        #TEXTURIZO EL CUADRADO
        self.gpuShape.texture = glGenTextures(1)                                     
        glBindTexture(GL_TEXTURE_2D, self.gpuShape.texture)
        # texture wrapping params
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        # texture filtering params
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        internalFormat = GL_RGB
        format = GL_RGB
        glTexImage2D(GL_TEXTURE_2D, 0, internalFormat, W, H, 0, format, GL_UNSIGNED_BYTE, self.imgData)
        #TERMINE DE TEXTURIZAR EL CUADRADO
    
    def change_ImgData(self,x, y, rgb):
        self.imgData[ x , y ] = rgb

        #RETEXTURIZO EL CUADRADO
        self.gpuShape.texture = glGenTextures(1)                                     
        glBindTexture(GL_TEXTURE_2D, self.gpuShape.texture)
        # texture wrapping params
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        # texture filtering params
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        internalFormat = GL_RGB
        format = GL_RGB
        glTexImage2D(GL_TEXTURE_2D, 0, internalFormat, self.W, self.H, 0, format, GL_UNSIGNED_BYTE, self.imgData)
        #TERMINE DE TEXTURIZAR EL CUADRADO


    def draw(self):
        glUseProgram(self.pipeline.shaderProgram)           #usa el simple texture shader program
        self.pipeline.setupVAO(self.gpuShape)
        self.pipeline.drawCall(self.gpuShape)              #dibuja el cuadrado
        
        glUseProgram(self.Colorpipeline.shaderProgram)      #usa el simple shader program
        self.Colorpipeline.setupVAO(self.gpugrid)
        self.Colorpipeline.drawCall(self.gpugrid, GL_LINES)     #dibuja la grilla


