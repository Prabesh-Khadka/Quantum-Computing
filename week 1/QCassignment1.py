#if qiskit is oi 0 state | 0 > which is ket notation

import qiskit as qk
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

#create a quantum circuit with two  quibits and two classical bits

qc = qk.QuantumCircuit(2, 2)

#Apply Handamard gate o both qubbits
qc.h(0)
qc.h(1)

#Measure both quibits
qc.measure(0, 0)
qc.measure(1, 1)

#choose the qasm_simulator backend
simulator =  AerSimulator(methods='statevector')

#simulate the circuit
job = simulator()