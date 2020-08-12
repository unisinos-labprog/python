#FUNÇÕES MATEMÁTICAS   =================================

'''
#importando todas funcoes de uma vez so:
from math import *

print ("seno=",sin(3.2))    #faz a chamada da funcao so usando o nome dela...
print ("pi:",pi)
'''

#mas se importar deste modo:
import math

#nesse caso tem que usar math na frente das funcoes:
print ("seno=",math.sin(3.2))
print ("pi:",math.pi)



#FORMATAÇÂO DOS DADOS NO PRINT  ===================================

a=6			        #é um int
c=7.36789321		#é um float

#formatacao antiga/classica
print("c=%.2f"%c," .. %.5f"%c,".. %.1f __ %.2f"%(c,c))
print("a= %3d ..."%a)

#formatacao nova
print("valores: a={0:3d} c={1:5.2f} c={1:.4f} a={0:05d}".format(a,c))
#na funcao format se passa as variaveis que se quer mostrar e formatar
#dentro do print, entre chaves fica: {indice da variavel no format:formato}

#EXEMPLOS de FORMATOS:
#2d   inteiro(d) com duas casas (colunas na tela)
#04d  inteiro(d) com 4 casas e preenchendo colunas a esquerda com zeros
#5.2f float(f) com 5 casas no total sendo 2 (das 5) na parte fracionaria
#.4f  float(f) 4 casas na parte fracionaria

# tabulando (inserindo TABS com \t) e novalinha com \n
print("\tabcdefgh\n\n")

print("sem nova linha", end="")
print(" isso sai na mesma linha do print anterior")



#FUNÇÕES PARA SORTEIO   ================================
import random

print ("rand=",random.random())      #sorteia valor float entre 0.0 e 0.9999999
print ("rand=",random.randint(2,5))  #sorteia valor int entre 2 e 5



#FUNÇÕES DE DATA    ====================================
import datetime

hoje = datetime.date.today()

print("hoje=",hoje)
print("hoje=",hoje.month)
print("hoje=",hoje.year)
print("hoje=",hoje.day)
print("weekday=",hoje.weekday())  #retorna 0 para segunda, 1 para terça, 2 para quarta, etc...

import time

print("hora:",time.localtime().tm_hour)
print("min:",time.localtime().tm_min)
print("seg:",time.localtime().tm_sec)




#FUNÇÕES DE STRING   ===================================

s = "internacional"
print(s)
print(s[0])       #primeira letra e' a de indice/posicao  zero
print(s[1])       #segunda letra e' a de indice/posicao  um
print(s[2])
print (s[2:5])    # mostra a substring, do índice 2 ao 5 (exclusivo) => 'ter'

car = 'a'
car += 'b'        # CONCATENA, JUNTA 'b' na string car
print("car = ", car)

print("comprimento da string s = ", len(s))

print("str=%20s"%s)               # insere espaços a esquerda ate completar 20 posicoes
print("str=%-20s"%s,".")          # insere espaços a direita ate completar 20 posicoes

print("str=%-20s"%s.upper(),".")  # insere espaços a direita ate completar 20 posicoes
			                            # s.upper() retorna string em MAIÚSCULAS

nome = "teste"
if nome.lower() == "teste":     # nome.lower() retorna string em minúsculas
   print("nome é teste.")

ss = s + "ee"                  # concatena "ee" numa copia da string s e atribui o resultado a string ss
ss += "x"                      # concatena "x" a string ss

a = "oi.sd"
x = a.replace(".",",")       # troca (substitui)  caracteres . por ,
print("x=",x)                # imprime oi,sd

valor = 7.3456
texto = "valor="  + str(valor)       # a função str converte o parâmetro para string
print(texto)


