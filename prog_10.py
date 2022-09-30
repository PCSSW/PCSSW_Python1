#Exercício 11 - Lista 10

print("Informe o valor dos ângulos do triângulo:")

a1 = int(input())
a2 = int(input())
a3 = int(input())

if a1 == 90 or a2 == 90 or a3 == 90:
	print("Triângulo Retângulo")
elif a1 > 90 or a2 > 90 or a3 > 90:
	print("Triângulo Obtusângulo")
elif a1 < 90 or a2 < 90 or a3 < 90:
	print("Triângulo Acutângulo")
else:
	print("Não é um triângulo")
