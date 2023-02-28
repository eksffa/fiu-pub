'''
 Patrick Tracanelli
 Materials Science and Engineering MS
 FIU Department of Mechanical and Materials Engineering
 http://mme.fiu.edu Interdisciplinary with https://case.fiu.edu/philosophy/
 PHI-2100, PHI-2600 https://m.fiu.edu/catalog/index.php?action=courseList&subject=PHI
 In this exercise we will learn Newton da Costa's paraconsistent logic in Python using pure math

 Assert the proposition that a compass is pointing to north with a given confidence level
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

# Define the compass proposition and the confidence level
bussola_apontando_para_norte = True
nivel_de_confianca = 0.8

# Calculate the truth value of the proposition using paraconsistent logic
verdade = paraconsistente(nivel_de_confianca)

# Check if the truth value is greater than or equal to the confidence level
if verdade >= nivel_de_confianca:
    print("A bússola está apontando para o norte com um nível de confiança de", nivel_de_confianca) # Compass points to north with confidence level of nivel_de_confianca
else:
    print("Não podemos afirmar com segurança que a bússola está apontando para o norte") # We can't assert compass is pointing north


