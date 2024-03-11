def soma_vetores(matriz_1, matriz_2):

    return matriz_1 + matriz_2

def inverso_vetor(matriz):

    return -matriz

def mult_escalar(matriz, esc):

    return esc * matriz

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
escalar=float(input("Digite o escalar: "))

matriz1 = ler_matriz_complexa(n)
matriz2 = ler_matriz_complexa(n)

print("Resultado da soma: ", soma_vetores(matriz1, matriz2))
print("Resultadodo inverso: ",inverso_vetor(matriz1))
print("Resultado do produto escalar: ", mult_escalar(matriz1, escalar))
