# ______________________________________________________ Modulo de Python ____________________________________________________________


# # # O que é lista?
# # #é uma variável que guarda mais de um valor ao mesmo tempo. Cada um desses valores, tem uma posição (índice, index), e sempre começa com 0


# # # lista = ["Nath",1,1.75,True,[]]
# # # print(lista[0])

# # #como adicionar algo no final da lista?
# # #append significa acrescentar e ele adiciona algo ao final da lista, mas apenas um por vez!
# # # lista.append("Jonathan")
# # # print(lista)

# # #função e método:

# # #Função: é um comando que faz alguma coisa, mas não depende do tipo da informação

# # #Método:  é um comando que faz alguma coisa mas DEPENDE do tipo da informação

# # # nome = 'nathalia'
# # # print(nome.upper())


# # #como adicionar algo em qualquer posição da lista?
# # # lista = ["Nath",1,1.75,True,[]]
# # # lista.insert(4,"Infinity School")
# # # print(lista)

# # #como remover algo de uma lista?
# # lista = ["Nath",1,1.75,True,[]]

# # #pop() - o pop() sem valor nos parenteses, remove o ultimo elemento da lista.
# # # lista.pop()
# # # print(lista)

# # #pop(posição)
# # # lista.pop(3)
# # # print(lista)

# # # numeros = [1,2,3,4,5,5,5,6,7,8]
# # # numeros.remove(5)
# # # print(numeros)
# # #remove() - ele espera receber o valor do elemento que voce quer remover, mas tem a seguinte observação, ele so remove a primeira ocorrencia do elemento

# # nomes = ["Jonathan","Lucrécio","Matheus","Alexsander","Nathalia","Paulo","Oswaldo"]
# # # for nome in nomes:
# # #     print(nome)

# # # nomes.extend(["Cristiane","Bárbara","Erick"]) - Adiciona mais de um elemento ao final da lista, mas esses elementos precisam estar dentro de outra lista
# # # print(nomes)

# # # nomes.sort() - organiza uma lista do menor para o maior ou em "ordem alfabética"
# # # print(nomes)


# numeros = [1,2,2,2,2,3,4,5,6,7,7,7,8]
# # print(numeros.count(7)) - conta quantas vezes o elemento  dentro dos parenteses aparece na lista


# # nomes.reverse() - Reverte a lista
# # print(nomes)


# # print(numeros.index(4))

# # nomes.clear() - Limpa a lista
# # print(nomes)


# #como saber o tamanho da lista?
# # print(len(numeros))






# # if not tem_habilitacao:
# #     print("Você não tem habilitação! ")


# # nomes = ["Jonathan","Lucrécio","Matheus","Alexsander","Nathalia","Paulo","Oswaldo"]
# # for nome in nomes:
# #     print(nome)

# # nomes.extend(["Cristiane","Bárbara","Erick"]) - Adiciona mais de um elemento ao final da lista, mas esses elementos precisam estar dentro de outra lista
# # print(nomes)

# # nomes.sort() - organiza uma lista do menor para o maior ou em "ordem alfabética"
# # print(nomes)


# # numeros = [1,2,2,2,2,3,4,5,6,7,7,7,8]
# # print(numeros.count(7)) - conta quantas vezes o elemento  dentro dos parenteses aparece na lista


# # nomes.reverse() - Reverte a lista
# # print(nomes)


# # print(numeros.index(4))

# # nomes.clear() - Limpa a lista
# # print(nomes)


# #como saber o tamanho da lista?
# # print(len(numeros))



# # numeros = [1,1,1,1,1,1,1,1,2,3,4,5,8,7,345,22,6,8,456,87,24,7]
# # qtd = numeros.count(1)
# # print(qtd)
# # numeros.sort()
# # print(numeros)



# # nums = []
# # qtd = int(input("Quantos numeros você quer digitar: "))
# # for i in range(qtd):
# #     numero = int(input("Digite um número: "))
# #     nums.append(numero)
# # soma = sum(nums)
# # media = soma/len(nums)
# # print(media)


# # lista = [1,1,2,3,4,5,5,5]
# # for i in lista:
# #     qtd = lista.count(i)#2
# #     print(f'Tem {qtd} numeros {i}')
# #     if qtd>1:
# #         lista.remove(i)
# # print(lista)


# #escreva um código em python que receba uma lista de numeros como entrada e retorne uma lista contendo a soma de cada par de numeros que aparecem consecutivamente

# #tem uma lista de numeros em algum lugar
# #tem um for de lista em algum lugar
# #se o próximo numero, for o seguinte do atual, some os dois e adicione em uma nova lista

