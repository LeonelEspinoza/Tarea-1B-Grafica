import grafica.transformations as tr
import grafica.basic_shapes as bs
import grafica.scene_graph as sg
import grafica.easy_shaders as es

import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import sys

# A simple class container to store vertices and indices that define a shape
class Shape:
    def __init__(self, vertices, indices, textureFileName=None):
        self.vertices = vertices
        self.indices = indices
        self.textureFileName = textureFileName

# We will use 32 bits data, so we have 4 bytes
# 1 byte = 8 bits
SIZE_IN_BYTES = 4

# A simple class container to reference a shape on GPU memory
class GPUShape:
    def __init__(self):
        self.vao = 0
        self.vbo = 0
        self.ebo = 0
        self.texture = 0
        self.size = 0

def toGPUShape(shape):
    assert isinstance(shape, Shape)

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

def createGrid(Nx, Ny):

    vertices = []
    indices = []
    index = 0

    # cols
    for x in np.linspace(-1, 1, Nx + 1, True):
        vertices += [x, -1, 0] + [0,0,0]
        vertices += [x,  1, 0] + [0,0,0]
        indices += [index, index+1]
        index += 2

    # rows
    for y in np.linspace(-1, 1, Ny + 1, True):
        vertices += [-1, y, 0] + [0,0,0]
        vertices += [ 1, y, 0] + [0,0,0]
        indices += [index, index+1]
        index += 2

    return Shape(vertices, indices)
