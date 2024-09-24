idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("Você ainda não pode votar.")
elif 16 <= idade < 18 or idade > 70:
    print("Você pode votar, mas o voto é opcional.")
else:
    print("Você pode votar e o voto é obrigatório.")