# # lista = [1,2,3,4,5,6,7]
# # resultado = []
# # for i in range(len(lista) - 1):
# #     soma = lista[i] + lista[i + 1]
# #     resultado.append(soma)
# # print(resultado)

# Na imagem, você pediu 5 exercícios sobre listas em Python, e eu sugeri os seguintes:

# 1.Média de uma lista:
# Escreva uma função que receba uma lista de números como entrada e retorne a média dos números na lista.

# def media_lista(lista):
#     if not lista:
#         return 0
#     return sum(lista) / len(lista)

# # Exemplo
# print(media_lista([5, 10, 15]))  # Saída: 20.0

# Explicação linha por linha:

# def media_lista(lista):
# Define a função chamada media_lista, que recebe um parâmetro chamado lista.

# if not lista:
# Verifica se a lista está vazia. Em Python, uma lista vazia é considerada "False".

# return 0
# Se a lista estiver vazia, a função retorna zero (evita erro de divisão por zero).

# sum(lista)
# Soma todos os valores da lista.

# len(lista)
# Conta quantos elementos existem na lista.

# return sum(lista) / len(lista)
# Faz a divisão da soma pela quantidade para calcular a média.


# 2.Remover duplicatas:
# Escreva uma função que receba uma lista e retorne uma nova lista com todos os duplicados removidos, mantendo a ordem original dos elementos.

# def remover_duplicatas(lista):
#     nova_lista = []
#     for item in lista:
#         if item not in nova_lista:
#             nova_lista.append(item)
#     return nova_lista

# # Exemplo
# print(remover_duplicatas([1, 2, 2, 3, 1, 4]))  # Saída: [1, 2, 3, 4]

# Explicação passo a passo:
# 1.nova_lista = []
# Cria uma lista vazia para guardar os elementos sem repetição.

# 2.for item in lista:
# Percorre cada elemento da lista original.

# 3.if item not in nova_lista:
# Verifica se o item ainda não foi adicionado.

# 4.mnova_lista.append(item)
# Se for a primeira vez, adiciona à nova lista.

# 5.return nova_lista
# Retorna a lista sem duplicatas.


# 3.Inversão de lista:
# Escreva uma função que receba uma lista como entrada e retorne uma nova lista com os elementos na ordem inversa.

# def inverter_lista(lista):
#     return lista[::-1]

# # Exemplo
# print(inverter_lista([1, 2, 3, 4]))  # Saída: [4, 3, 2, 1]



# FORMA ALTERNATIVA (sem [::-1]):

# def inverter_lista(lista):
#     nova_lista = []
#     for i in range(len(lista)-1, -1, -1):
#         nova_lista.append(lista[i])
#     return nova_lista
# print(inverter_lista([1, 2, 3, 4]))

# Explicação:
# range(len(lista)-1, -1, -1) conta de trás pra frente.

# Vai pegando os elementos do fim até o começo.



# 4.Ordenação parcial:
# Escreva uma função que receba uma lista de números como entrada e retorne uma nova lista contendo os números pares ordenados e os ímpares na mesma ordem original.

# def ordenar_pares(lista):
#     pares_ordenados = sorted([x for x in lista if x % 2 == 0])
#     resultado = []
#     indice_par = 0
#     for num in lista:
#         if num % 2 == 0:
#             resultado.append(pares_ordenados[indice_par])
#             indice_par += 1
#         else:
#             resultado.append(num)
#     return resultado

# # Exemplo
# print(ordenar_pares([5, 4, 2, 7, 6]))  # Saída: [5, 2, 4, 7, 6]


# 5.Soma de elementos consecutivos:
# Escreva uma função que receba uma lista de números e retorne uma nova lista contendo a soma de cada par de elementos consecutivos da lista original.

# def soma_consecutivos(lista):
#     return [lista[i] + lista[i + 1] for i in range(len(lista) - 1)]

# # Exemplo
# print(soma_consecutivos([1, 2, 3, 4]))  # Saída: [3, 5, 7]



# # Mini-Projeto: Operações com Listas


# def media_lista(lista):
#     if not lista:
#         return 0
#     return sum(lista) / len(lista)

# def remover_duplicatas(lista):
#     nova_lista = []
#     for item in lista:
#         if item not in nova_lista:
#             nova_lista.append(item)
#     return nova_lista

# def inverter_lista(lista):
#     return lista[::-1]

# def ordenar_pares(lista):
#     pares_ordenados = sorted([x for x in lista if x % 2 == 0])
#     resultado = []
#     indice_par = 0
#     for num in lista:
#         if num % 2 == 0:
#             resultado.append(pares_ordenados[indice_par])
#             indice_par += 1
#         else:
#             resultado.append(num)
#     return resultado

