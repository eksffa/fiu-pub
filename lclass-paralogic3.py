'''
 Patrick Tracanelli
 Materials Science and Engineering MS
 FIU Department of Mechanical and Materials Engineering
 http://mme.fiu.edu Interdisciplinary with https://case.fiu.edu/philosophy/
 PHI-2100, PHI-2600 https://m.fiu.edu/catalog/index.php?action=courseList&subject=PHI
 In this exercise we will learn Newton da Costa's paraconsistent logic in Python using pure math

 Assert the proposition that the spin of a particle is "up" with a given confidence level
'''
# Import the necessary libraries
import math
import scipy.constants as const

# Define a function to calculate the conjunction of two truth values
def conjuncao(a, b):
    # Use the minimum function to implement the conjunction
    return min(a, b)

# Define a function to calculate the disjunction of two truth values
def disjuncao(a, b):
    # Use the maximum function to implement the disjunction
    return max(a, b)

# Define a function to calculate the strong negation of a truth value
def negacao_forte(a):
    # Use the absolute value function to implement the strong negation
    return abs(1 - a)

# Define a function to calculate the weak negation of a truth value
def negacao_fraca(a):
    # Use the complement function to implement the weak negation
    return 1 - a

# Define a function to calculate the paraconsistent implication of two truth values
def implicacao_paraconsistente(a, b):
    # Use the Newton da Costa's paraconsistent implication formula
    return disjuncao(negacao_forte(a), b)

# Define a function to calculate the truth value of a paraconsistent statement
def paraconsistente(a):
    # Use the paraconsistent truth value formula
    return (a + negacao_forte(a)) / 2

# Define a function to calculate the truth value of a paracomplete statement
def paracompleto(a):
    # Use the paracomplete truth value formula
    return max(negacao_fraca(a), a)

# Define the assertion that the particle's spin is "up" and the confidence level
spin_up = True
confidence_level = 0.9

# Use the physics library to extract consistent values for the particle's spin
spin = const.physical_constants["proton gyromag. ratio over 2 pi"][0]

# Check if the spin is positive and the assertion is true
if spin > 0 and spin_up:
    # Calculate the truth value of the proposition using paraconsistent logic
    verdade = paraconsistente(confidence_level)
    # Check if the truth value is greater than or equal to the confidence level
    if verdade >= confidence_level:
        print("The particle's spin is up with a confidence level of", confidence_level)
    else:
        print("Cannot assert with certainty that the particle's spin is up")
else:
    print("The particle's spin is not up")

'''
Patrick notes:

We define the confidence level as confidence_level with a value of 0.9 to represent
the degree of confidence that the assertion is true. use the physical_constants function
from the scipy.constants library to extract the consistent value of the particle's spin
after that we shall check if the spin is positive and the assertion is true. When both
conditions are met, we calculate the truth value of the proposition using the
paraconsistente function based on the given confidence level.

Students shall update this code to grasp data from reality, the photon box and
use the electromagnetic field data value instead of simplified polarization H/V

Remember I'm not a professor and in this class I do not welcome
philosophers doing philosohy dettached from specialized knowlege
therefore all exercises must use the qasm_simulator or the light
box from the Lab. Thank you.

Some help since the library is made by us at MME and documentation only exists in
the package. You should see qlogic.py as a reference, you shall import:

from qcbox import qPhoton

get_qedField(,,,,,,)
get_qedField({lphoton;hphoton;vphoton},{crystalh;crystalH;crystalPauliX;crystalCNOT},{entangle2;colapse2},0..1,0..1)

qp.get_qedField(lphoton,crystalh,,0.5,0.2) will return only light photons with quantum electromagnetic field values
ranging 0.5 or greather that it's spinning up, 0.2 or greather it's spinning right, those values are estimated
from the laser-crystal-mirror apparatus and you shall measure to correctly assert it. Hadamard gate is the second
paramter, shall be fine for this exercise but students are welcome to try other gates. At FIU's MME we can only
entanble or colapse from two laser beans therefore {entangle2;colapse2} express the hope for more complex 
entanglements and collapses in the furture but right now the student shall work with what it can.

Finally remember lads:

It is most likely that among all propositions, from the simplest ones
(am I hungry? I am sleepy! It's dark in here!) to the most complex ones
(the cat is dead in the box, the spin is spinning up), they are better
expressed in paraconsistent logic. Including this proposition.
'''

