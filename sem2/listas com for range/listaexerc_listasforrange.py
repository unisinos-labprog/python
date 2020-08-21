#Lista de exercicios: laços e listas
 
#1
listaVog = ["a","e","i","o","u"]
#texto = input("digite um texto")
texto = "colorado"
contaVogais = 0
for cadaLetra in texto:   #cadaLetra -> c
  for vog in listaVog:    #vog -> i
    if cadaLetra == vog:
      contaVogais +=1
      break  #abandona laço interno se achou vogal
print("total de vogais em ",texto,"eh de ",contaVogais)

#2
quantosProds=int(input("Quantos produtos serão adicionados?"))
listaProds=[]
i=0
while i<quantosProds:
  produto=input("Qual produto?")
  listaProds.append(produto)
  i+=1
print(listaProds)

#3
listaNomes=[]
listaEstadoCivil=[]
listaCodigos = ["s","c","d","v"]
i=0
while i<5:
  listaNomes.append(input("Nome?"))
  listaEstadoCivil.append( input("Estado civil (s/c/d/v)?)"))
  i +=1
for cod in listaCodigos:
  i=0
  while i<5:
    if listaEstadoCivil[i]==cod:
      print(listaNomes[i])
    i+=1

#4
i=0
senhaOK = False
while i<6 and not senhaOK:
  senhaOK=True
  #testa comprimento da senha:
  senha=input("digite a senha:")
  if len(senha)<5 or len(senha)>10:
    print("senha com tamanho invalido!")
    senhaOK=False
  #testa se a senha so contem digitos:
  soDigitos=True
  j=0    #  senha = "73a" 012
  while j<len(senha):
    if not senha[j].isdigit(): 
      soDigitos=False
      break
    j+=1
  if not soDigitos:
    print("so digitar digitos!")
    senhaOK=False
  i+=1
if senhaOK:
  print("senha aceita!")
else:
  print("senha recusada!")

#5
joioETrigo = ["joio", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio"]
listaJoio = []
listaTrigo = []
for item in joioETrigo:
  if item == "joio":
    listaJoio.append(item)
  else:
    listaTrigo.append(item)
print("lista joio:",listaJoio)
print("lista trigo:",listaTrigo)

#6
while True:
  quant = int(input("Quantidade de indices?"))
  audienciaCaiu = False
  indiceAnterior = 0
  soma=0
  i=0
  while i<quant:
    indiceAudiencia = float(input("Indice?"))
    soma+=indiceAudiencia
    if indiceAudiencia < indiceAnterior:
      audienciaCaiu = True
    indiceAnterior = indiceAudiencia
    i+=1
  print("Media de audiencia: %.2f"%(soma/quant))
  if audienciaCaiu:
    print("Audiência nem sempre crescente!")
  else:
    print("Audiência sempre crescente!")
  if input("continuar?").lower() == "n":
    break
