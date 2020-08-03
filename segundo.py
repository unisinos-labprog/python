import math


#dados da primeira pessoa
pessoa = input("nome:")
idade = float(input("idade:"))

print ("nome:",pessoa)
print ("idade:",idade)

#dados da segunda pessoa
pessoa2 = input("nome:")
idade2 = float(input("idade:"))

print ("nome:",pessoa2)
print ("idade:",idade2)

mediaIdades = (idade + idade2)/2

print("media das idades = ",mediaIdades)

if mediaIdades > 50:
  print("media acima de 50...")
  print("é uma média alta...")
elif mediaIdades == 20 or idade2 <=10:
  #print("media abaixo ou igual a 50")
  #if mediaIdades == 20:
    print("media=20")

valor = 13
valModulo = valor % 2
if valModulo == 0:
  print("valor ",valor, "é par.")
else:
  print("valor ",valor, "é ímpar.")

potencia = 2 ** 5
print("2 elevado a 5 é ",potencia)

raizQ = math.sqrt(25)
print("raiz de 25 é", raizQ)

print("valor de pi:", math.pi)
print("valor de pi:%.5f"% math.pi)
  
print("fim do programa")