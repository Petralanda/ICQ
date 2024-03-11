import matplotlib.pyplot as plt


c = 1+1j
x=c.real
y=c.imag
plt.figure()


for i in range (1,11):
    
    plt.quiver(0, 0, x + i, y , angles='xy', scale_units='xy', scale=1, color='b')


plt.xlim(0,x+11)
plt.ylim(0,y)

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')

plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()