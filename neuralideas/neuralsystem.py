import numpy as np
import math
import sys, ast

class neuralsystem:
	def __init__(self, name, neurons):
		self.name = name
		self.neurons = neurons
		self.inneurons = []
		self.proneurons = []
		self.outneurons = []
		for neuron in self.neurons:
			if neuron.kind == inneuron:
				self.inneurons.add(neuron)
			if neuron.kind == proneuron:
				self.proneurons.add(neuron)
			if neuron.kind == outneuron:
				self.outneurons.add(neuron)
	def birth(self, commandtime):						 #time between requests for new commands
		commandtemp = 0
		while commandtemp > -1:
			commandtemp += 1
			if commandtemp > time
				commandtemp = 0
				print "Is there any new input for me?"
				command = raw_input('Command: ')
				if command == 'die':
					return
				if command == 'input':
					print 'What do you let experience me?'
					impression = ast.literal.eval( sys.argv[1] )		#take input as list containing the names of the stimulated (input) neurons
					print impression
			for neuron in neurons:							#make everything ready for a new round of signal processing
				neuron.resetstatus()
				neuron.resetsumincomings()
			for neuron in neurons:							#signal processing
				if neuron.name in impression:
					neuron.sumincomings(neuron.actthreshold)
				neuron.activate()
			output = []
			for neuron in outneurons []:
				if neuron.status == 1:
					output.add(neuron.name)
			print "I created the following output: "
			print output
