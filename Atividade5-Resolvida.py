def fatorial_iterativo(n):
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

# Testando a função
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial_iterativo(numero)}")

def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

# Testando a função
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial_recursivo(numero)}")


import math
def fatorial_biblioteca(n):
    return math.factorial(n)

# Testando a função
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial_biblioteca(numero)}")