# def soma_consecutivos(lista):
#     return [lista[i] + lista[i + 1] for i in range(len(lista) - 1)]

# def converter_entrada(entrada):
#     return list(map(int, entrada.strip().split()))

# def menu():
#     while True:
#         print("\n=== MENU: Operações com Listas ===")
#         print("1. Calcular média da lista")
#         print("2. Remover duplicatas")
#         print("3. Inverter a lista")
#         print("4. Ordenar números pares (ímpares mantêm a ordem)")
#         print("5. Somar elementos consecutivos")
#         print("0. Sair")
#         opcao = input("Escolha uma opção: ")

#         if opcao == "0":
#             print("Saindo do programa. Até mais!")
#             break

#         entrada = input("Digite os números da lista, separados por espaço: ")
#         lista = converter_entrada(entrada)

#         if opcao == "1":
#             print("Média da lista:", media_lista(lista))
#         elif opcao == "2":
#             print("Lista sem duplicatas:", remover_duplicatas(lista))
#         elif opcao == "3":
#             print("Lista invertida:", inverter_lista(lista))
#         elif opcao == "4":
#             print("Pares ordenados, ímpares mantidos:", ordenar_pares(lista))
#         elif opcao == "5":
#             print("Soma dos elementos consecutivos:", soma_consecutivos(lista))
#         else:
#             print("Opção inválida. Tente novamente.")





#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) quantas vezes apareceu o valor 9. B) Em que posiçaõ foi digitado o primeiro valor 3. C) Quais foram os números pares.



# # Lê quatro valores e guarda em uma tupla
# valores = (
#     int(input('Digite o 1º valor: ')),
#     int(input('Digite o 2º valor: ')),
#     int(input('Digite o 3º valor: ')),
#     int(input('Digite o 4º valor: '))
# )

# print(f'\nVocê digitou os valores: {valores}')

# # A) Quantas vezes apareceu o valor 9
# print(f'O valor 9 apareceu {valores.count(9)} vez(es).')

# # B) Em que posição foi digitado o primeiro valor 3
# if 3 in valores:
#     print(f'O valor 3 apareceu primeiro na posição {valores.index(3)+1}ª.')
# else:
#     print('O valor 3 não foi digitado.')

# # C) Quais foram os números pares
# pares = [n for n in valores if n % 2 == 0]
# if pares:
#     print(f'Os números pares digitados foram: {pares}')
# else:
#     print('Nenhum número par foi digitado.')


#     #Explicação rápida:
# #tuple() armazena os números como imutáveis.

# #.count(9) conta quantas vezes o número 9 apareceu.

# #index(3) mostra a posição do primeiro 3 (começa do 0, então somamos +1 para mostrar “posição humana”).

# #A lista [n for n in valores if n % 2 == 0] usa list comprehension para pegar só os pares.



# programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado(entre o e 20) e mostrá-lo por extenso.

# # Tupla com os números de 0 a 20 por extenso
# numeros_por_extenso = (
#     'zero', 'um', 'dois', 'três', 'quatro',
#     'cinco', 'seis', 'sete', 'oito', 'nove',
#     'dez', 'onze', 'doze', 'treze', 'quatorze',
#     'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
#     'vinte'
# )

# while True:
#     numero = int(input("Digite um número entre 0 e 20: "))
#     if 0 <= numero <= 20:
#         break
#     print("Tente novamente. Número fora do intervalo!")

# print(f"Você digitou o número {numeros_por_extenso[numero]}.")

# Como funciona:
#A tupla numeros_por_extenso armazena os nomes dos números de 0 a 20.

#Um laço while garante que o usuário só digite um número válido (entre 0 e 20).

#Quando um número válido é digitado, o programa mostra o número por extenso usando o índice da tupla.


#  uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,na ordem de colocação.Deois moestre: A) apenas os 5 primeiros colocados. B) os últimos 4 colocados da tabela. C) uma lista com os times em ordem alfabética. D) em que posição na tabela está o time do corinthians .


# Tupla com os 20 primeiros colocados do Brasileirão (exemplo fictício)

# tabela_brasileirao = (
#     'Flamengo', 'Botafogo', 'Palmeiras', 'Grêmio', 'Atlético-MG',
#     'Athletico-PR', 'Bragantino', 'Fortaleza', 'Internacional', 'Cuiabá',
#     'São Paulo', 'Cruzeiro', 'Bahia', 'Corinthians', 'Santos',
#     'Vasco', 'Goiás', 'Coritiba', 'América-MG', 'Chapecoense'
# )

