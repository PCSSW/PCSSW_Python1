#Exercício 8 - Lista 10

nlados = int(input("Informe o número de lados do polígono: "))

if nlados < 3:
	print("Não é um polígono")
elif nlados == 3:
	print("Triângulo")
	b = float(input("Digite a medida da base do triângulo:"))
	h = float(input("Digite a medida da altura do triângulo:"))
	area = (b * h)/2
	print("A área do triângulo é: {0}".format(area))
elif nlados == 4:
	print("Quadrilátero")
elif nlados == 5:
	print("Pentágono")
elif nlados == 6:
	print("Hexágono")
else:
	print("Polígono não identificado")
