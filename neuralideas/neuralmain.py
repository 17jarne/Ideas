import numpy as np
import math
from neuralsystem import neuralsystem
from neuron import neuron

if __name__ == '__main__':
	print "hello"
	actthreshold = 0.3
	smell1 = neuron(0, 'inputneuron', actthreshold)
	smell2 = neuron(1, 'inputneuron', actthreshold)
	pro1 = neuron(2, 'proneuron', actthreshold)
	pro2 = neuron(3, 'proneuron', actthreshold)
	pro3 = neuron(4, 'proneuron', actthreshold)
	out = neuron(5, 'outneuron', actthreshold)
	
	templist = [pro1, pro2, pro3]
	for neuron in templist:
		smell1.add_outconnects([neuron, 0.4])
		smell2.add_outconnects([neuron, 0.4])
		neuron.add_inconnects([smell1, 0.4])
		neuron.add_inconnects([smell2, 0.4])
		neuron.add_outconnects([out, 0.2])
		out.add_inconnects([neuron, 0.2])
		for neuron2 in templist:
			neuron.add_outconnects([neuron2, 0.3])
			neuron.add_inconnects([neuron2, 0.3])
	templist = [smell1, smell2, pro1, pro2, pro3, out]
	network = neuralsystem('network1', templist)
	network.birth(10)
