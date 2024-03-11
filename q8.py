import matplotlib.pyplot as plt

z1 = 2 - 1j
z2 = 1 + 1j

plt.figure()
plt.quiver(0, 0, z1.real, z1.imag, angles='xy', scale_units='xy', scale=1, color='b')
plt.quiver(0, 0, z2.real, z2.imag, angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, z2.real+z1.real, z2.imag+z1.imag, angles='xy', scale_units='xy', scale=1, color='y', label ='Vetor soma')
plt.quiver(z2.real, z2.imag, z1.real-z2.real, z1.imag-z2.imag, angles='xy', scale_units='xy', scale=1, color='g', label ='Vetor subtração')


plt.xlim(0, 4)
plt.ylim(-2, 2)

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()