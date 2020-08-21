#************UM**************
num = int(input("Digite um número: "))
if num < 0:
  print("NEGATIVO")
elif num > 0:
  print("POSITIVO")
else:
  print("NULO")
#**************************

#************DOIS**************
num = int(input("Digite um número: "))
if num % 2 == 0:
  print("PAR")
else:
  print("IMPAR")
#**************************

#************TRES**************
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
if num1 > num2:
  print("O primeiro número é maior")
elif num1 < num2:
  print("O segundo número é maior")
else:
  print("IGUAIS")
#**************************

#************QUATRO**************
import math
cod = int(input("Digite um código: "))
if cod == 1:
  num1 = int(input("Digite um número: "))
  num2 = int(input("Digite um número: "))
  if num2 != 0:
    print("Resto do primeiro pelo segundo: ",num1 % num2)
  else:
    print("Primeiro dividido por 3:" ,num1/3)
elif cod == 2:
  num = int(input("Digite um número: "))
  if num > 0:
    print("Raiz quadrada:" ,math.sqrt(num))
  elif num < 0:
    print("Número absoluto: ",num)
  else:
    print("ZERO")
elif cod == 3:
  num = float(input("Digite um número real: "))
  print("Quadrado: ", num**2)
else:
  print("CÓDIGO INVÁLIDO")
#**************************

#***********CINCO***************
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = ((nota1*4)+(nota2*2)+(nota3*4))/10
print("A média é ",media)
if(media >= 7):
  print("Você foi aprovado.")
else:
  print("Você foi reprovado.")
#**************************

#************SEIS**************
alt = float(input("Digite sua altura: "))
sexo = int(input("Digite seu sexo: [1 - Masculino][2 - feminino]: "))
if sexo == 1:
  peso = (72.7*alt) - 58
  print("Seu peso ideal é: ",peso,"KG")
elif sexo == 2:
  peso = (62.1*alt) - 44.7
  print("Seu peso ideal é: ",peso,"KG")
else:
  print("Sexo inválido.")
#**************************

#************SETE**************
matricula = int(input("Digite sua matrícula: "))
grauA = float(input("Digite sua nota de Grau A: "))
grauB = float(input("Digite sua nota de Grau B: "))
media = (grauA+(2*grauB))/3
print("Sua média é: ", media)
if media >= 6:
  print(matricula," APROVADO")
else:
  grauC = float(input("Digite sua nota de Grau C: "))
  g = int(input("Digite o grau a ser substituido [1 - Grau A][2 - Grau B]: "))
  if g == 1:
    media = (grauC+(2*grauB))/3
  elif g == 2:
    media = (grauA+(2*grauC))/3
  else:
    print("Grau incorreto")
  print("Sua nova media é: ",media)
  if media >= 6:
    print("Matrícula: ",matricula, " APROVADO.")
  else:
    print("Matrícula: ",matricula, " REPROVADO.")
#**************************

#*************OITO*************
cod = int(input("Digite o seu código: "))
sal = float(input("Digite o seu salário: "))
if sal >= 600.00 and sal < 900.00:
  sal *= 1.13
elif sal >=900.00 and sal < 2000.00:
  sal *= 1.10
elif sal >= 2000.00:
  sal *= 1.06
print("Seu salário final é de: R$",sal)
#**************************

#*************NOVE*************
cod = int(input("Digite o código do produto [10][20][30]: "))
quant = int(input("Digite a quantidade de produtos vendidos: "))
if cod == 10:
  preco = quant * 100.00
elif cod == 20:
  preco = quant * 150.00
elif cod == 30:
  preco = quant * 200.00
else:
  print("Código incorreto.")
if preco >= 200.00 and preco <= 1000.00:
  desc = preco*0.05
elif preco > 1000.00:
  desc = preco*0.10
else:
  desc = 00.00
print("O preço real foi: R$",preco)
print("O desconto foi: R$",desc)
print("O preço final foi: ",(preco-desc))
#**************************
