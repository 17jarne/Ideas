import math
import sys, ast

import numpy as np

from neuron import Neuron
from sensory_cadvanced import SensoryC
from hippocampus_cadvanced import HippocampusC
from motor_cadvanced import MotorC
from executive_cadvanced import ExecutiveC
from amygdala_cadvanced import AmygdalaC

class Brain(object):
	def __init__(self, name, sensory_c, motor_c, amygdala_c, hippocampus_c, executive_c, outneurons):
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
                self.outneurons = outneurons
		defaultweight = 0.4
		for part in self.parts:
			self.neuronstemp.extend(part.neurons)
		self.neurons = self.neuronstemp
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
			for neuron2 in sensory_c.neurons:
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
			for neuron2 in amygdala_c.neurons: 
				neuron1.add_inconnects([neuron2, defaultweight])
                                neuron2.add_outconnects([neuron1, defaultweight])
	def birth(self, commandtime):                                            #time between requests for new commands
                commandtemp = commandtime + 1
                while commandtemp > -1:
                        if commandtemp > commandtime:
                                commandtemp = 0
                                print "Is there any new input for me?"
                                command = raw_input('Command: ')
                                if command == 'stop':
                                        return
                                if command == 'input':
                                        print 'What do you show me?'
                                        impression = raw_input().split(',')     #take input as list containing the names of the stimulated (input) neurons
                                        if impression != '':
                                                impression = map(int, impression)
					for neuron in self.neurons:
						if neuron.name in impression:
							neuron.sumincomings(neuron.actthreshold)
                        for neuron in self.neurons:                                             #signal processing
                                neuron.resetsumincomings()                                      #pushes the newincomings to incomings
                        for neuron in self.neurons:
                                neuron.activation()
                        for neuron in self.neurons:
                                neuron.resetweights()
                                print neuron.status
                        output = []
                        for neuron in self.outneurons:
                                if neuron.status == 1:
                                        output.append(neuron.name)
                        print "I created the following output: "
                        print output
                        commandtemp += 1
				
