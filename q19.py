import numpy as np

def ler_matriz_complexa(k):
    matriz = []
    for i in range(k):
        linha = []
        for j in range(k):
            valor_complexo = complex(input(f"Digite o valor para a posição ({i+1},{j+1}): "))
            linha.append(valor_complexo)
        matriz.append(linha)
    return matriz

n=int(input("Digite o valor de n: "))

mat = ler_matriz_complexa(n)
matriz1 = np.conjugate(np.transpose(mat))

mat = np.array(mat)
matriz1 = np.array(matriz1)

if (np.array_equal(mat, matriz1)):
    print("Matriz hermitiana")
else:
    print("Matriz nao hermitiana")
