""" Qubit Optimization for 3 qubit ising model in qml default qubit ecosystem. 

we will be comparing pennylane gradient descent optimizer and tensorflow optimizer

for this quantum system"""

import tensorflow as tf
import tensorflow.contrib.eager as tfe
tf.enable_eager_execution()
print(tf.executing_eagerly())

import pennylane as qml
from pennylane import numpy as np
"""making a device with pennylane dafault qubit command"""

dev2 = qml.device('default.qubit', wires=3)
@qml.qnode(dev2, interface='tfe')
def circuit2(p1, p2):
        """lets say first spin is always up (+1 eigenstate of pauli-z operator)
        then we can optimize the rotation angles for the other two spins
        so that the energy in minimized for the given couplings"""

        """WE USE THE GENERAL rot(phi,theta,omega,wires) single qubit operation"""

        qml.Rot(p1[0],p1[1],p1[2], wires =1)
        qml.Rot(p2[0],p2[1],p2[2], wires =2)
        return qml.expval.PauliZ(0), qml.expval.PauliZ(1), qml.expval.PauliZ(2) 


t1=tf.Variable([0, np.pi, 0])
t2=tf.Variable([0, np.pi,0])
"""var_init=tfe.Variable([t1,t2])"""
res=circuit2(t1,t2)
res.shape
