import math
import numpy as np

const = 0.8
class Neuron(object):
    def __init__(self, name, kind, actthreshold):
        self.name = name
        self.kind = kind							#processing, input, output, joy or pain neuron
        self.actthreshold = actthreshold
        self.inconnects = []							#one connect: [otherneuron, weight]
        self.newinconnects = []
        self.outconnects = []
        self.newoutconnects = []
        self.newsumincomings = 0
        self.oldsumincomings = 0
        self.status = 0								#status 0: not activated, status 1: activated
        self.oldstatus = 0

    def __eq__(self, otherneuron):
        if self.name == otherneuron.name and self.kind == otherneuron.kind and self.actthreshold == otherneuron.actthreshold and self.inconnects == otherneuron.inconnects and self.outconnects == otherneuron.outconnects: return true
        else: return false

    def changename(self, name):
        self.name = name

    def add_inconnects(self, inconnects):
        self.inconnects.append(inconnects)

    def add_outconnects(self, outconnects):
        self.outconnects.append(outconnects)

    def resetsumincomings(self):
        self.oldsumincomings = self.oldsumincomings *const + self.newsumincomings
        self.newsumincomings = 0

    def resetstatus(self):
        self.oldstatus = self.status
        self.status = 0

    def resetweights(self):
        self.inconnects = self.newinconnects
        self.outconnects = self.newoutconnects
        self.newinconnects = []
        self.newoutconnects = []

    def sumincomings(self, incoming):						#sums up incoming signals
        self.newsumincomings += incoming

    def setweightin(self, otherneuron, newweight, oldweight):			#sets new weight to inconnect
        self.newinconnects.append([otherneuron, newweight])
        otherneuron.newoutconnects.append([self, oldweight])

    def setweightout(self, otherneuron, newweight, oldweight):                      
        self.newoutconnects.append([otherneuron, newweight])
        otherneuron.newinconnects.append([self, oldweight])

    def activation(self, situimportance):								#manages the processes when neuron gets ac                                                                                                         tivated
        if self.oldsumincomings >= self.actthreshold:
            self.status = 1
            for outconnect in self.outconnects:
                outconnect[0].sumincomings(outconnect[1])
            for inconnect in self.inconnects:
                if inconnect[1] > 0 and inconnect[0].oldstatus == 1:
                    self.setweightin(inconnect[0], math.pow(inconnect[1], math.pow(1/2, situimportance)), inconnect[1])		#strengthen connection if it had effect
                else:
                    self.setweightin(inconnect[0], inconnect[1], inconnect[1])
                #if inconnect[1] < 0:									#weaken it otherwise
                #	self.setweightin(inconnect[0], math.pow(inconnect[1],2), inconnect[1])
        if self.oldsumincomings < self.actthreshold:
            self.status = 0
            for inconnect in self.inconnects:						#really bad running time
                self.setweightin(inconnect[0], inconnect[1], inconnect[1])
               # for inconnect in self.inconnects:
                #        if inconnect[1] < 0:
                 #               self.setweightin(inconnect[0], math.sqrt(inconnect[1]), inconnect[1])		#as above
                  #      if inconnect[1] > 0:
                   #             self.setweightin(inconnect[0], math.pow(inconnect[1],2), inconnect[1])
