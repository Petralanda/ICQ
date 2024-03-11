import cmath as cm
import math as m
import matplotlib.pyplot as plt

c = complex(1,1)

plt.figure()


for i in range (1,11):
    xi = (abs(c)**i)*m.cos(cm.phase(c)*i)
    yi = (abs(c)**i)*m.sin(cm.phase(c)*i)
    plt.quiver(0, 0, xi, yi, angles='xy', scale_units='xy', scale=0.5, color='b')


plt.xlim(-abs(c)**12,abs(c)**12)
plt.ylim(-abs(c)**12,abs(c)**12)

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')

plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()