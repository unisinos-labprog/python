#Exemplo de laços com o comando WHILE


i = 0			#neste exemplo, i é a variável de controle do laço
while i < 7:
	print("Valor de i:",i)
	i += 1

	
	
	
op = int(input("Digite 3 para sair:"))
while op != 3:
    print("\nOpção digitada:",op,"\nVocê não saiu.")
    op = int(input("Digite 3 para sair:"))

	
	
	
i = 0
while i < 100:
	print("Valor de i:",i)
	i += 1
	if i == 12:
		break		#comando break causa o abandono do laço

		
		
		
while True:			# True é uma constante que é sempre verdadeira
	op = int(input("Digite 3 para sair:"))
	print("\nOpção digitada:",op)	
	if op == 3:		
		break	
	print("Você não saiu.\n")
print("\nVocê saiu.") 

