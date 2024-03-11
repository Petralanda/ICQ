import matplotlib.pyplot as plt

c1 = input("Digite o primeiro complexo no formato a+bj: ")
c2 = input("Digite o segundo complexo no formato a+bj: ")

z1 = complex(c1)
z2 = complex(c2)

plt.figure()

plt.quiver(0, 0, z1.real, z1.imag, angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, z1.real*z2.real, z1.imag*z2.real, angles='xy', scale_units='xy', scale=1, color='b', label ='c X r0')
plt.quiver(0, 0, -1 *z1.imag*z2.real,z1.real *z2.imag , angles='xy', scale_units='xy', scale=1, color='g', label ='c X i0')

plt.xlim(-max(z1.real*z2.real,z1.imag*z2.real)-1, max(z1.real*z2.real,z1.imag*z2.real)+1)
plt.ylim(-max(z1.imag*z2.real,z1.real *z2.imag)-1, max(z1.imag*z2.real,z1.real *z2.imag)+1)

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')

plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()