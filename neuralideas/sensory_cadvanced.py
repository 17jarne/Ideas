import math
import numpy as np
from neuron import neuron

actthreshold = 0.5
class sensory_c:
	def __init__(self, size):
		smell1 = neuron(0, 'inputneuron', actthreshold)
		#create neurons
		for i in range(size):
			tempneuron = neuron(0, 'inputneuron', actthreshold)
			preneurons.append(tempneuron)
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

