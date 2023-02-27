# Patrick Tracanelli
# Materials Science and Engineering MS
# FIU Department of Mechanical and Materials Engineering
# http://mme.fiu.edu
# -
# Finding the Langarian density on QED as per Feynmann's we shall:
#       L = -(1/4) F^μν F_μν + ψ^† (iγ^μ ∂_μ - m) ψ - e ψ^† γ^μ A_μ ψ
# This is a toy model to estimate L from pure chaotic randomness (doi:10.1063/1.3597793, doi:10.1103/PhysRevApplied.3.054004)

import random # https://pypi.org/project/quantumrandom/ quantumrandom.binary()[N]
from sympy import symbols, Matrix

F_mu_nu, psi_dag, gamma_mu, d_mu, m, e, A_mu = symbols('F_mu_nu psi_dag gamma_mu d_mu m e A_mu')

# L = -(1/4) F^μν F_μν + ψ^† (iγ^μ ∂_μ - m) ψ - e ψ^† γ^μ A_μ ψ
L = - (1/4) * F_mu_nu * F_mu_nu + psi_dag * (1j * gamma_mu * d_mu - m) * psi_dag - e * psi_dag * gamma_mu * A_mu * psi_dag

L = L.subs([(F_mu_nu, Matrix([[2, 3], [4, 5]])), (psi_dag, Matrix([[1, 2], [3, 4]])),
    (gamma_mu, Matrix([[1, 0], [0, -1]])), (d_mu, Matrix([[1, 0], [0, 1]])), (m, 3), (e, 1), (A_mu, Matrix([[1, 0], [0, 1]]))])

def estima_1_sobre_137_0359(n):
    soma = 0
    for i in range(n):
        soma += 1 / random.uniform(1, 137.0359) # quantumrandom.uint16.uniform(1,137.0359)
    return soma / n

# Estimate 1/137.0359 from 10K samples
# Adjust sample ratio before running the toy model for serious,
# as it will will require way more samples, way more Leonidas
estimativa = estima_1_sobre_137_0359(10000)

def calcular_precisao(L, estimativa):
    return abs(L - estimativa) / estimativa

print("L vale: {:.10f}".format(L))

precisao = calcular_precisao(L, estimativa)

print("Estimate val for 1/137.0359: {:.10f}".format(estimativa))
print("Estimate precision for L = 1/137: {:.6f}%".format(precisao * 100))
