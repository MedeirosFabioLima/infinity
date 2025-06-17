# ATIVIDADE PRÁTICA

# Atividade 01:
# Comparação de Idades:
# Peça ao usuário duas idades e use operadores de comparação para
# # verificar se a primeira idade é maior, menor ou igual à segunda.

# idade1 = int(input("Digite a primeira idade: "))
# idade2 = int(input("Digite a segunda idade: "))

# if idade1 > idade2:
#     print("A primeira idade é maior que a segunda.")
# elif idade1 < idade2:
#     print("A primeira idade é menor que a segunda.")
# else:
#     print("As duas idades são iguais.")


# Atividade 02:
# Verificar Igualdade de Strings:
# Peça ao usuário duas palavras e use operadores
# de comparação para verificar se elas são iguais.

# palavra1 = input("Digite a primeira palavra: ")
# palavra2 = input("Digite a segunda palavra: ")

# if palavra1 == palavra2:
#     print("As palavras são iguais.")
# else:
#     print("As palavras são diferentes.")


# Atividade 03:
# Verificação de Maioridade e Habilitação:
# Crie um programa que peça a idade do usuário e se ele possui habilitação
# (sim ou não). Use operadores lógicos para verificar se ele é maior de idade
# (>= 18) e possui habilitação.

# idade = int(input("Digite sua idade: "))
# habilitacao = input("Você possui habilitação? (sim ou não): ").strip().lower()

# if idade >= 18 and habilitacao == "sim":
#     print("Você é maior de idade e possui habilitação.")
# else:
#     print("Você **não** atende aos requisitos de maioridade e habilitação.")


# Atividade 04:
# Verificação de Notas Aprovadas:
# Escreva um programa que peça duas notas de um aluno. Use operadores
# lógicos para verificar se as duas notas são maiores ou iguais a 6.

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))

# if nota1 >= 6 and nota2 >= 6:
#     print("O aluno está aprovado!")
# else:
#     print("O aluno não está aprovado.")


# Atividade 05:
# Desconto em Preço:
# Peça ao usuário para inserir o preço de um produto e, em seguida,
# use o operador de atribuição -= para aplicar um desconto de 5%.

# preco = float(input("Digite o preço do produto: "))
# preco -= preco * 0.05  # Aplica 5% de desconto
# print(f"Preço com 5% de desconto: R$ {preco:.2f}")



# Atividade 06:
# Dobro do Valor:
# Solicite ao usuário um número e use o operador de
# atribuição *= para dobrar o valor e exibir o resultado.

# numero = float(input("Digite um número: "))
# numero *= 2 # Dobra o valor
# print(f"O dobro do número é: {numero}")


# Atividade 07:
# Verificação de Caracteres em uma String:
# Crie um programa que peça ao usuário uma frase e um caractere.
# Use o operador de associação in para verificar se o caractere está
# presente na frase.

# frase = input("Digite uma frase: ")
# caractere = input("Digite um caractere: ")

# if caractere in frase:
#     print("O caractere está presente na frase.")
# else:
#     print("O caractere não está presente na frase.")


# Atividade 08:
# Verificação de Palavras em uma Frase:
# Peça ao usuário para inserir uma frase e uma palavra.
# Use in para verificar se a palavra está na frase.

# frase = input("Digite uma frase: ")
# palavra = input("Digite uma palavra: ")

# if palavra in frase:
#     print("A palavra está presente na frase.")
# else:
#     print("A palavra não está presente na frase.")



# Atividade 09:
# Verificar Par ou Ímpar:
# Crie um programa que peça ao usuário um número e use a
# estrutura condicional if para verificar se ele é par ou ímpar.

# numero = int(input("Digite um número: "))

# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")


# Atividade 10:
# Verificar Nota para Aprovado:
# Crie um programa que peça a nota de um aluno e
# use if para verificar se ele foi aprovado (nota >= 6).

nota = float(input("Digite a nota do aluno: "))

if nota >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")


# Atividade 11:
# Verificar Par ou Ímpar e Positivo ou Negativo:
# Escreva um programa que peça um número e use if para verificar
# se ele é par ou ímpar e também se é positivo ou negativo.

# numero = int(input("Digite um número: "))

# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

# if numero >= 0:
#     print("O número é positivo.")
# else:
#     print("O número é negativo.")


# Atividade 12:
# Verificar Classificação de IMC:
# Crie um programa que calcule o Índice de Massa Corporal (IMC)
# e use if para classificar o resultado em "Abaixo do peso", "Pesonormal","Sobrepeso" e "Obesidade".

# peso = float(input("Digite seu peso (kg): "))
# altura = float(input("Digite sua altura (m): "))

# imc = peso / (altura ** 2)

# print(f"Seu IMC é: {imc:.2f}")

# if imc < 18.5:
#     print("Classificação: Abaixo do peso")
# elif imc < 25:
#     print("Classificação: Peso normal")
# elif imc < 30:
#     print("Classificação: Sobrepeso")
# else:
#     print("Classificação: Obesidade")


# Atividade 13:
# Sistema de Login Simples:
# Desenvolva um programa que peça ao usuário um nome de usuário
# e uma senha e use if para verificar se são iguais a "admin" e "1234", respectivamente.

# usuario = input("Digite o nome de usuário: ")
# senha = input("Digite a senha: ")

# if usuario == "admin" and senha == "1234":
#     print("Login bem-sucedido!")
# else:
#     print("Usuário ou senha incorretos.")





# Atividade 14:
# Verificar Status de Taxa de Desconto:
# Crie um programa que peça ao usuário o preço original de um produto e
# a quantidade comprada. Use if para verificar se a quantidade é maior que
# 10 para aplicar um desconto de 10% sobre o total.

# preco_unitario = float(input("Digite o preço unitário do produto: "))
# quantidade = int(input("Digite a quantidade comprada: "))

# total = preco_unitario * quantidade

# if quantidade > 10:
#     total -= total * 0.10  # Aplica 10% de desconto

# print(f"Valor total a pagar: R$ {total:.2f}")
