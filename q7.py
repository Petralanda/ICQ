z1 = input("Digite o primeiro complexo no formato a+bj: ")
z2 = input("Digite o segundo complexo no formato a+bj: ")

c1 = complex(z1)
c2 = complex(z2)

print("conjugate(c1)+conjugate(c2) = conjugate(c1 + c2)\t ", c1.conjugate()+c2.conjugate() == (c1+c2).conjugate())
print("conjugate(c1)*conjugate(c2) = conjugate(c1 * c2)\t ", c1.conjugate()+c2.conjugate() == (c1+c2).conjugate())