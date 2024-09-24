# Solicitar o tamanho da matriz
N = int(input("Digite o tamanho N da matriz NxN: "))

# Inicializar a matriz
matriz = []

# Solicitar os elementos da matriz ao usuário
for i in range(N):
    linha = []
    for j in range(N):
        valor = int(input(f"Digite o valor da posição [{i+1},{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)
# Imprimir a Diagonal Principal
print("\nDiagonal Principal:")
for i in range(N):
    print(matriz[i][i])

# Imprimir a Diagonal Secundária
print("\nDiagonal Secundária:")
for i in range(N):
    print(matriz[i][N-i-1])
