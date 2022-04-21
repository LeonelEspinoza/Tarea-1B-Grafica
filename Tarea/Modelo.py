import grafica.transformations as tr
import grafica.basic_shapes as bs
import grafica.scene_graph as sg
import grafica.easy_shaders as es

from OpenGL.GL import glClearColor, GL_STATIC_DRAW


SIZE_IN_BYTES = 4

def create_gpu(shape, pipeline):
    gpu = es.GPUShape().initBuffers()
    pipeline.setupVAO(gpu)
    gpu.fillBuffers(shape.vertices, shape.indices, GL_STATIC_DRAW)
    return gpu

class buttons(object):

    def __init__(self,pipeline,transparent,color1,color2,color3):
        
        gpu_gather = create_gpu(bs.createColorQuad(0.5, 0.5, 0.5), pipeline) 
        #gpu_button_back = create_gpu(bs.createColorQuad(0, 0, 0), pipeline)  
        gpu_button1 = create_gpu(bs.createColorQuad(transparent[0], transparent[1], transparent[2]), pipeline) 
        gpu_button2 = create_gpu(bs.createColorQuad(color1[0], color1[1], color1[2]), pipeline) 
        gpu_button3 = create_gpu(bs.createColorQuad(color2[0], color2[1], color2[2]), pipeline) 
        gpu_button4 = create_gpu(bs.createColorQuad(color3[0], color3[1], color3[2]), pipeline) 


        gather = sg.SceneGraphNode('gather')
        gather.transform = tr.scale(0.5,2,0)
        gather.childs += [gpu_gather]



        #creamos los botones
        button1 = sg.SceneGraphNode('button1')
        button1.transform = tr.matmul([tr.scale(0.3,0.1,0), tr.translate(0,9,0)])
        button1.childs += [gpu_button1]
        
        button2 = sg.SceneGraphNode('button2')
        button2.transform = tr.matmul([tr.scale(0.3,0.1,0), tr.translate(0,7.5,0)]) 
        button2.childs += [gpu_button2]
        
        button3 = sg.SceneGraphNode('button3')
        button3.transform = tr.matmul([tr.scale(0.3,0.1,0), tr.translate(0,6,0)])
        button3.childs += [gpu_button3]
        
        button4 = sg.SceneGraphNode('button4')
        button4.transform = tr.matmul([tr.scale(0.3,0.1,0), tr.translate(0,4.5,0)])
        button4.childs += [gpu_button4]

        #creamos el Gather grande
        Gather = sg.SceneGraphNode('gather')
        Gather.transform = tr.translate(0.8,0,0)
        Gather.childs += [gather, button1, button2, button3, button4]

        #El que los contiene todos juntos
        mono = sg.SceneGraphNode('buttons')
        mono.childs += [Gather]
        self.model = mono

#        #para transformarlos todos juntos
#        transform_mono = sg.SceneGraphNode('buttonsTR')
#        transform_mono.childs += [mono]

    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, 'transform')

