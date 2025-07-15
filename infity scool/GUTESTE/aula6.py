# Revisão de Variáveis

# ATIVIDADE PRÁTICA

# Conversão de Unidades:
# Crie um programa que converta metros para centímetros.
# Peça ao usuário para digitar um valor em metros, armazene
# em uma variável e converta para centímetros.

# # Solicita ao usuário um valor em metros
# metros = float(input("Digite o valor em metros: "))

# # Converte metros para centímetros (1 metro = 100 centímetros)
# centimetros = metros * 100

# # Exibe o resultado
# print(f"{metros} metros equivalem a {centimetros} centímetros.")




# Cálculo de Área:
# Crie um programa que calcule a área de um retângulo.
# Peça ao usuário para digitar a largura e a altura,
# armazene em variáveis e calcule a área.

# # Solicita ao usuário a largura do retângulo
# largura = float(input("Digite a largura do retângulo (em metros): "))

# # Solicita ao usuário a altura do retângulo
# altura = float(input("Digite a altura do retângulo (em metros): "))

# # Calcula a área do retângulo (fórmula: largura × altura)
# area = largura * altura

# # Exibe o resultado
# print(f"A área do retângulo é {area:.2f} metros quadrados.")




# ATIVIDADE PRÁTICA

# Cálculo de IMC:
# Crie um programa que calcule o Índice de Massa Corporal (IMC).
# Peça ao usuário para digitar seu peso e altura, armazene em
# variáveis e calcule o IMC.

# # Solicita o peso e a altura do usuário
# peso = float(input("Digite seu peso em kg: "))
# altura = float(input("Digite sua altura em metros: "))

# # Calcula o IMC (fórmula: peso / altura²)
# imc = peso / (altura ** 2)

# # Exibe o resultado com duas casas decimais
# print(f"Seu IMC é: {imc:.2f}")


# Cálculo de Juros Simples:
# Crie um programa que calcule o valor futuro de um investimento
# usando a fórmula de juros simples. Peça ao usuário para digitar o
# capital inicial, a taxa de juros e o tempo de aplicação.

# # Solicita os dados ao usuário
# capital = float(input("Digite o capital inicial (R$): "))
# taxa = float(input("Digite a taxa de juros (% ao mês ou ano): "))
# tempo = float(input("Digite o tempo da aplicação (meses ou anos): "))

# # Calcula o montante usando a fórmula de juros simples
# # Fórmula: M = C * (1 + i * t)
# montante = capital * (1 + (taxa / 100) * tempo)

# # Exibe o valor final
# print(f"O valor futuro do investimento é: R$ {montante:.2f}")




# Revisão de Algoritmo

# ATIVIDADE PRÁTICA

# Verificando a Média do Aluno:
# Crie um algoritmo que peça quatro notas de um aluno, calcule a
# média e exiba se o aluno foi aprovado ou reprovado (média >= 6).


# # Solicita as quatro notas do aluno
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# nota4 = float(input("Digite a quarta nota: "))

# # Calcula a média das notas
# media = (nota1 + nota2 + nota3 + nota4) / 4

# # Exibe a média e o resultado
# print(f"Média: {media:.2f}")

# if media >= 6:
#     print("Aluno aprovado!")
# else:
#     print("Aluno reprovado.")


# Algoritmo de Cálculo de Desconto:
# Desenvolva um algoritmo que calcule o preço de um produto
# após aplicar um desconto. Solicite o preço original e o percentual
# de desconto.

# # Solicita o preço original do produto
# preco_original = float(input("Digite o preço original do produto (R$): "))

# # Solicita o percentual de desconto
# desconto_percentual = float(input("Digite o percentual de desconto (%): "))

# # Calcula o valor do desconto
# valor_desconto = preco_original * (desconto_percentual / 100)

# # Calcula o preço final com o desconto aplicado
# preco_final = preco_original - valor_desconto

# # Exibe os resultados
# print(f"Desconto: R$ {valor_desconto:.2f}")
# print(f"Preço com desconto: R$ {preco_final:.2f}")



# ATIVIDADE PRÁTICA

# Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.

# # Entrada do usuário
# segundos_total = int(input("Digite o total de segundos: "))

# # Cálculos
# horas = segundos_total // 3600
# resto = segundos_total % 3600
# minutos = resto // 60
# segundos = resto % 60

# # Saída formatada
# print(f"O tempo convertido é: {horas} hora(s), {minutos} minuto(s), {segundos} segundo(s).")


# Algoritmo de Conversão de Temperatura:
# Crie um algoritmo que converta uma temperatura de Celsius
# para Fahrenheit. Solicite ao usuário a temperatura em Celsius
# e exiba o resultado em Fahrenheit.

# # Entrada
# celsius = float(input("Digite a temperatura em Celsius: "))

# # Cálculo
# fahrenheit = (celsius * 9 / 5) + 32

# # Saída
# print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")




# Revisão de Condicionais

# ATIVIDADE PRÁTICA

# Categoria de Idade:
# Desenvolva um programa que peça a idade do usuário e
# informe se ele é criança, adolescente, adulto ou idoso.

# Programa para classificar a idade

# # Solicita a idade do usuário
# idade = int(input("Digite sua idade: "))

# # Verifica a categoria de idade
# if idade < 12:
#     print("Você é uma criança.")
# elif idade < 18:
#     print("Você é um adolescente.")
# elif idade < 60:
#     print("Você é um adulto.")
# else:
#     print("Você é um idoso.")


# Classificação de Notas:
# Crie um programa que solicite uma nota de 0 a 100
# e informe o conceito (A, B, C, D, F) com base na nota.

# Solicita a nota ao usuário
nota = int(input("Digite a nota (0 a 100): "))

# Verifica o conceito com base na nota
if nota >= 90 and nota <= 100:
    print("Conceito: A")
elif nota >= 80:
    print("Conceito: B")
elif nota >= 70:
    print("Conceito: C")
elif nota >= 60:
    print("Conceito: D")
elif nota >= 0:
    print("Conceito: F")
else:
    print("Nota inválida. Digite um valor entre 0 e 100.")




# ATIVIDADE PRÁTICA

# Verificar Signo:
# Escreva um programa que peça o dia e o mês de
# nascimento do usuário e informe o signo correspondente.

# Sistema de Login:
# Desenvolva um programa que simule um sistema de login.
# O programa deve pedir o nome de usuário e a senha e verificar
# se correspondem a um usuário pré-cadastrado. Exiba mensagens
# apropriadas para login bem-sucedido ou falha.


# Revisão de Estruturas de Repetição

# ATIVIDADE PRÁTICA

# Contagem Regressiva:
# Desenvolva um programa que use um laço while para exibir uma
# contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

# Contagem Regressiva:
# Desenvolva um programa que use um laço for para exibir uma
# contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".


# ATIVIDADE PRÁTICA

# Soma de Números Pares:
# Crie um programa que use um laço while para somar
# todos os números pares de 1 a 100 e exiba o resultado.

# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).
    

#     ATIVIDADE PRÁTICA

# Verificação de Palíndromo:
# Escreva um programa que solicite uma palavra ao usuário e
# use um laço while para verificar se a palavra é um palíndromo
# (lê-se da mesma forma de trás para frente).

# Sistema de Login com Tentativas Limitadas:
# Desenvolva um programa que simule um sistema de login.
# O programa deve solicitar o nome de usuário e senha até que o
# usuário insira as credenciais corretas ou até que o número máximo
# de tentativas seja atingido. Use um laço while com uma condicional
# para verificar as credenciais e limitar as tentativas.

