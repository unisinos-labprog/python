#Primeira Lista
import math

# 1 ------------------------------------------------------
print ("Alô mundo!")

# 2 ------------------------------------------------------
num1 = int(input("Qual o primeiro número?"))
num2 = int(input("Qual o segundo número?"))

print("a soma de ",num1," e ",num2," é ", num1 + num2)
print("o produto de ",num1," e ",num2," é ", num1 * num2)

# 3 ------------------------------------------------------
saldoInicial = float(input("Saldo inicial?"))           
receita = float(input("Receita?"))
despesa = float(input("Despesa?"))

print("Saldo Final é de ", saldoInicial + receita - despesa)

# 4 ------------------------------------------------------
valor = int(input("Qual o valor?"))
print("a raiz quadrada de ",valor," é ", math.sqrt(valor))

# 5 ------------------------------------------------------
raio = float(input("Qual o raio?"))
altura = float(input("Qual a altura?"))

print("Volume é ", math.pi * raio**2 * altura)

# 6 ------------------------------------------------------
a = int(input("Qual o valor de A?"))
b = int(input("Qual o valor de B?"))

temp = a
a = b
b = temp

print("O valor de A é", a)
print("O valor de B é", b)

# 7 ------------------------------------------------------
tempC = float(input("Qual o temperatura (em Celsius)?"))
print("Temperatura em Fahrenheit = ", (9*tempC+160)/5)

# 8 ------------------------------------------------------
notaGA = float(input("Qual a nota do GA?"))
notaGB = float(input("Qual a nota do GB?"))

print("A média é ", (notaGA+2*notaGB)/3)









