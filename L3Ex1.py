### Ex1. Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.


num = int(input("Digite o valor de n: "))

if num == 0:
	print("1")
else:

	multiplicador = num


	while num != 1:
		multiplicador = multiplicador * (num - 1)
		num = num - 1


	print(multiplicador)	