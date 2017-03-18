import numpy as np
import math
import sys, ast
from neuron import neuron

class neuralsystemadvanced:
	def __init__(self, name, sensory_c, motor_c, amygdala_c, hippocampus_c, executive_c):
		self.name = name
		self.sensory_c = sensory_c
		self.motor_c = motor_c
		self.amygdala_c = amygdala_c
		self.hippocampus_c = hippocampus_c
		self.executive_c = executive_c
		self.parts = []
		self.parts.append(sensory_c)
		self.parts.append(motor_c) 
		self.parts.append(amygdala_c)
		self.parts.append(hippocampus_c) 
		self.parts.append(executive_c)
		self.neuronstemp = []
		defaultweight = 0.4
		for part in parts:
			self.neuronstemp.append(part.neurons)
		self.neurons = neuronstemp
		#build up connections between the different parts
		for neuron1 in sensory_c.neurons:
			for neuron2 in hippocampus_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
				neuron2.add_outconnects([neuron1, defaultweight])
		for neuron1 in motor_c.neurons:
			for neuron2 in hippocampus_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
			for neuron2 in executive_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
		for neuron1 in amygdala_c.neurons:
			for neuron2 in hippocampus_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
		for neuron1 in hippocampus_c.neurons:
			for neuron2 in motor_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
			for neuron2 in sensory_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
			for neuron2 in amygdala_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
		for neuron1 in executive_c.neurons:
			for neuron2 in motor_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
			for neuron2 in sensor_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
			for neuron2 in amygdala_c.neurons: 
				
