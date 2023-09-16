import qiskit
import numpy as np

def quantum_multiplication(multiplicand, multiplier):
  """
  Performs quantum multiplication of two numbers.

  Args:
    multiplicand: The first number to multiply.
    multiplier: The second number to multiply.

  Returns:
    The product of the two numbers.
  """

  # Adding these variables to clean up a little. The -2 is because of how
  # python expresses binary numbers
  multiplicandBinLen = len(bin(multiplicand)) - 2
  multiplierBinLen = len(bin(multiplier)) - 2

  # Initialize the registers and quantum circuit.
  q = qiskit.QuantumRegister(8)
  c = qiskit.ClassicalRegister(8)
  circuit = qiskit.QuantumCircuit(q, c)

  # Encode the values on to the Operands.
  for i in range(multiplicandBinLen):
    print(bin(multiplicand)[len(bin(multiplicand))-1-i])
    if int(bin(multiplicand)[len(bin(multiplicand))-1-i]) == 1:
      circuit.x(q[i])

  for i in range(multiplierBinLen):
    print(int(bin(multiplier)[len(bin(multiplier))-1-i]))
    if int(bin(multiplier)[len(bin(multiplier))-1-i]) == 1:
      circuit.x(q[i + 4])

  # Add an Hadamard gate to each of the input qubits.
  circuit.h(q)

  # Create the QFT multiplication circuit.
  qft_circuit = qiskit.circuit.library.QFT(8)
  
  circuit.compose(qft_circuit)
  # Measure the output qubits.
  circuit.measure(q, c)

  # Send the circuit to a backend device and get the results back.
  job = qiskit.execute(circuit, backend=qiskit.Aer.get_backend('qasm_simulator'))
  result = job.result()

  # The product is the binary representation of the measured state.
  product = format(result.get_counts().get('00000000', 0), '08b')

  return int(product, 2)
