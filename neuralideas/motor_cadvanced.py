import math

import numpy as np

from neuron import Neuron

actthreshold = 0.5
class MotorC:
    def __init__(self, size, outputneuron):
        preneurons = []
        defaultweight = 0.3
        #create neurons
        for i in range(size):
            tempneuron = Neuron('motor' + str(i), 'proneurons', actthreshold)
            preneurons.append(tempneuron)
        self.neurons = preneurons
        self.size = size
        #connect neurons
        for neuron1 in self.neurons:
            for neuron2 in self.neurons:
                if neuron1 is not neuron2:
                    neuron1.add_inconnects([neuron2, defaultweight])
                    neuron2.add_outconnects([neuron1, defaultweight])

        #connect with outputneurons in the right way
        for neuron in self.neurons:
            neuron.add_inconnects([outputneuron, defaultweight])
            outputneuron.add_outconnects([neuron, defaultweight])

