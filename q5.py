z1 = input("Digite o primeiro complexo no formato a+bj: ")
z2 = input("Digite o segundo complexo no formato a+bj: ")
z3 = input("Digite o terceiro complexo no formato a+bj: ")

c1 = complex(z1)
c2 = complex(z2)
c3 = complex(z3)

print("c1 + c2 = c2 + c1\t ", (c1+c2 == c2+c1))
print("c1*c2 = c2*c1\t", (c1*c2 == c2*c1))
print("(c1+c2) + c3 = c1 + (c2+c3)\t", ((c1+c2) + c3 == c1 + (c2+c3)))
print("(c1*c2)*c3 = c1*(c2*c3)\t", ((c1*c2)*c3 == c1*(c2*c3)))
print("cc1*(c2+c3) = (c1*c2)+(c1*c3)\t", (c1*(c2+c3) == (c1*c2)+(c1*c3)))