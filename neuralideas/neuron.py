import math
import numpy as np

class neuron:

    	def __init__(self, name, kind, actthreshold):
        	self.name = name
		self.kind = kind							#processing, input, output, joy or pain neuron
		self.actthreshold = actthreshold
        	self.inconnects = []							#one connect: [otherneuron, weight]
		self.outconnects = []	
   	def add_inconnects(self, inconnects):
        	self.inconnects.append(inconnects)
	def add_outconnects(self, outconnects):
                self.outconnects.append(outconnects)
	def resetincomings(self):
		sumincomings = 0
	def sumincommings(self, incoming):						#sums up incoming signals
		sumincomings += incoming
	def setweightin(self, otherneuron, newweight, oldweight):			#sets new weight to inconnect
		self.inconnects.remove([otherneuron, oldweight])
		self.inconnects.add([otherneuron, newweight])
		otherneuron.outconnects.remove([self, oldweight])
		otherneuron.outconnects. add([self, oldweight])
	def setweightin(self, otherneuron, newweight, oldweight):                      
                self.outconnects.remove([otherneuron, oldweight])
                self.outconnects.add([otherneuron, newweight])
                otherneuron.inconnects.remove([self, oldweight])
                otherneuron.inconnects. add([self, oldweight])
	def activation(self):								#manages the processes when neuron gets activated
		if sumincommings > actthreshold:
			for outconnect in self.outconnects:
				outconnect[0].sumincomings(outconnect[1])
			for inconnect in self.inconnects:
				if inconnect[1] > 0:
					self.setweightin(inconnect[0], math.sqrt(inconnect[1]), inconnect[1])

	