# # A) Os 5 primeiros colocados
# #print("A) Os 5 primeiros colocados são:")uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato #brasileiro de futebol,na ordem de colocação.Deois moestre: A) apenas os 5 primeiros colocados. B) os últimos 4 colocados #da tabela. C) uma lista com os times em ordem alfabética. D) em que posição na tabela está o time do corinthians .
# print(tabela_brasileirao[:5])

# # B) Os 4 últimos colocados
# print("\nB) Os 4 últimos colocados são:")
# print(tabela_brasileirao[-4:])

# # C) Times em ordem alfabética
# print("\nC) Times em ordem alfabética:")
# print(sorted(tabela_brasileirao))

# # D) Posição do Corinthians (índice + 1 porque posição começa em 1, não 0)
# posicao = tabela_brasileirao.index('Corinthians') + 1
# print(f"\nD) O Corinthians está na {posicao}ª posição da tabela.")

#uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,na ordem de colocação.Deois moestre: A) apenas os 5 primeiros colocados. B) os últimos 4 colocados da tabela. C) uma lista com os times em ordem alfabética. D) em que posição na tabela está o time do corinthians"


# um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e tambem indique o menor eo maior valor que estão na tupla.


# from random import randint

# # Gerar 5 números aleatórios entre 1 e 100 e colocá-los em uma tupla
# numeros = (
#     randint(1, 100),
#     randint(1, 100),
#     randint(1, 100),
#     randint(1, 100),
#     randint(1, 100)
# )

# # Mostrar os números gerados
# print("Números sorteados:", numeros)

# # Mostrar o maior e o menor valor
# print("Maior número:", max(numeros))
# print("Menor número:", min(numeros))

# Explicando:
#randint(1, 100) → gera um número aleatório entre 1 e 100.

#max(tupla) → retorna o maior valor da tupla.

#min(tupla) → retorna o menor valor da tupla.


# Tupla com produtos e preços (nome, preço, nome, preço...)
# produtos = (
#     'Lápis', 1.50,
#     'Caneta', 2.00,
#     'Caderno', 15.90,
#     'Borracha', 0.99,
#     'Mochila', 120.00,
#     'Estojo', 12.50,
#     'Régua', 3.75,
#     'Livro', 45.00
# )

# print('-' * 40)
# print(f'{"LISTAGEM DE PREÇOS":^40}')
# print('-' * 40)

# # Percorre os itens da tupla em pares (produto, preço)
# for i in range(0, len(produtos), 2):
#     nome = produtos[i]
#     preco = produtos[i + 1]
#     print(f'{nome:.<30} R$ {preco:>7.2f}')

# print('-' * 40)

#EXPLICAÇÃO COMPLETA DO CÓDIGO
#Objetivo:
#Criar uma tupla com nomes de produtos e seus respectivos preços, e depois exibir uma tabela de preços formatada.

# 1. A TUPLA:

# #produtos = (
#     'Lápis', 1.50,
#     'Caneta', 2.00,
#     ...
# )


#A tupla armazena nomes e preços intercalados:

#Índices pares (0, 2, 4...) = nomes dos produtos.

#Índices ímpares (1, 3, 5...) = preços.

#2. Cabeçalho da tabela:
#print('-' * 40)
#print(f'{"LISTAGEM DE PREÇOS":^40}')
#print('-' * 40)

#'-' * 40 → Imprime 40 traços.

#f'{"LISTAGEM DE PREÇOS":^40}' → Centraliza o título em 40 caracteres.

#3. Laço for para percorrer os dados:

#for i in range(0, len(produtos), 2):
    
#Começa em 0 e vai até o final da tupla.

#Vai de 2 em 2 porque cada item é composto por um nome e um preço.

#Exemplo: índice 0 → "Lápis", índice 1 → 1.50

#4. Coleta dos dados:

#nome = produtos[i]
#preco = produtos[i + 1]

#Para cada par:

#nome pega o nome do produto.

#   preco pega o preço correspondente.

# 5. Impressão formatada da linha:

#print(f'{nome:.<30} R$ {preco:>7.2f}')

#nome:.<30 → imprime o nome e preenche com pontos até 30 espaços.

#preco:>7.2f → imprime o preço:

#Alinhado à direita.

#Com 2 casas decimais.

#Dentro de 7 espaços (ex: 2.00)

# 6. Final da tabela:

#print('-' * 40)

#Mais uma linha de traços para finalizar.

# Exemplo de saída:

# ----------------------------------------
#          LISTAGEM DE PREÇOS         
# ----------------------------------------
# Lápis........................... R$    1.50
# Caneta.......................... R$    2.00
# Caderno......................... R$   15.90
# Borracha........................ R$    0.99
# Mochila......................... R$  120.00
# Estojo.......................... R$   12.50
# Régua........................... R$    3.75
# Livro........................... R$   45.00
# ----------------------------------------


