import math

import numpy as np

from neuron import Neuron

actthreshold = 0.5
class SensoryC:
    def __init__(self, size):
        preneurons = []
        defaultweight = 0.3
        #create neurons
        for i in range(size):
            tempneuron = Neuron('sensory' + str(i), 'inputneuron', actthreshold)
            preneurons.append(tempneuron)
        self.neurons = preneurons
        self.size = size
        #connect neurons
        for neuron1 in self.neurons:
            for neuron2 in self.neurons:
                if neuron1 is not neuron2:
                    neuron1.add_inconnects([neuron2, defaultweight])
                    neuron2.add_outconnects([neuron1, defaultweight])

