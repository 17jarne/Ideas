import math

import numpy as np

from brain import Brain
from neuron import Neuron
from sensory_cadvanced import sensory_c
from hippocampus_cadvanced import hippocampus_c
from motor_cadvanced import motor_c
from executive_cadvanced import executive_c
from amygdala_cadvanced import amygdala_c

if __name__ == '__main__':
    actthreshold = 0.3
    sensory_c = sensory_c(2)
    hippocampus_c = hippocampus_c(3)
    executive_c = executive_c(2)
    amygdala_c = amygdala_c(2)
    motor_c = motor_c(1)
    brain = Brain('network1', sensory_c, motor_c, hippocampus_c, amygdala_c, executive_c)
    brain.birth(10)
