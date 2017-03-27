import math
import numpy as np

actthreshold = 0.5
class motor_c:
        def __init__(self, size, outputneuron):
                #create neurons
                preneurons = [neuron(0, 'preoutputneuron', actthreshold) for i in range(size)]
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
		#connect with outputneurons in the right way
		for neuron in neurons:
			 neuron.add_inconnects([outputneuron, defaultweight])
                         outputneuron.add_outconnects([neuron, defaultweight])

