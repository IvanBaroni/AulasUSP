### Desafio semana 6

# Dado um número inteiro n, n>1, imprimir sua decomposição em fatores primos, 
#  indicando também a multiplicidade de cada fator

n = int(input("Digite um número inteiro maior que 1"))

fator = 2
multiplicidade = 0

while n > 1
	while n % fator ==0:
		multiplicidade = multiplicidade + 1
		n = n / fator
	print("fator ", fator, "multiplicidade = ", multiplicidade)
	fator = fator + 1