import cmath as cm
import math as m
z1 = input("Digite o primeiro complexo no formato a+bj: ")

c1 =complex(z1)
c2 = cm.polar(c1)
print("O numero em coordenadas polares: (", c2[0], ",", m.degrees(c2[1]),")")