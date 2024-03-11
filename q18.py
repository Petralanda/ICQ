import numpy as np

def calc_traco(matriz):
    matriz=np.array(matriz)
    return np.trace(matriz)

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
mat=ler_matriz_complexa(n, m)
resultado =calc_traco(mat)
print("O traço é: ", resultado)