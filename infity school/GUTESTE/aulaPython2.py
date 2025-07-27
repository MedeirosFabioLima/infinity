#ATIVIDADE PRÁTICA 1

#Crie um conjunto vazio chamado frutas e adicione as
#seguintes frutas a ele: "maçã", "banana", "uva", "laranja"
#e "morango". Em seguida, imprima o conjunto. morango". Em seguida, imprima o conjunto.


frutas = set()
frutas.add("Maçã")
frutas.add("Uva")
frutas.add("Laranja")
frutas.add("banana")
print(frutas)


#ATIVIDADE PRÁTICA 2 

#Verifique se a fruta "banana" está presente no conjuntofrutas e imprima o resultado.

if 'banana' in frutas:
    print("A fruta banana está no conjunto de frutas")


#ATIVIDADE PRÁTICA 3

#Crie um conjunto chamado frutas_vermelhas e adicioneas seguintes frutas a ele:"morango", "cereja" e "framboesa". Em #seguida, imprima o conjunto.

frutas_vermelhas = set()
novas_frutas = {"Morango","Cereja","Framboesa"}
frutas_vermelhas.update(novas_frutas)
print(frutas_vermelhas)


#ATIVIDADE PRÁTICA 4

#Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.

frutas_vermelhas.remove("Cereja")
print(frutas_vermelhas)



#ATIVIDADE PRÁTICA 5

#Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.



#ATIVIDADE PRÁTICA 6

#Crie um programa que recebe dois conjuntos e exibe a interseção deles.



#ATIVIDADE PRÁTICA 7

#Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.




#ATIVIDADE PRÁTICA 8

#Escreva um programa que EXIBA um dicionário contendoinformações de pessoas (nome, idade) e exiba essas informações.



#ATIVIDADE PRÁTICA 9

#Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.




#ATIVIDADE PRÁTICA 10

#Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o valor ao #dicionário, atualizando o valor se a chave já existir.


#ATIVIDADE PRÁTICA 11

#Escreva um programa que recebe um dicionário e uma lista de chaves como entrada e verifica se todas as chaves da lista #existem no dicionário. A função deve retornar True se todas as chaves existirem e False casocontrário.


#ATIVIDADE PRÁTICA 12

#Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção. Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.



#ATIVIDADE PRÁTICA 13

#Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.




#ATIVIDADE PRÁTICA 14

#Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em seguida, exiba a lista original e a lista sem duplicatas.



#ATIVIDADE PRÁTICA 15

#Crie um programa que realize a união de múltiplos conjuntos e exiba o conjunto resultante.





#DESAFIO PRÁTICO

#Sistema de Cadastro de Alunos - passo 1

#Cadastro de Alunos: O programa deve permitir ao usuário
#cadastrar alunos. Cada aluno terá as seguintes
#informações: nome, idade e notas em três disciplinas:
#Matemática, Ciências e História. Os dados de cada aluno
#devem ser armazenados em um dicionário com as
#seguintes chaves:'nome', 'idade', 'notas'. 'notas'. As notas devem
#ser armazenadas em uma tupla.




#DESAFIO PRÁTICO

#Sistema de Cadastro de Alunos - passo 2

#Visualização de Alunos: O programa deve permitir ao usuário
#visualizar todos os alunos cadastrados, exibindo suas informações
#de forma organizada.
#Média de Notas: O programa deve calcular a média das
#notas de cada aluno e exibi-la.
#Aluno com Melhor Média: O programa deve identificar e
#exibir o aluno com a melhor média de notas.



