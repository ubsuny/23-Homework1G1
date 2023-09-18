**Repository Overview**

We will perform a multiplication operation on the IBM quantum computer, taking a simple example of multiplying two numbers. As it is suggested that for simple athematic operations using quantum computers is not an excellent choice, but we just want to check and learn how things work on a quantum computer. 

**Environmental setup**
We performed a simple matiplication fuunction, using IMB quantum computer plateform.
https://quantum-computing.ibm.com/
**Code Structure**
**The code itself is well structured but I will explain its different parts and how they work.

1. **Importing Libraries**:
   - `import qiskit` and `import numpy as np` are used to import the Qiskit and NumPy libraries, which are necessary for quantum computation and numerical operations.

2. **Function Definition**:
   - `def quantum_multiplication(multiplicand, multiplier):` defines a function named `quantum_multiplication` that takes two arguments: `multiplicand` and `multiplier`.

3. **Binary Length Calculation**:
   - `multiplicandBinLen` and `multiplierBinLen` are calculated to determine the number of bits required to represent the multiplicand and multiplier in binary form.

4. **Quantum Registers and Circuit Initialization**:
   - Quantum registers `q` and classical registers `c` are created with appropriate sizes to hold the binary representations of the numbers and the results.
   - A quantum circuit `circuit` is initialized using these registers.

5. **Encoding of Input Numbers**:
   - The binary representations of the multiplicand and multiplier are encoded onto the quantum registers using X gates based on their binary digits.

6. **Quantum Fourier Transform (QFT) Multiplication**:
   - A QFT multiplication circuit `qft_circuit` is created using the `RGQFTMultiplier` from the Qiskit library. This circuit performs the quantum multiplication.
   - The QFT multiplication circuit is composed with the base circuit `circuit`.

7. **Measurement**:
   - The output qubits (result of multiplication) are measured using the `measure` method. These measurements are stored in the classical registers `c`.

8. **Execution on Quantum Simulator**:
   - The quantum circuit is executed on a quantum simulator (`qasm_simulator`) using Qiskit's `execute` function. The `shots` parameter specifies the number of times the circuit is executed (in this case, 2000 times).
   - The measurement results are obtained from the simulator.
  
   **- Unit test.**
Unit test is performed, with different examples like belove,
         # Test cases with expected results
    test_cases = [
        (100, 100, 10000),  # 100 * 100 = 10000
        (20 ,531, 10620),  # 20 * 531 = 10620
        (77, 45, 3465),  # 77 * 45 = 3465
        (13, 93, 1209),  # 13 * 93 = 1209

# Test cases with negative numbers
    test_cases = [
        (-3, -5, 15),  # -3 * -5 = 15
        (-5, -5, 25),  # -5 * -5 = 25
        (-2, -5, 10),  # -2 * -5 = 10


        # Test cases with mixed numbers
    test_cases = [
        (-3, 5, -15),  # -3 * 5 = -15
        (3, -5, -15),  # 3 * -5 = -15
        (3, -2, -6),  # 3 * -2 = -6
   
In the unittest file, you can find out which numbers work and which don't

**Acknowledgment.** 
I acknowledge all my group members for working on this project. As it was done in a collaborative way. We are also thankful to the other groups who helped from time to time. And also, our instructor for the course, he helps in making it happen. References Most of the help was taken from the IMP quantum computing platform and different AI tool like ChatGPT bard and googlecolab was used for checking the code. 
**References**

https://www.scienceworld.ca/stories/ho-do-quantum-computers-work/?gclid=Cj0KCQjwx5qoBhDyARIsAPbMagDCv1G_AWs_S1r2IZ1MsKoGVUzE1QfXoCBwM9vu_t5am7nMZZTeu64aAkLwEALw_wcB
https://quantum-computing.ibm.com/
https://quantumcomputinguk.org/tutorials/multiplication-on-quantum-computers-with-qiskit

Chatgpt

Bard




**Ahmed Changed This Line**



