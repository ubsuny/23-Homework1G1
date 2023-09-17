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

  # Adding these variables to clean up a little. First we check to see if only 1
  # number is negative so we know our product needs a negative sign
  sign = 1
  if (multiplicand < 0) != (multiplier < 0):
    sign = -1
  
  #We then set the inputs to their absolute values because negative numbers
  #sometimes will not play nice with these later functions
  multiplier = abs(multiplier)
  multiplicand = abs(multiplicand)
  
  #We need enough qubits to hold both inputs and the output, and the two
  #inputs must be stored in the same number of qubits
  maxBitSize = max(len(bin(multiplier)), len(bin(multiplicand))) - 2
  qRegSize = 4*(maxBitSize)
  cRegSize = 2*(maxBitSize)
  #For these 2, the -2 is because python appends '0b' to the start of all
  #binary representations of numbers
  multiplicandBinLen = len(bin(multiplicand)) - 2
  multiplierBinLen = len(bin(multiplier)) - 2

  # Initialize the registers and quantum circuit.
  q = qiskit.QuantumRegister(qRegSize)
  c = qiskit.ClassicalRegister(cRegSize)
  circuit = qiskit.QuantumCircuit(q, c)

  # Encode the values on to the Operands.
  #Takes the binary representations of the operands and represents them
  #in the given qubits, i.e. 2 = |1>|0>
  for i in range(multiplicandBinLen):
    if int(bin(multiplicand)[len(bin(multiplicand))-1-i]) == 1:
      circuit.x(q[i])

  for i in range(multiplierBinLen):
    #print(int(bin(multiplier)[len(bin(multiplier))-1-i]))
    if int(bin(multiplier)[len(bin(multiplier))-1-i]) == 1:
      circuit.x(q[i + maxBitSize])
    
  # Create the QFT multiplication circuit and add it to our base circuit
  qft_circuit = qiskit.circuit.library.RGQFTMultiplier(num_state_qubits=maxBitSize, num_result_qubits=cRegSize)
  circuit = circuit.compose(qft_circuit)

  # Measure the output qubits.
  circuit.measure(q[(qRegSize-cRegSize):qRegSize],c)

  # Send the circuit to a backend device and get the results back.
  job = qiskit.execute(circuit, backend=qiskit.Aer.get_backend('qasm_simulator'), shots = 2000)
  result = job.result()

  # The product is the binary representation of the measured state.
  # We multiply it by our sign found earlier and return it to base 10
  return sign*int(list(result.get_counts())[0],2)
