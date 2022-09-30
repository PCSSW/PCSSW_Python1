#Exercício 4 - Lista 10

nome = input("Digite o nome da pessoa: ")
anoN = int(input("Digite o ano de nascimento: "))
anoA = 2022

nome = nome.title()
x = anoA - anoN

if x >= 16:
	print("{0} tem idade para votar".format(nome))

else:
	print("{0} não tem idade para votar".format(nome))
	
print("{0} tem {1} anos".format(nome,x))
