z1 = input("Digite o primeiro complexo no formato a+bj: ")
z2 = input("Digite o segundo complexo no formato a+bj: ")

c1 = complex(z1)
c2 = complex(z2)

print("|c1*c2|  = |c1|*|c2|\t", abs(c1*c2) == abs(c1)*abs(c2))

print("|c1+c2| <= |c1|+|c2|\t", abs(c1+c2) <= abs(c1)+abs(c2))
