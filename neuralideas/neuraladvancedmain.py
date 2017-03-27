import math

import numpy as np

from brain import Brain
from neuron import Neuron
from sensory_cadvanced import SensoryC
from hippocampus_cadvanced import HippocampusC
from motor_cadvanced import MotorC
from executive_cadvanced import ExecutiveC
from amygdala_cadvanced import AmygdalaC

if __name__ == '__main__':
    actthreshold = 0.3
    sensory_c = SensoryC(2)
    hippocampus_c = HippocampusC(3)
    executive_c = ExecutiveC(2)
    amygdala_c = AmygdalaC(2)
    out = Neuron(0, 'outneuron', actthreshold)
    motor_c = MotorC(1, out)
    brain = Brain('network1', sensory_c, motor_c, hippocampus_c, amygdala_c, executive_c, [out])
    brain.birth(10)
