# Patrick Tracanelli
# Materials Science and Engineering MS
# FIU Department of Mechanical and Materials Engineering
# http://mme.fiu.edu
#
# Seres de brinquedo no universo de briquedo
# Sintetizar um Paramecyum a partir da sequencia de 87M
# Paramecium tetraurelia (ASM16542v1) formato FASTA download em https://protists.ensembl.org/Paramecium_tetraurelia/Info/Index

import random
import math

class Element:
    def __init__(self, mass, charge, spin):
        self.mass = mass
        self.charge = charge
        self.spin = spin


'''
# Cola: matematica da treta
Neutron: ψ(x, y, z) = Ae^(-r^2/2σ^2)
Oxygen: Ψ = Ψ(x1, y1, z1, x2, y2, z2, ..., xN, yN, zN)
Hydrogen: Ψ(r, θ, φ) = R(r) * Y(θ, φ)
Carbon: Ψ(x, y, z) = Σc_ij * φ_j(x, y, z)
'''

class Carbon(Element):
    def __init__(self):
        super().__init__(mass=12, charge=6, spin=0.5)

    def wavefunction(self, x, y, z):
        # Wavefunction for a particle of Carbon element
        # (assuming it's a stationary state, for simplicity)
        return math.sqrt(1/3) * (2 * math.cos(math.pi*x) + math.cos(math.pi*y) + math.cos(math.pi*z))

class Hydrogen(Element):
    def __init__(self):
        super().__init__(mass=1, charge=1, spin=0.5)

    def wavefunction(self, x, y, z):
        # Wavefunction for a particle of Hydrogen element
        # (assuming it's a stationary state, for simplicity)
        return (1 / math.sqrt(math.pi)) * math.exp(-math.sqrt(x**2 + y**2 + z**2))

class Oxygen(Element):
    def __init__(self):
        super().__init__(mass=16, charge=8, spin=0.5)

    def wavefunction(self, x, y, z):
        # Wavefunction for a particle of Oxygen element
        # (assuming it's a stationary state, for simplicity)
        return math.sqrt(1/5) * (2 * math.cos(math.pi*x) + 2 * math.cos(math.pi*y) - math.cos(math.pi*z))

class Neutron(Element):
    def __init__(self):
        super().__init__(mass=1.00866491595, charge=0, spin=0.5)

    def wavefunction(self, x, y, z):
        # Wavefunction for a particle of Neutron element
        # (assuming it's a stationary state, for simplicity)
        return (1 / (math.sqrt(2*math.pi) * 0.67)) * math.exp(-0.5*((x**2 + y**2 + z**2)/(0.67**2)))

''' # Teste
carbon = Carbon()
print("Carbon:", carbon.wavefunction(0, 0, 0))
hydrogen = Hydrogen()
print("Hydrogen:", hydrogen.wavefunction(1, 2, 3))

oxygen = Oxygen()
print("Oxygen:", oxygen.wavefunction(0, 0, 0))

neutron = Neutron()
print("Neutron:", neutron.wavefunction(1, 1, 1))
'''

def sintetizar_deoxirribose():
    # Perform enzymatic steps to synthesize deoxyribose
    ribose = [(Carbon(), 5), (Hydrogen(), 10), (Oxygen(), 5)] # Formula bio para C5-H10-O5
    enzimas = [[(Carbon(), 2), (Hydrogen(), 3), (Oxygen(), 2)], [(Oxygen(), 1), (Hydrogen(), 1)], [(Hydrogen(), 1), (Oxygen(), 1)]] # C2H3O2-OH-HO
    # Each enzyme is represented as a list of tuples, indicating the atoms it contains and their number
    for enzima in enzimas:
        for atom, num in enzima:
            for i in range(num):
                ribose.append((atom, 1)) # Add the atoms from the enzyme to the ribose molecule
    return [(Carbon(), 5), (Hydrogen(), 10), (Oxygen(), 4)] + ribose # Return the completed deoxyribose molecule with one less oxygen atom

