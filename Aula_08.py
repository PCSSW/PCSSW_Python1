#Exercício 7 - Lista 10

print("...:Esse programa só possuí polígonos com até 6 lados:...")
print("\n")
nlados = int(input("Informe o número de lados do polígono: "))

if nlados < 3:
	print("Não é um polígono")
elif nlados == 3:
	print("Triângulo")
elif nlados == 4:
	print("Quadrilátero")
elif nlados == 5:
	print("Pentágono")
elif nlados == 6:
	print("Hexágono")
else:
	print("Polígono não identificado")
