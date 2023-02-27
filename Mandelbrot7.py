# Patrick Tracanelli
# Materials Science and Engineering MS
# FIU Department of Mechanical and Materials Engineering
# http://mme.fiu.edu
# 
# θ=π/2 orthogonal
#
import numpy as np
import matplotlib.pyplot as plt
import quantumrandom

# Define the Mandelbrot function
def mandelbrot(z, max_iters):
    # Define the complex number c as z
    c = z
    # Iterate the function up to max_iters times
    for i in range(max_iters):
        # If the magnitude of z is greater than 2, return the current iteration
        if abs(z) > 2:
            return i
        # Apply the Mandelbrot function to z
        z = z*z + c
    # If the magnitude of z does not exceed 2 after max_iters iterations, return max_iters
    return max_iters

# Set the size of the image
largura = 1000
altura = 1000

# Define the range of the complex plane
faixa_real = (-2.5, 1)
faixa_ortogonal = (-1, 1)

# Create an array to store the Mandelbrot set
conjunto_mandelbrot = np.zeros((altura, largura))

# Generate the Mandelbrot set
for x in range(largura):
    for y in range(altura):
        # Scale x and y coordinates to match the range of the complex plane
        real = faixa_real[0] + (faixa_real[1] - faixa_real[0]) * x / (largura - 1)
        ortogonal = faixa_ortogonal[0] + (faixa_ortogonal[1] - faixa_ortogonal[0]) * y / (altura - 1)

        # Generate a complex number using random quantum bits from the quantumrandom module
        bits = quantumrandom.get_bits(32)
        z = complex(bits[0]/2**31, bits[1]/2**31)

        # Apply the Mandelbrot function to the complex number
        conjunto_mandelbrot[y, x] = mandelbrot(z*complex(real, ortogonal), 100)

# Plot the Mandelbrot set
plt.imshow(conjunto_mandelbrot, cmap='hot', extent=[faixa_real[0], faixa_real[1], faixa_ortogonal[0], faixa_ortogonal[1]])
plt.title('Mandelbrot set') # Conjunto Mandelbrot
plt.xlabel('Real Axis') # Eixo real
plt.ylabel('Orthogonal Axis') # Eixo imaginario mas vou chamar de ortogonal pra nao ser punido por Euler
plt.show()
