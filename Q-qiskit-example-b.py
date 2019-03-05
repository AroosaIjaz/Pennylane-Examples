import pennylane as qml
from pennylane import numpy as np
import pennylane_qiskit



dev1 = qml.device('qiskit.aer', wires=3)

@qml.qnode(dev1)
def circuit1(p1, p2):

	pennylane_qiskit.U3(p1[0],p1[1],p1[2], wires =1)
	pennylane_qiskit.U3(p2[0],p2[1],p2[2], wires =2)
	return qml.expval.PauliZ(0), qml.expval.PauliZ(1), qml.expval.PauliZ(2) 

t1=np.array([0, np.pi, 0])
t2=np.array([0,np.pi ,0])
print(circuit1(t1,t2))