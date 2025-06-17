# FOR É TILIZADO QUANDO VOCES SABEM A QUANTIDADE DE VEZES QUE ALGO PRECISA SER REPETIDO


#toda vez que fizer um while com cndição, precisa de uma linha de código para que ess condição , em algum momento, se torne falsa.



# contador = 1 
# while contador <=5:
#     print(contador)
#     contador+=1

    #mostre uma contagem de 10 azero,e no final, mostre feliz ano novo!

# Atividade 01:
# Contagem de 1 a 10:
# Crie um programa que use um laço while
# para contar de 1 a 10 e exibir cada número.


# contador = 10
# while contador >=0:
#     print(contador)
#     contador-=1



# # Atividade 02:
# Soma de Números de 1 a 100:
# Escreva um programa que use um laço while para
# somar os números de 1 a 100 e exiba o resultado.



# contador = 1
# soma = 0
# while contador <=100:
#      soma+=contador
#      contador+=1  
# print(soma)



# Atividade 03:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).


# numero = int(input('digite um numero:'))
# tabuada = 1
# while tabuada <= 10:
#     resultado = numero*tabuada
#     print(f"{numero}x{tabuada}={resultado} ")
#     tabuada+=1






# Atividade 04:
# Contagem Regressiva:
# Desenvolva um programa que use um laço while para exibir
# uma contagem regressiva de 10 até 1 e, em seguida, exiba
# "Feliz Ano Novo!".

# import time

# contador = 10 

# while contador >= 1:
#     print(contador)
#     time.sleep(1)
#     contador-=1 
# print("Feliz Ano Novo!")
    

    



# ATIVIDADE PRÁTICA

# Atividade 05:
# Contagem até o Número Inserido:
# Crie um programa que solicite um número ao usuário e use
# um laço while para contar de 1 até o número inserido,
# exibindo apenas os números ímpares.


# import time
# limite = int(input('digite um numero:'))
# contador = 1
# while contador <= limite:
#     if contador % 2 != 0:
#         print(contador)
#         time.sleep(0.5)
#     contador += 1
# print("Fim")

# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.

# soma = 0
# while True:
#     numero = int(input('Digite um número: '))
#     if numero % 2 != 0:
#         break
#     soma += numero
# print(f'A soma dos números positivos é: {soma}')



# Atividade 07:
# Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.

# # Solicita um número ao usuário
# numero = int(input("Digite um número para ver a tabuada (somente os múltiplos de 3): "))

# # Inicializa o contador
# contador = 1

# # Laço while para gerar a tabuada até 10
# while contador <= 10:
#     resultado = numero * contador
#     # Verifica se o resultado é múltiplo de 3
#     if resultado % 3 == 0:
#         print(f"{numero} x {contador} = {resultado}")
#     contador += 1




# Atividade 08:
# Média de Notas:
# Desenvolva um programa que solicite as notas dos alunos até
# que o usuário digite -1. Calcule e exiba a média das notas
# inseridas.



# # Inicializa as variáveis
# soma = 0
# quantidade = 0

# # Solicita notas até que o usuário digite -1
# while True:
#     nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
    
#     if nota == -1:
#         break  # Encerra o loop se o usuário digitar -1

#     soma += nota
#     quantidade += 1

# # Verifica se alguma nota foi inserida
# if quantidade > 0:
#     media = soma / quantidade
#     print(f"Média das notas: {media:.2f}")
# else:
#     print("Nenhuma nota foi inserida.")



# Atividade 09:
# Contagem até 10:
# Crie um programa que use um laço while para contar de 1 a 10
# e termine quando atingir 10.

# contador = 1

# while contador <= 10:
#     print(contador)
#     contador += 1  # Incrementa o contador a cada repetição




# Atividade 10:

# Escreva um programa que use um laço while para somar
# números consecutivos começando de 1 e termine quando
# a soma atingir ou ultrapassar 50.
# Atividade 10:
# Soma até 50:


