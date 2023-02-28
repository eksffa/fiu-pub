# Patrick Tracanelli
# Materials Science and Engineering MS
# FIU Department of Mechanical and Materials Engineering
# http://mme.fiu.edu Interdisciplinary with https://case.fiu.edu/philosophy/
# PHI-2100, PHI-2600 https://m.fiu.edu/catalog/index.php?action=courseList&subject=PHI
# Monte Carlo method to find π from random
import quantumrandom as qr
import math

def encontra_pi(n):
    m = 0
    for i in range(n):
        x = qr.randfloat()
        y = qr.randfloat()
        m += (x ** 2 + y ** 2 < 1)
    return 4 * m / n

saida = encontra_pi(1000000) * 7

taxa_confianca = saida / (22/7) # Take rate of trust C[0..1] where 22/7 = π such as a valid approximation for π * 7 = 22 such as C=0.999
diferenca = abs(taxa_confianca - (math.pi * 7))

print("Approximate rate of confident that 22/7: {:.12f}".format(taxa_confianca))
print("Value of pi * 7: {:.12f}".format(math.pi * 7))
print("Diff: {:.12f}".format(diferenca))

'''
Propositional truth can be acurately described with paraconsistent logic

Qt( (π * 7 = 22) ≅ encontra_pi(1000000) = π) →⊥

∴  

Qt→⊥

∴ R = Qt→⊥

With a confidence vector of truth tending to indeterminacy of [0.9962,0.0051]

For R = Relatively True (1)

Such as 

T = (1, 1) Inconsistent
t = (1, 0) True
f = (0, 1) False
⊥ = (0, 0) Incomplete

Therefore (0.9962,0.0051) out of (6.9962-7,14.9949-15) = (t,⊥)
'''
