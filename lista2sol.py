#Segunda lista de exercícios
import math

# 1
nome = input("Nome do usuário?")
print ("nome do usuário é ", nome)

# 2
nome = input("Nome do usuário?")
idade = int(input("Idade do usuário?"))
print ("nome do usuário é ", nome, " e sua idade é ", idade)

# 3
nome = input("Nome do usuário?")
print ("nome do usuário é ", nome)
altura = float(input("Altura do usuário?"))
print ("altura do usuário é ", altura)

print("obrigado!")

# 4
rua = input("nome da rua?")
num = int(input("número?"))
comp = int(input("complemento?"))
cep = input("cep?")

'''
observação:
poderiamos fazer algum teste de verificação para saber
se o numero do CEP esta ok...
por exemplo, poderiamos testar a quantidade de digitos fornecidos...
'''

if len(cep)< 8:
    print("numero de cep com poucos digitos...")
else:
    print("rua ",rua,", ",num,"sala/ap ",comp)
    print("cep: ",cep)

# 5
n1 = int(input("numero 1:"))
n2 = int(input("numero 2:"))
n3 = int(input("numero 3:"))
n4 = int(input("numero 4:"))
n5 = int(input("numero 5:"))

print("somatório = ",n1+n2+n3+n4+n5)
print("produtório = ",n1*n2*n3*n4*n5)

# 6
a = int(input("numero a:"))
b = int(input("numero b:"))
c = int(input("numero c:"))
d = int(input("numero d:"))
e = int(input("numero e:"))

areaTriangulo = (b * c)  / 2
perim = a + b + c + d
areaCirculo = math.pi * e**2

print("area triangulo ",areaTriangulo)
print("perimetro retangulo ",perim)
print("area circulo ", areaCirculo)

# 7
nota1 = float(input("nota1:"))
nota2 = float(input("nota2:"))
nota3 = float(input("nota3:"))

print("nota final = ",nota1*0.1 + nota2*0.6 + nota3*0.3)

# 8
ga_pra = float(input("GA pratica:"))
ga_teo = float(input("GA teorica:"))

gb_lab = float(input("GB prova lab:"))
gb_teo = float(input("GB teste teorico:"))
gb_extra = float(input("GB extraclasse:"))

print("nota final = ",0.33*(0.45*ga_pra+0.55*ga_teo)+0.67*(0.6*gb_lab+0.2*gb_teo+0.2*gb_extra))

