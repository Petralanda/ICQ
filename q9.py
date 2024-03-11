import cmath

def coordenadas_polares(z):
    rho = abs(z)
    theta = (cmath.phase(z) / cmath.pi) * 180
    return rho, theta

z1 = 2 - 1j
z2 = 1 + 1j

soma1 = coordenadas_polares(z1 + z2)
soma2 = coordenadas_polares(z1 - z2)

print("a) A representação em coordenadas polares (rho,theta) é ({:.2f},{:.2f})".format(*soma1))
print("b) A representação em coordenadas polares (rho,theta) é ({:.2f},{:.2f})".format(*soma2))
