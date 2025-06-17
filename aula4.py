
# # ATIVIDADE PRÁTICA



# # Atividade 01:
# # Tabuada de um Número:
# # Faça um programa que solicite um número ao usuário e use
# # um laço for para exibir a tabuada desse número (de 1 a 10).
    
    # Solicita um número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Laço for para exibir a tabuada de 1 a 10
print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


     Exemplo simples:
python
Copiar
Editar
for i in range(1, 6):
    print(i)
O que acontece aqui?
O range(1, 6) gera a sequência: 1, 2, 3, 4, 5

A variável i vai assumindo cada um desses valores, um por um.

O print(i) é executado 5 vezes, mostrando:

1
2
3
4
5

Como funciona:
O input() pede ao usuário para digitar um número.

O int() converte esse valor para um número inteiro.

O for percorre de 1 a 10 (inclusive) e multiplica o número pelo valor atual da variável i.

Em cada repetição, o resultado é mostrado com print().

 O que é o i no laço for?
O i é uma variável de controle. Ela representa o valor atual da repetição dentro do laço for.
O que acontece aqui?

O range(1, 6) cria os números: 1, 2, 3, 4, 5

O i vai mudando a cada volta do laço:

Na 1ª repetição, i = 1

Na 2ª repetição, i = 2

Na 3ª repetição, i = 3

E assim por diante...

Cada vez que o bloco dentro do for roda, o i tem um valor diferente da sequência.


    

#     Atividade 02:
# Soma de Números de 1 a 100:
# Crie um programa que use um laço for para somar
# todos os números de 1 a 100 e exiba o resultado.


# # Inicializa a variável que vai guardar a soma
# soma = 0

# # Laço for para somar os números de 1 a 100
# for i in range(1, 101,1):
#     soma += i  # mesma coisa que soma = soma + i

# # Exibe o resultado final
# print(f"A soma dos números de 1 a 100 é: {soma}")


# soma = 0
# for i in range(1, 101,1):
#     soma += i
#     print(soma)

 
 
#  Explicação linha por linha:

# soma = 0
# Cria uma variável chamada soma e começa com o valor 0.

# Ela será usada para acumular a soma dos números.

# for i in range(1, 101):
# Cria um laço que vai de 1 até 100 (o 101 é excluído).

# A variável i vai receber os valores: 1, 2, 3, ..., até 100.

# O laço vai rodar 100 vezes, somando um número a cada repetição.

# soma += i
# Isso é uma forma curta de escrever: soma = soma + i

# A cada volta do laço, o valor de i é adicionado à variável soma.

# print(...)
# Depois que o laço termina, mostramos o resultado com print().

# 🧮 Como funciona:
# No final, o programa vai fazer:

# soma = 1 + 2 + 3 + ... + 100

# O resultado será:

# A soma dos números de 1 a 100 é: 5050



# Atividade 03:
# Caractere por Caractere:
# Escreva um programa que solicite uma palavra ao usuário e use um
# laço for para exibir cada caractere da palavra em uma linha separada.
    
#     # Solicita uma palavra ao usuário
# palavra = input("Digite uma palavra: ")

# # Laço for para exibir cada caractere da palavra
# for letra in palavra:
#     print(letra)

#     Explicação linha por linha:
# palavra = input("Digite uma palavra: ")
# Pede para o usuário digitar uma palavra.

# O valor digitado é guardado na variável palavra.

# for letra in palavra:
# Este laço for percorre cada caractere da palavra, um por um.

# A variável letra assume o valor de cada letra da string na ordem.

# print(letra)
# Mostra cada letra em uma linha separada.

# 🖥️ Exemplo de execução:

# Se o usuário digitar:
# amor

# a 
# m
# o
# r




    

#     Atividade 04:
# Contagem Regressiva de 10 a 1:
# Desenvolva um programa que use um laço for para fazer uma
# contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

