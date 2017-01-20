### Bháskara usando chamada de funções.

# Bibliotecas
import math


def delta(a, b, c):
	return b**2 - 4*a*c


def main():
	a = int(input("Digite o valor do termo A: "))
	b = int(input("Digite o valor do termo B: "))
	c = int(input("Digite o valor do termo C: "))
	imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):
	d = delta(a, b, c)

	# Devolve com todos os possíveis casos
	if d < 0:
		print("---> Não existem raízes reais...")
	else:
		if d == 0:
			raiz1 = (-b + math.sqrt(d)) / (2*a)
			print ("A raiz dupla é: ", raiz1)
			print("---> Apenas uma raiz dupla")
		else:
			raiz1 = (-b + math.sqrt(d)) / (2*a)
			raiz2 = (-b - math.sqrt(d)) / (2*a)
			print ("A primeira raiz é: ", raiz1)
			print ("A seunda raiz é: ", raiz2)
			print("---> Duas raízes reais")


main()