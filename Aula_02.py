#Exercício 2 - Lista 7

a = int(input("Digite um número inteiro qualquer: "))
b = int(input("Digite outro número inteiro qualquer: "))

if a % b == 0:
	print("{0} é divisível por {1}".format(a,b))
else:
	print("{0} não é divisível por {1}".format(a,b))
		
