# ______________________________________________________ Modulo de Python ____________________________________________________________


# # O que é lista?
# #é uma variável que guarda mais de um valor ao mesmo tempo. Cada um desses valores, tem uma posição (índice, index), e sempre começa com 0


# # lista = ["Nath",1,1.75,True,[]]
# # print(lista[0])

# #como adicionar algo no final da lista?
# #append significa acrescentar e ele adiciona algo ao final da lista, mas apenas um por vez!
# # lista.append("Jonathan")
# # print(lista)

# #função e método:

# #Função: é um comando que faz alguma coisa, mas não depende do tipo da informação

# #Método:  é um comando que faz alguma coisa mas DEPENDE do tipo da informação

# # nome = 'nathalia'
# # print(nome.upper())


# #como adicionar algo em qualquer posição da lista?
# # lista = ["Nath",1,1.75,True,[]]
# # lista.insert(4,"Infinity School")
# # print(lista)

# #como remover algo de uma lista?
# lista = ["Nath",1,1.75,True,[]]

# #pop() - o pop() sem valor nos parenteses, remove o ultimo elemento da lista.
# # lista.pop()
# # print(lista)

# #pop(posição)
# # lista.pop(3)
# # print(lista)

# # numeros = [1,2,3,4,5,5,5,6,7,8]
# # numeros.remove(5)
# # print(numeros)
# #remove() - ele espera receber o valor do elemento que voce quer remover, mas tem a seguinte observação, ele so remove a primeira ocorrencia do elemento

# nomes = ["Jonathan","Lucrécio","Matheus","Alexsander","Nathalia","Paulo","Oswaldo"]
# # for nome in nomes:
# #     print(nome)

# # nomes.extend(["Cristiane","Bárbara","Erick"]) - Adiciona mais de um elemento ao final da lista, mas esses elementos precisam estar dentro de outra lista
# # print(nomes)

# # nomes.sort() - organiza uma lista do menor para o maior ou em "ordem alfabética"
# # print(nomes)


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


# nomes = ["Jonathan","Lucrécio","Matheus","Alexsander","Nathalia","Paulo","Oswaldo"]
# # for nome in nomes:
# #     print(nome)

# # nomes.extend(["Cristiane","Bárbara","Erick"]) - Adiciona mais de um elemento ao final da lista, mas esses elementos precisam estar dentro de outra lista
# # print(nomes)

# # nomes.sort() - organiza uma lista do menor para o maior ou em "ordem alfabética"
# # print(nomes)


# numeros = [1,2,2,2,2,3,4,5,6,7,7,7,8]
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

Na imagem, você pediu 5 exercícios sobre listas em Python, e eu sugeri os seguintes:

1.Média de uma lista:
Escreva uma função que receba uma lista de números como entrada e retorne a média dos números na lista.

def media_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

# Exemplo
print(media_lista([10, 20, 30]))  # Saída: 20.0


2.Remover duplicatas:
Escreva uma função que receba uma lista e retorne uma nova lista com todos os duplicados removidos, mantendo a ordem original dos elementos.

def remover_duplicatas(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

# Exemplo
print(remover_duplicatas([1, 2, 2, 3, 1, 4]))  # Saída: [1, 2, 3, 4]


3.Inversão de lista:
Escreva uma função que receba uma lista como entrada e retorne uma nova lista com os elementos na ordem inversa.

def inverter_lista(lista):
    return lista[::-1]

# Exemplo
print(inverter_lista([1, 2, 3, 4]))  # Saída: [4, 3, 2, 1]


4.Ordenação parcial:
Escreva uma função que receba uma lista de números como entrada e retorne uma nova lista contendo os números pares ordenados e os ímpares na mesma ordem original.

def ordenar_pares(lista):
    pares_ordenados = sorted([x for x in lista if x % 2 == 0])
    resultado = []
    indice_par = 0
    for num in lista:
        if num % 2 == 0:
            resultado.append(pares_ordenados[indice_par])
            indice_par += 1
        else:
            resultado.append(num)
    return resultado

# Exemplo
print(ordenar_pares([5, 4, 2, 7, 6]))  # Saída: [5, 2, 4, 7, 6]


5.Soma de elementos consecutivos:
Escreva uma função que receba uma lista de números e retorne uma nova lista contendo a soma de cada par de elementos consecutivos da lista original.

def soma_consecutivos(lista):
    return [lista[i] + lista[i + 1] for i in range(len(lista) - 1)]

# Exemplo
print(soma_consecutivos([1, 2, 3, 4]))  # Saída: [3, 5, 7]



Mini-Projeto: Operações com Listas


def media_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def remover_duplicatas(lista):
    nova_lista = []
    for item in lista:
        if item not in nova_lista:
            nova_lista.append(item)
    return nova_lista

def inverter_lista(lista):
    return lista[::-1]

def ordenar_pares(lista):
    pares_ordenados = sorted([x for x in lista if x % 2 == 0])
    resultado = []
    indice_par = 0
    for num in lista:
        if num % 2 == 0:
            resultado.append(pares_ordenados[indice_par])
            indice_par += 1
        else:
            resultado.append(num)
    return resultado

def soma_consecutivos(lista):
    return [lista[i] + lista[i + 1] for i in range(len(lista) - 1)]

def converter_entrada(entrada):
    return list(map(int, entrada.strip().split()))

def menu():
    while True:
        print("\n=== MENU: Operações com Listas ===")
        print("1. Calcular média da lista")
        print("2. Remover duplicatas")
        print("3. Inverter a lista")
        print("4. Ordenar números pares (ímpares mantêm a ordem)")
        print("5. Somar elementos consecutivos")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo do programa. Até mais!")
            break

        entrada = input("Digite os números da lista, separados por espaço: ")
        lista = converter_entrada(entrada)

        if opcao == "1":
            print("Média da lista:", media_lista(lista))
        elif opcao == "2":
            print("Lista sem duplicatas:", remover_duplicatas(lista))
        elif opcao == "3":
            print("Lista invertida:", inverter_lista(lista))
        elif opcao == "4":
            print("Pares ordenados, ímpares mantidos:", ordenar_pares(lista))
        elif opcao == "5":
            print("Soma dos elementos consecutivos:", soma_consecutivos(lista))
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
menu()


