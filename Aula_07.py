#Exercício 5 - Lista 10

'''senha = input("Digite a senha: ")

if senha == "1234":
	print("ACESSO PERMITIDO")
	
else:
	print("ACESSO NEGADO")'''
	
senha = input("Digite a senha: ")

while senha != "1234":
	print("ACESSO NEGADO")
	print("\nPor favor digite sua senha novamente: ")
	senha = input("Digite a senha: ")
	if senha == "1234":
		break
print("ACESSO PERMITIDO")
