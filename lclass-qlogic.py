# Patrick Tracanelli
# Materials Science and Engineering MS
# FIU Department of Mechanical and Materials Engineering
# http://mme.fiu.edu Interdisciplinary with https://case.fiu.edu/philosophy/
# PHI-2100, PHI-2600 https://m.fiu.edu/catalog/index.php?action=courseList&subject=PHI
# In this exercise I will show how qlogic is applied in reality, in the strict sense of phisical reality
from qiskit import QuantumCircuit, Aer, execute
from qcbox import qPhoton as qp

# Create a quantum circuit with one qubit
circuit = QuantumCircuit(1, 1)

# Apply the Hadamard gate to the qubit
# The Hadamard gate creates a superposition of the 0 and 1 states.
circuit.h(0)

# Measure the qubit and store the result in a classical bit
circuit.measure(0, 0)

# Run the circuit on the crystal-mirror box from FIU lab or from a simulator
backend = qp.retrieve_state(lphoton,crystalh)
#backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend)
result = job.result()

# Print the measurement result, expected result like {'0': 504, '1': 520} meaning 50.4% of time the bit collapsed to 0 and 52% it collapsed to 1, yeah I know its more than 100%
print(result.get_counts())

# Create a quantum circuit with two qubits
circuit = QuantumCircuit(2, 2)

# Apply the CNOT gate to the qubits
# The CNOT gate entangles the two qubits in a way that ensures that they will always have the same measurement outcome.
circuit.cx(0, 1)

# Measure the qubits and store the result in classical bits
circuit.measure([0, 1], [0, 1])

# Run the circuit on the crystal-mirror box from FIU lab or from a simulator
backend = qp.retrieve_state(lphoton,crystalh)
#backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend)
result = job.result()

# Print the measurement result, expected output like {'00': 1024}
# Remember the CNOT gate
print(result.get_counts())

'''
Patrick notes:

The output of this program will be a dictionary that shows the
number of times each possible measurement outcome occurred.
In this case, the output will be something like: {'00': 1024}

Quantum gates are the basic building blocks of quantum circuits.
Quantum logic gates can be used to manipulate qubits, which are
the basic units of quantum information. There are many types of
quantum logic gates, some of which include the Pauli-X gate, the
Hadamard gate, the CNOT gate, and the Toffoli gate. In this class
we used the CNOT and the Hadamard gate. Shor Algorith uses mostly 
Pauli-X. The philosophy students are suggested to play with the
reality box and test their assertions from possible reality and
as a final exercise implement Pauli-X and H-gate statements.

In the next class we will learn the final logic with pure math
and you will be able to atest the confidence level of your
assertions. 

Remember I'm not a professor and in this class I do not welcome
philosophers doing philosohy dettached from specialized knowlege
therefore all exercises must use the qasm_simulator or the light
box from the Lab. Thank you.
'''
