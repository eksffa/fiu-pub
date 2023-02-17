# Patrick Tracanelli
# Materials Science and Engineering MS
# FIU Department of Mechanical and Materials Engineering
# http://mme.fiu.edu
# -
# Pra encontrar a densilidade de Langarian no QED do Feynmann temos:
# 			L = -(1/4) F^μν F_μν + ψ^† (iγ^μ ∂_μ - m) ψ - e ψ^† γ^μ A_μ ψ
# Toy model para estimar L a partir do puro caos (doi:10.1063/1.3597793, doi:10.1103/PhysRevApplied.3.054004)

import random # https://pypi.org/project/quantumrandom/ quantumrandom.binary()[N]
from sympy import symbols, Matrix

F_mu_nu, psi_dag, gamma_mu, d_mu, m, e, A_mu = symbols('F_mu_nu psi_dag gamma_mu d_mu m e A_mu')

L = - (1/4) * F_mu_nu * F_mu_nu + psi_dag * (1j * gamma_mu * d_mu - m) * psi_dag - e * psi_dag * gamma_mu * A_mu * psi_dag

# L = -(1/4) F^μν F_μν + ψ^† (iγ^μ ∂_μ - m) ψ - e ψ^† γ^μ A_μ ψ

L = L.subs([(F_mu_nu, Matrix([[2, 3], [4, 5]])), (psi_dag, Matrix([[1, 2], [3, 4]])),
	(gamma_mu, Matrix([[1, 0], [0, -1]])), (d_mu, Matrix([[1, 0], [0, 1]])), (m, 3), (e, 1), (A_mu, Matrix([[1, 0], [0, 1]]))])

def estima_1_sobre_137_0359(n):
    soma = 0
    for i in range(n):
        soma += 1 / random.uniform(1, 137.0359) # quantumrandom.uint16.uniform(1,137.0359)
    return soma / n

# Gerar uma estimativa de 1/137.0359 usando 10K amostras
# No universo de brinquedo vai ser preciso mais que 10K haha, um pouco mais ooo Leonidas
estimativa = estima_1_sobre_137_0359(10000)

def calcular_precisao(L, estimativa):
    return abs(L - estimativa) / estimativa

print("L vale: {:.10f}".format(L))

precisao = calcular_precisao(L, estimativa)

print("Valor estimado de 1/137.0359: {:.10f}".format(estimativa))
print("Precisão da estimativa para L = 1/137: {:.6f}%".format(precisao * 100))




