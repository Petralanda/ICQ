import numpy as np

def trans(matriz):

    return np.transpose(matriz)

def conj(matriz):

    return np.conjugate(matriz)

def dagger(matriz):
    return np.conj(matriz).T

def ler_matriz_complexa(n, m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            valor_complexo = complex(input(f"Digite o valor para a posição ({i+1},{j+1}): "))
            linha.append(valor_complexo)
        matriz.append(linha)
    return matriz
