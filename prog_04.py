#Exercício 5 - Lista 7

h = float(input("Informe a altura: "))
s = input("Informe o sexo M para masculino e F para feminino: ")
s = s.title()

if s == "M":
	Pm = (72.7 * h) - 58
	print(f"O peso ideal é {Pm}")
elif s == "F":
	Pf = (62.1 * h) - 44.7
	print(f"O peso ideal é {Pf}")
else:
	print("Opção inválida!")
	