#Criar um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quai são as suas vogais.


# Tupla com várias palavras (sem acento)
# palavras = ("carro", "bicicleta", "aviao", "computador", "python", "programacao")

# # Conjunto com as vogais para facilitar a checagem
# vogais = set("aeiou")

# # Para cada palavra na tupla
# for palavra in palavras:
#     # Criar um conjunto para armazenar as vogais encontradas na palavra
#     vogais_na_palavra = set()

#     # Percorrer cada letra da palavra
#     for letra in palavra:
#         # Se a letra for vogal, adiciona no conjunto
#         if letra in vogais:
#             vogais_na_palavra.add(letra)
    
#     # Mostrar as vogais encontradas na palavra, ordenadas em ordem alfabética
#     print(f"Palavra '{palavra}' tem as vogais: {', '.join(sorted(vogais_na_palavra))}")


    #Explicação:
#Usei uma tupla chamada palavras com algumas palavras.

#Um set com as vogais para facilitar a comparação (mais rápido que lista).

#Para cada palavra, eu verifico letra por letra se é vogal.

#Uso um conjunto para armazenar as vogais, assim não repete.

#No final, mostro as vogais encontradas, ordenadas para ficar mais organizado.#

#o código linha a linha, bem simples pra você copiar e entender direitinho.


#palavras = ("carro", "bicicleta", "aviao", "computador", "python", "programacao")
#Aqui criamos uma tupla chamada palavras que armazena várias palavras sem acento. A tupla é imutável, então não dá pra alterar depois.


#vogais = set("aeiou")
#Criamos um conjunto (set) chamado vogais que contém as letras 'a', 'e', 'i', 'o', 'u'. O set é usado para facilitar a checagem rápida se uma letra está entre as vogais.


#for palavra in palavras:
#Iniciamos um laço que vai percorrer palavra por palavra dentro da tupla palavras.


   # vogais_na_palavra = set()
#Para cada palavra, criamos um conjunto vazio chamado vogais_na_palavra para armazenar as vogais encontradas nessa palavra. Usamos set pra evitar repetições.


    #for letra in palavra:
#Agora, para cada palavra, fazemos outro laço que percorre letra por letra dentro da palavra.


        #if letra in vogais:
            #vogais_na_palavra.add(letra)
#Se a letra atual estiver dentro do conjunto vogais (ou seja, se for vogal), adicionamos essa letra ao conjunto vogais_na_palavra.


    #print(f"Palavra '{palavra}' tem as vogais: {', '.join(sorted(vogais_na_palavra))}")
#Depois de verificar todas as letras da palavra, mostramos na tela quais vogais foram encontradas.

#Usamos sorted() para ordenar as vogais em ordem alfabética.

#O ', '.join(...) transforma o conjunto em uma string separada por vírgulas, para mostrar bonitinho.



                                      #Curso de Python - Lista e Tupla 20/07/2025


# num = [2, 5 , 9, 1]
# num [2] = 3
# num [3] = 7
# num.append(8)  # Adiciona o número 8 ao final da lista
# #num.sort()  # Organiza a lista em ordem crescente
# #num.reverse()  # Inverte a ordem da lista
# num.sort(reverse=True)
# num.insert(2, 0)  # Insere o número 0 na posição 2
# num.pop()  # Remove o último elemento da lista
# num.pop(2)  # Remove o elemento na posição 2
# num.append(3)  # Adiciona o número 3 ao final da lista
# num.remove(3)  # Remove a primeira ocorrência do número 3
# if 5 in num:  # Verifica se o número 4 está na lista
#     num.remove(5)  # Remove o número 4 se ele estiver na lista
# else:
#     print(f'Não existe o número 4 na lista, então não foi removido.')
# print(num)  
# print(f'Essa lista tem {len(num)} elementos.')


# valores = []
# valores.append(2) 
# valores.append(5)
# valores.append(9)
# valores.append(1)   
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print(f'Cheguei ao final da lista com {len(valores)} elementos.')

# valores = []  # Cria uma lista vazia
# for c in range(0, 10):  # Loop de 0 a 9
#     valores.append(int(input(f'Digite o valor: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print(f'Cheguei ao final da lista com {len(valores)} elementos.')

a = [2, 3, 4, 7,]   
b = a[:] # Faz uma cópia da lista a
b[2] = 8  # Altera o terceiro elemento da lista b
print(f'Lista A: {a}')  
print(f'Lista B: {b}')




    

  




