import time

valor = -3
print("valor absoluto:", abs(valor))

time.sleep(5)  #execução para por 5 segundos

valor = 127
print("valor em hexadecimal:", hex(valor))
print("valor em binario:", bin(valor))
time.sleep(2)  #execução para por 5 segundos

a1 =2 
a2 = 5
menor = min(a1,a2)
menor = min(45,3,78,9,13)
maior = max(45,3,78,9,13)
print("menor:", menor," maior:", maior)

valor = 3.8
print("valor arredondado:", round(valor))  #arredonda para o inteiro + proximo

#para arredondar para baixo, deve-se empregar a função floor do modulo math
#neste caso, deve-se importar este modulo para fazer uso desta função...
import math
print("valor arredondado para baixo:", math.floor(valor))
print("valor arredondado para cima:", math.ceil(valor))  #arredonda p/ cima

#conversoes de tipo

val =  23.78   #val e´ do tipo float , isto e´, um numero real
valInt = int(val)  #carrega em valInt um inteiro (sem parte fracionaria) de val
valString = "os valores sao: " + str(val) + " e " + str(valInt)

print(valString)

valorNumaString = "45.33"
valor = float(valorNumaString)  #converte a string num float e atribui a valor
print (valor + 1000)  #agora e´ possivel fazer calculos com o valor

#testando o tipo de uma variavel:
x = isinstance(valor, float)  #isinstance verifica se valor é um float; retorna um booleano (True ou False)
print(x)
print(type(valString))  #função type retorna o tipo da variável


if isinstance(valString, str):
  print("valString é uma string...")



import replit

replit.clear() #limpa a tela do console repl.it

print("fim.")