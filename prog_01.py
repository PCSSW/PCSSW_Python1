#Exercício 1 - Lista 7

a = int(input("Digite um número inteiro qualquer: "))
b = int(input("Digite outro número inteiro qualquer: "))

if a > b:
	print("{0} é  maior que {1}".format(a,b))
elif b > a:
	print("{0} é maior que {1}".format(b,a))
else:
	print("{0} e {1} são iguais".format(a,b))
		
