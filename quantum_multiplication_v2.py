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
  q = qiskit.QuantumRegister(19)
  c = qiskit.ClassicalRegister(9)
  circuit = qiskit.QuantumCircuit(q, c)

  # Encode the values on to the Operands.
  for i in range(multiplicandBinLen):
    #print(bin(multiplicand)[len(bin(multiplicand))-1-i])
    if int(bin(multiplicand)[len(bin(multiplicand))-1-i]) == 1:
      circuit.x(q[i])
      #print("worming")

  for i in range(multiplierBinLen):
    #print(int(bin(multiplier)[len(bin(multiplier))-1-i]))
    if int(bin(multiplier)[len(bin(multiplier))-1-i]) == 1:
      circuit.x(q[i + 5])
      #print("worming")
    
  # Create the QFT multiplication circuit and add it to our base circuit
  qft_circuit = qiskit.circuit.library.RGQFTMultiplier(num_state_qubits=5, num_result_qubits=9)
  circuit = circuit.compose(qft_circuit)
  # Measure the output qubits.
  circuit.measure(q[10:19],c)

  # Send the circuit to a backend device and get the results back.
  job = qiskit.execute(circuit, backend=qiskit.Aer.get_backend('qasm_simulator'), shots = 2000)
  result = job.result()

  # The product is the binary representation of the measured state.
  product = format(result.get_counts().get('000000000', 0), '04b')

  return int(list(result.get_counts())[0],2)
