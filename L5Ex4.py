# Lista 5 Exercício 4

# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, 
# de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

x = largura
y = altura

while altura > 0:
	while largura > 0:
		if altura == 1 or altura == y:
			print ("#", end ="")
		else:
			if largura == 1 or largura == x:
				print ("#", end ="")
			else:
				print (" ", end ="")
		largura = largura - 1
	altura = altura - 1
	print()
	largura = x