# # Laço for para contagem regressiva de 10 até 1
# for i in range(10, 0, -1):
#     print(i)

# # Mensagem final
# print("Feliz Ano Novo!")

# Explicação linha por linha:
# for i in range(10, 0, -1):
# O range() aqui tem três partes:

# 10 → início da contagem (começa em 10)

# 0 → parada da contagem (vai até 1, pois o 0 não é incluído)

# -1 → passo negativo (diminui 1 a cada volta)

# 👉 Isso faz o i contar assim: 10, 9, 8, 7, ..., 1

# print(i)
# Exibe o valor atual de i na tela, um número por linha.

# print("Feliz Ano Novo!")
# Depois da contagem, exibe a mensagem final 🎉

# 🖥️ Saída esperada:

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Feliz Ano Novo!


# ATIVIDADE PRÁTICA

# Atividade 05:
# Contagem de Números Positivos e Negativos:
# Escreva um programa que solicite ao usuário 10 números e use um
# laço for com uma condicional para contar quantos são positivos e
# quantos são negativos.

# Variáveis para contar positivos e negativos
# positivos = 0
# negativos = 0

# # Laço for para receber 10 números
# for i in range(1, 11):
#     numero = int(input(f"Digite o {i}º número: "))
    
#     # Verifica se o número é positivo ou negativo
#     if numero > 0:
#         positivos += 1
#     elif numero < 0:
#         negativos += 1
#     # Zero não conta como positivo nem negativo (pode ser tratado separadamente se quiser)

# # Exibe os resultados
# print(f"\nQuantidade de números positivos: {positivos}")
# print(f"Quantidade de números negativos: {negativos}")



# positivo = 0
# negativo = 0
# for i in range(10):
#     numero=int(input("digite um numero: "))
#     if numero<0:
#         negativo+=1
#     else:
#         positivo+=1
# print(f"total negativos= {negativo}")
# print(f"total positivos={positivo}")

# Explicação:
# positivos e negativos: variáveis que começam em 0 e vão contar quantos números são de cada tipo.

# for i in range(1, 11): faz o laço rodar 10 vezes, de 1 a 10.

# input(...): pede um número ao usuário a cada repetição.

# if numero > 0: se for positivo, soma 1 na variável positivos.

# elif numero < 0: se for negativo, soma 1 na variável negativos.

# print(...): mostra os totais no final.

# 🖥️ Exemplo de execução:
# Se o usuário digitar:

# 5
# -3
# 0
# 7
# -1
# -4
# 2
# 8
# -6
# 1
# A saída será:


# Quantidade de números positivos: 5
# Quantidade de números negativos: 4





# # Atividade 06:
# # Soma de Números Pares:
# # Escreva um programa que use um laço for para somar
# # todos os números pares de 1 a 50 e exiba o resultado final.


# # Atividade 07:
# # Contagem de Vogais em uma Palavra:
# # Crie um programa que solicite uma palavra ao usuário e use um laço for com
# # uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.


# # Atividade 08:
# # Cálculo de Média de Notas:
# # Escreva um programa que solicite 5 notas de alunos. Use um laço for
# # para somar as notas e uma condicional para exibir a média e a
# # classificação ("Aprovado" para média >= 6, "Reprovado" para média < 6).


# # ATIVIDADE PRÁTICA

# # Atividade 09:
# # Verificar Números Pares e Impares com Interrupção:
# # Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
# # identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.


# # Atividade 10:
# # Contar Números Positivos e Negativos:
# # Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
# # são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.
    

# #     Atividade 11:
# # Verificar Múltiplos de 5 e Parar:
# # Escreva um programa que use um laço for para imprimir números de 1 a 30.
# # Use uma condicional para verificar se um número é múltiplo de 5 e outro
# # para verificar se é maior que 20 e interromper o loop com break.


# # Atividade 12:
# # Soma de Números com Desconto:
# # Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
# # calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
# # interrompa o loop com break.


