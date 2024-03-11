import numpy as np

def ler_matriz_complexa(x, y):
    matriz = []
    for i in range(x):
        linha = []
        for j in range(y):
            valor_complexo = complex(input(f"Digite o valor para a posição ({i+1},{j+1}): "))
            linha.append(valor_complexo)
        matriz.append(linha)
    return matriz

n=int(input("Numero de linhas da primeira matriz: "))
m=int(input("Numero de colunas da primeira matriz: "))
a=int(input("Numero de linhas da segunda matriz: "))
b=int(input("Numero de colunas da segunda matriz: "))

mat1=ler_matriz_complexa(n, m)
mat2=ler_matriz_complexa(a, b)

resultado = np.kron(mat1,mat2)
print("Resultado do produto tensorial: ")
print(resultado)