# + Adição
# - subtração
# * multiplicação
# / divisão
# % módulo (resto da divisão)
# ** potência (exponenciação)
# // divisão inteira (arredonda para baixo)

# 1º()
# 2º**
# 3º * / // %
# 4º + -

# n1 = int(input('um valor: '))
# n2 = int(input('outro valor: '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# di = n1 // n2
# e = n1 ** n2
# print('A soma vale {}' .format(s))
# print('A multiticação vale {}'. format(m))
# print(' Adivisão vale {:.3f}' . format(d))
# print('A divisão inteira vale {}' . format(di))
# print('A potência vale {}' . format(e))



# 1) Faça um programa que leia um número inteiro e mostre e mostre na tela seu secessor e seu antecessor.

# numero = int(input('Digite um número: '))
# antecessor = numero -1
# sucessor = numero +1
# print('O sucessor {} e o atecessor {}' .format(sucessor, antecessor))


# 2) Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# numero = int(input('Digite um número: '))
# dobro = 2 * numero
# triplo = 3 * numero
# raiz = numero ** (1/2)
# print('O dobro de {} e o triplo {} e a raiz {:.3}' .format (dobro, triplo, raiz))


# 3) Desenvolva um progra que leia as duas notas de um aluno, calcule e mostre a média entre elas.

# nota1 = float(input('Nota 1: '))
# nota2 = float(input('Nota 2: '))
# media = (nota1 + nota2) / 2
# print('A média entre {} e {} é {:.2f}' .format(nota1, nota2, media))


# 4) Desenvolva um programa que leia um valor em metros eo exiba convertido em centímetros e milímetros.

metros = float(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print('O valor {:.1f} metros correspode a {:.1f} centimetros e {:.1f} milimetros'.format( metros , centimetros, milimetros))