def sintetizar_adenina():
    # Perform enzymatic steps to synthesize adenine
    precursores = [[(Carbon(), 5), (Hydrogen(), 5), (Neutron(), 1)], [(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 1)]]
    enzimas = [[(Carbon(), 2), (Hydrogen(), 3), (Neutron(), 1), (Oxygen(), 1)], [(Carbon(), 1), (Hydrogen(), 3), (Neutron(), 1)]] # C2H3N1O1-CHN
    # Each enzyme is represented as a list of tuples, indicating the atoms it contains and their number
    for precursor in precursores:
        for enzima in enzimas:
            for atom, num in enzima:
                for i in range(num):
                    precursor.append((atom, 1)) # Add the atoms from the enzyme to the precursor molecule
    return [(Carbon(), 5), (Hydrogen(), 6), (Neutron(), 5)] + precursores # Return the completed adenine molecule

def sintetizar_citosina():
    # Perform enzymatic steps to synthesize cytosine
    precursores = [[(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 1)], [(Carbon(), 4), (Hydrogen(), 4), (Neutron(), 2)]]
    enzimas = [[(Carbon(), 3), (Hydrogen(), 2), (Oxygen(), 1)], [(Carbon(), 2), (Oxygen(), 1), (Hydrogen(), 3), (Neutron(), 1)], [(Carbon(), 3), (Hydrogen(), 3), (Neutron(), 1)]]
    # Each enzyme is represented as a list of tuples, indicating the atoms it contains and their number
    for precursor in precursores:
        for enzima in enzimas:
            for atom, num in enzima:
                for i in range(num):
                    precursor.append((atom, 1)) # Add the atoms from the enzyme to the precursor molecule
    return [(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 3)] + precursores # Return the completed cytosine molecule

def sintetizar_guanina():
    # Perform enzymatic steps to synthesize guanine
    precursores = [[(Carbon(), 5), (Hydrogen(), 5), (Neutron(), 1)], [(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 3)]]
    enzimas =
def sintetizar_guanina():
    # Perform enzymatic steps to synthesize guanine
    precursores = [[(Carbon(), 5), (Hydrogen(), 5), (Neutron(), 1)], [(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 3)]]
    enzimas = [[(Carbon(), 4), (Hydrogen(), 4), (Neutron(), 1)], [(Carbon(), 2), (Hydrogen(), 3), (Neutron(), 3)], [(Carbon(), 2), (Oxygen(), 1), (Hydrogen(), 3), (Neutron(), 1)]]
    # Each enzyme is represented as a list of tuples, indicating the atoms it contains and their number
    for precursor in precursores:
        for enzima in enzimas:
            for atom, num in enzima:
                for i in range(num):
                    precursor.append((atom, 1)) # Add the atoms from the enzyme to the precursor molecule
    return [(Carbon(), 5), (Hydrogen(), 5), (Neutron(), 5)] + precursores # Return the completed guanine molecule

def sintetizar_timina():
    # Perform enzymatic steps to synthesize thymine
    precursores = [[(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 1)], [(Carbon(), 2), (Hydrogen(), 4), (Oxygen(), 2)], [(Carbon(), 2), (Hydrogen(), 3), (Neutron(), 1)]]
    enzimas = [[(Carbon(), 2), (Oxygen(), 1), (Hydrogen(), 3), (Neutron(), 1)], [(Carbon(), 4), (Hydrogen(), 4), (Neutron(), 2)], [(Carbon(), 3), (Hydrogen(), 3), (Oxygen(), 1)]]
    # Each enzyme is represented as a list of tuples, indicating the atoms it contains and their number
    for precursor in precursores:
        for enzima in enzimas:
            for atom, num in enzima:
                for i in range(num):
                    precursor.append((atom, 1)) # Add the atoms from the enzyme to the precursor molecule
    return [(Carbon(), 5), (Hydrogen(), 6), (Neutron(), 2), (Oxygen(), 2)] + precursores # Return the completed thymine molecule