# soma = 0
# numero = 1

# while soma < 50:
#     soma += numero
#     print(f"Adicionando {numero}, soma atual: {soma}")
#     numero += 1

# print("\nA soma final atingiu ou ultrapassou 50.")



# Atividade 11:
# Entrada Válida:
# Crie um programa que solicite ao usuário um número entre 1 e 10.
# Continue pedindo até que o usuário forneça um valor válido.

# # Solicita um número entre 1 e 10 até o usuário digitar corretamente
# numero = int(input("Digite um número entre 1 e 10: "))

# while numero < 1 or numero > 10:
#     print("Número inválido. Tente novamente.")
#     numero = int(input("Digite um número entre 1 e 10: "))

# print(f"Você digitou o número válido: {numero}")



# Atividade 12:
# Desenvolva um programa que peça ao usuário para digitar uma
# senha e continue pedindo até que a senha correta (previamente
# definida) seja inserida.
# Atividade 12:
# Senha Correta:


# # Senha previamente definida
# senha_correta="130683"

# # Solicita a senha ao usuário
# senha = input("Digite a senha:")

# # Continua pedindo até que a senha correta seja digitada
# while senha != senha_correta:
#     print("Senha incorreta. Tente novamente.")
#     senha = input("Digite a senha:")

# print("Acesso permitido. Senha correta!")















 # Imprimir números de 1 a 5 com while
# contador = 1

# while contador <= 5:
#     print(contador)
#     contador += 1

#     # Imprimir números de 1 a 5 com for
# for numero in range(1, 6):
#     print(numero)


# nomes = ["Ana", "Bruno", "Carlos", "Diana"]

# for nome in nomes:
#     print("Olá,", nome)

nomes = ["Ana", "Bruno", "Carlos", "Diana"]
indice = 0

while indice < len(nomes):
    print("Olá,", nomes[indice])
    indice += 1




tarefas = ["Estudar Python", "Fazer exercícios", "Ler um livro", "Beber água"]

print("=== Lista de Tarefas ===")
while tarefas:
    print("\nTarefa atual:", tarefas[0])
    resposta = input("Você já concluiu essa tarefa? (s/n): ")

    if resposta.lower() == 's':
        tarefa_concluida = tarefas.pop(0)
        print(f"✅ Tarefa '{tarefa_concluida}' marcada como concluída!")
    else:
        print("🔄 Ok, volte quando terminar.")

print("\n🎉 Parabéns! Você concluiu todas as tarefas!")




tarefas = ["Estudar Python", "Fazer exercícios", "Ler um livro", "Beber água"]

print("=== Lista de Tarefas ===")
concluidas = 0

for tarefa in tarefas:
    print("\nTarefa:", tarefa)
    resposta = input("Você já concluiu essa tarefa? (s/n): ")

    if resposta.lower() == 's':
        print(f"✅ Muito bem! '{tarefa}' marcada como concluída.")
        concluidas += 1
    else:
        print("🔄 Tarefa pendente. Tente concluí-la mais tarde.")

print(f"\nVocê concluiu {concluidas} de {len(tarefas)} tarefas.")



 while = "repita enquanto isso for verdade"
Você não sabe exatamente quantas vezes vai repetir.

Ele continua rodando até você mandar parar.

Útil para jogos, menus ou esperar uma resposta certa.

Exemplo com while:

# senha = ""
# while senha != "1234":
#     senha = input("Digite a senha: ")

# print("Acesso liberado!")


Resumo simples: diferença entre for e while
🔁 for = "repita X vezes ou percorra essa lista"
Você sabe quantas vezes vai repetir.

Serve para percorrer listas, como nomes ou tarefas.

Vai do começo até o fim, uma vez só.

Exemplo com for:



for nome in ["Ana", "João", "Lia"]:
    print("Olá", nome)
















     
     
