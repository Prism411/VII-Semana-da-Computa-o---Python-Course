nomes = []
quantidades = []
precos = []

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    quantidade = int(input(f"Digite a quantidade do produto {i+1}: "))
    preco = float(input(f"Digite o preço do produto {i+1}: "))

    # Adicionar os dados nas respectivas listas
    nomes.append(nome)
    quantidades.append(quantidade)
    precos.append(preco)

print("\nProdutos cadastrados:")
for i in range(5):
    print(f"Produto {i+1}: {nomes[i]}, Quantidade: {quantidades[i]}, Preço: R${precos[i]:.2f}")
