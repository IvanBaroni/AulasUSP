# Lista 5 Exercício 1

# Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros
# correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir
# uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.


largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

x = largura

while altura > 0:
	while largura > 0:
		print ("#", end ="")
		largura = largura - 1
	altura = altura - 1
	print()
	largura = x
