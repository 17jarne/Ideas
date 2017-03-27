import math
import numpy as np

actthreshold = 0.5
class hippocampus_c:
        def __init__(self, size):
                #create neurons
                preneurons = [neuron(0, 'proneuron', actthreshold) for i in range(size)]
                i = 0
                for neuron in preneurons:
                        neuron.changename(i)
                        i += 1
                self.neurons = preneurons
                self.size = size
                #connect neurons
                defaultstrength = 0.4
                for neuron1 in neurons:
                        for neuron2 in neurons:
                                if neuron1 is not neuron2:
                                        neuron1.add_inconnects([neuron2, defaultweight])
                                        neuron2.add_outconnects([neuron1, defaultweight])