def sintetizar_nucleotideo(base):
    # Perform enzymatic steps to synthesize a nucleotide with the given base
    deoxirribose = sintetizar_deoxirribose()
    if base == 'A':
        base = sintetizar_adenina()
    elif base == 'C':
        base = sintetizar_citosina()
    elif base == 'G':
        base = sintetizar_guanina()
    elif base == 'T':
        base = sintetizar_timina()
    else:
        raise ValueError('Invalid base: must be one of A, C, G, T')
    return [("P", 1), (Oxygen(), 4)] + deoxirribose + base # Return the completed nucleotide molecule

def sintetizar_dna(comprimento):
    # Perform enzymatic steps to synthesize a DNA strand with the given length
    dna = []
    for i in range(comprimento):
        nucleotideo = sintetizar_nucleotideo(random.choice(['A', 'C', 'G', 'T']))
        dna += nucleotideo
   
# Each enzyme is represented as a list of tuples, indicating the atoms it contains and their number
for precursor in precursores:
    for enzima in enzimas:
        for atom, num in enzima:
            for i in range(num):
                precursor.append((atom, 1)) # Add the atoms from the enzyme to the precursor molecule
return [(Carbon(), 5), (Hydrogen(), 5), (Neutron(), 5), (Oxygen(), 1)] + precursores # Return the completed guanine molecule

# This function synthesizes thymine through enzymatic steps
def sintetizar_timina():
    # Define the precursor molecules for the synthesis of thymine
    precursores = [[(Carbon(), 5), (Hydrogen(), 6), (Neutron(), 2)], [(Carbon(), 2), (Hydrogen(), 2), (Oxygen(), 1)]]
    # Define the enzymes that are involved in the synthesis of thymine
    enzimas = [[(Carbon(), 3), (Hydrogen(), 2), (Oxygen(), 1)], [(Carbon(), 2), (Hydrogen(), 3), (Neutron(), 1)], [(Carbon(), 4), (Hydrogen(), 5), (Neutron(), 1)]]
    
    # Loop through each precursor molecule and each enzyme and add the atoms from the enzyme to the precursor
    for precursor in precursores:
        for enzima in enzimas:
            for atom, num in enzima:
                for i in range(num):
                    precursor.append((atom, 1))
    
    # Return the completed thymine molecule
    return [(Carbon(), 5), (Hydrogen(), 6), (Neutron(), 2), (Oxygen(), 2)] + precursores


# This function synthesizes a nucleotide with a given base (A, C, G, or T)
def sintetizar_nucleotideo(base):
    # Synthesize a deoxyribose molecule
    deoxirribose = sintetizar_deoxirribose()
    
    # Synthesize a base molecule based on the given input base
    if base == "A":
        base = sintetizar_adenina()
    elif base == "C":
        base = sintetizar_citosina()
    elif base == "G":
        base = sintetizar_guanina()
    elif base == "T":
        base = sintetizar_timina()
    
    # Combine the deoxyribose and base molecules into a nucleotide
    return deoxirribose + base

'''
def sintetizar_dna(genome):
   # Synthesize a DNA molecule with the given genome sequence
    dna = []
    for base in genome:
        nucleotideo = sintetizar_nucleotideo(base)
        dna += nucleotideo
    return dna
'''
# This function synthesizes a DNA molecule with a given number of nucleotides
def sintetizar_dna(num_nucleotideos):
    dna = []
    for i in range(num_nucleotideos):
        # Randomly choose a base from A, C, G, or T
        base = random.choice(["A", Carbon(), "G", "T"])
        # Synthesize a nucleotide with the chosen base
        nucleotideo = sintetizar_nucleotideo(base)
        # Add the nucleotide to the DNA molecule
        dna += nucleotideo
    # Return the completed DNA molecule
    return dna

# Read the genome sequence from a file FASTA formato
# Or download it from https://ftp.ensemblgenomes.ebi.ac.uk/pub/protists/release-56/fasta/paramecium_tetraurelia
with open("/usr/home/eksffa/phraphread/seq/3/paramecyumSequence.phrap") as file:
    genome = file.read().strip()

# Synthesize the DNA from the genome sequence
dna = sintetizar_dna(genome)

# Output the synthesized DNA
print(dna)







