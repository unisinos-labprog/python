#Exemplos para as funções ORD, CHR , ISDIGIT, ISALPHA

letra = "a"

x = ord(letra)           #x recebe o valor ASCII do simbolo "a", que e´ 97

outraLetra = chr(x)      #outraLetra recebe o caracter ASCII correspondente ao valor que esta em x

print(outraLetra)        #mostra o caracter  a  no console

if  outraLetra.isdigit():   #testa se o caracter que esta na variavel e' um digito (0,1,2,3,4,5,6,7,8 ou 9)
   print("eh um digito") 

if  outraLetra.isalpha():  #testa se o caracter que esta na variavel e' uma letra (a ou A ate z ou Z)
   print("eh uma letra ou digito") 

if  outraLetra.isspace():  #testa se o caracter que esta na variavel e´ um espaço
   print("eh um espaco") 