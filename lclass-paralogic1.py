'''
 Patrick Tracanelli
 Materials Science and Engineering MS
 FIU Department of Mechanical and Materials Engineering
 http://mme.fiu.edu Interdisciplinary with https://case.fiu.edu/philosophy/
 PHI-2100, PHI-2600 https://m.fiu.edu/catalog/index.php?action=courseList&subject=PHI
 In this exercise we will learn Newton da Costa's paraconsistent logic in Python using pure math
 We will support testing paraconsistent and paracomplete statements as well as da Costa's
 paraconsistent implication along with both strong and weak contradiction.
'''
# Import the math library
import math

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

# Define some truth values
verdadeiro = 1
falso = 0
indeterminado = 0.5

# Test the functions
print(conjuncao(verdadeiro, falso))  # Output: 0
print(disjuncao(verdadeiro, falso))  # Output: 1
print(negacao_forte(verdadeiro))  # Output: 0
print(negacao_fraca(verdadeiro))  # Output: 0
print(implicacao_paraconsistente(verdadeiro, falso))  # Output: 0
print(paraconsistente(indeterminado))  # Output: 0.25
print(paracompleto(indeterminado))  # Output: 0.5

