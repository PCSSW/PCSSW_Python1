#Exercício 7 - Lista 7

idade = int(input("informe a idade: "))

if idade > 0 and idade <= 11:
	print("Criança")
elif idade <= 14:
	print("Adolescente")
elif idade <= 17:
	print("Jovem")
elif idade <= 59:
	print("Adulto")
else:
	print("Idoso")

