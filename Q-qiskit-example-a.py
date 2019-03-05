#a try at mixing qiskit directly into pennylane
import pennylane as qml
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import BasicAer

backend_statevector = BasicAer.get_backend('statevector_simulator')
backend = BasicAer.get_backend('qasm_simulator')
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)
qc.x(q[0])
qc.x(q[1])
#qc.ch(q[0],q[1])
#qc.measure(q, c)
job = execute(qc, backend_statevector)
print(job.result().get_statevector(qc))
