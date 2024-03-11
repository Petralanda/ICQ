import numpy as np

def ler_matriz_complexa(k):
    mat = []
    for i in range(k):
        linha = []
        for j in range(k):
            valor_complexo = complex(input(f"Digite o valor para a posição ({i+1},{j+1}): "))
            linha.append(valor_complexo)
        mat.append(linha)
    return mat

n=int(input("Digite o valor de n: "))

matriz = ler_matriz_complexa(n)
matriz = np.array(matriz)

inversa = np.linalg.inv(matriz)
dagger=np.conj(matriz).T

dagger =np.array(dagger)
inversa=np.array(inversa)

if (np.array_equal(dagger, inversa)):
    print("Matriz unitaria")

else: print("Matriz nao unitaria")
