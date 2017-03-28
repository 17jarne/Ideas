import math

import numpy as np

from neuron import Neuron

actthreshold = 0.5
class AmygdalaC(object):
    def __init__(self, joysize, painsize):
        defaultweight = 0.3
        preneurons = []
        #create neurons
        for i in range(joysize):
            tempneuron = Neuron('amygdala' + str(i), 'joyneurons', actthreshold)
            preneurons.append(tempneuron)
        self.joyneurons = preneurons
        preneurons = []
        for i in range(painsize):
            tempneuron = Neuron('amygdala' + str(i + joysize), 'painneurons', actthreshold)
            preneurons.append(tempneuron)
        self.painneurons = preneurons
        preneurons = []
        for neuron in self.joyneurons:
            preneurons.append(neuron)
        for neuron in self.painneurons:
            preneurons.append(neuron)
        self.neurons = preneurons
        self.size = joysize + painsize
        self.joysize = joysize
        self.painsize = painsize
        #connect neurons
        for neuron1 in self.neurons:
            for neuron2 in self.neurons:
                if neuron1 is not neuron2:
                    neuron1.add_inconnects([neuron2, defaultweight])
                    neuron2.add_outconnects([neuron1, defaultweight])

