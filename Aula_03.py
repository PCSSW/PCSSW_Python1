#Exercício 3 - Lista 7

total = float(input("Informe o total arrecadado: "))

Pc = total * 0.46
Sc = total * 0.32
Tc = total - (Pc + Sc)

print("O primeiro colocado receberá: R${0}".format(Pc))
print("O segundo colocado receberá: R${0}".format(Sc))
print("O terceiro colocado receberá: R${0}".format(Tc))
		
