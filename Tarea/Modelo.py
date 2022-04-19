import grafica.transformations as tr
import grafica.basic_shapes as bs
import grafica.scene_graph as sg
import grafica.easy_shaders as es

from OpenGL.GL import glClearColor, GL_STATIC_DRAW


def create_gpu(shape, pipeline):
    gpu = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpu)
    gpu.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
    return gpu

class buttons(object):

    def __init__(self,pipeline,Nx,transparent,color1,color2,color3):
        
        gpu_gather = create_gpu(bs.createColorQuad(0.5, 0.5, 0.5), pipeline) 
        #gpu_button_back = create_gpu(bs.createColorQuad(0, 0, 0), pipeline)  
        gpu_button1 = create_gpu(bs.createColorQuad(transparent[0], transparent[1], transparent[2]), pipeline) 
        gpu_button2 = create_gpu(bs.createColorQuad(color1[0], color1[1], color1[2]), pipeline) 
        gpu_button3 = create_gpu(bs.createColorQuad(color2[0], color2[1], color2[2]), pipeline) 
        gpu_button4 = create_gpu(bs.createColorQuad(color3[0], color3[1], color3[2]), pipeline) 
        #gpu_grid = create_gpu(bs.createGrid(Nx,Nx), pipeline)

        gather = sg.SceneGraphNode('gather')
        gather.transform = tr.scale(0.5,2,0.8)
        gather.childs += [gpu_gather]

        #grid = sg.SceneGraphNode('grid')
        #grid.transform = tr.uniformScale(1)
        #grid.childs += [gpu_grid]

        #creamos los botones
        button1 = sg.SceneGraphNode('button1')
        button1.transform = tr.matmul([tr.scale(0.3,0.1,0.2), tr.translate(0,9,0)]) #tr.scale(0.3,0.1,0.2) 
        button1.childs += [gpu_button1]
        
        button2 = sg.SceneGraphNode('button2')
        button2.transform = tr.matmul([tr.scale(0.3,0.1,0.2), tr.translate(0,7.5,0)]) 
        button2.childs += [gpu_button2]
        
        button3 = sg.SceneGraphNode('button3')
        button3.transform = tr.matmul([tr.scale(0.3,0.1,0.2), tr.translate(0,6,0)])
        button3.childs += [gpu_button3]
        
        button4 = sg.SceneGraphNode('button4')
        button4.transform = tr.matmul([tr.scale(0.3,0.1,0.2), tr.translate(0,4.5,0)])
        button4.childs += [gpu_button4]

        #boton 1
        #button_1 = sg.SceneGraphNode('button1')
        #button_1.transform = tr.translate(0,0.9,0)
        #button_1.childs += [button1]

        #boton 2
        #button_2 = sg.SceneGraphNode('button2')
        #button_2.transform = tr.translate(0,0.75,0)
        #button_2.childs += [button2]
        
        #boton 3
        #button_3 = sg.SceneGraphNode('button3')
        #button_3.transform = tr.translate(0,0.6,0)
        #button_3.childs += [button3]

        #boton 4
        #button_4 = sg.SceneGraphNode('button4')
        #button_4.transform = tr.translate(0,0.45,0)
        #button_4.childs += [button4]
        
        # Ensamblamos
        Gather = sg.SceneGraphNode('gather')
        Gather.transform = tr.translate(0.8,0,1)
        Gather.childs += [gather, button1, button2, button3, button4]

        mono = sg.SceneGraphNode('buttons')
        mono.transform = tr.translate(0,0,0)
        mono.childs += [Gather]

        transform_mono = sg.SceneGraphNode('buttonsTR')
        transform_mono.childs += [mono]

        self.model = transform_mono
        #self.model.transform = tr.translate(0.7,0.7,0) 


    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')

    def modifymodel(self):
        self.model.transform = tr.translate(self.x, self.y, 0)
    




