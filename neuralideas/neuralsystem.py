import numpy as np
import math
import sys, ast
from neuron import neuron

class neuralsystem:
	def __init__(self, name, neurons):
		self.name = name
		self.neurons = neurons
		self.inneurons = []
		self.proneurons = []
		self.outneurons = []
		for neuron in self.neurons:
			if neuron.kind == 'inputneuron':
				self.inneurons.append(neuron)
			if neuron.kind == 'proneuron':
				self.proneurons.append(neuron)
			if neuron.kind == 'outneuron':
				self.outneurons.append(neuron)
	def birth(self, commandtime):						 #time between requests for new commands
		commandtemp = commandtime + 1
		while commandtemp > -1:
			if commandtemp > commandtime:
				commandtemp = 0
				print "Is there any new input for me?"
				command = raw_input('Command: ')
				if command == 'die':
					return
				if command == 'input':
					print 'What do you let experience me?'
					impression = raw_input().split(',')	#take input as list containing the names of the stimulated (input) neurons
					print impression
			for neuron in self.neurons:							#make everything ready for a new round of signal processing
				neuron.resetstatus()
				neuron.resetsumincomings()
				neuron.resetweights()
			for neuron in self.neurons:							#signal processing
				if neuron.name in impression:
					neuron.sumincomings(neuron.actthreshold)
				neuron.activation()
			output = []
			for neuron in self.outneurons:
				if neuron.status == 1:
					output.add(neuron.name)
			print "I created the following output: "
			print output
			commandtemp += 1
