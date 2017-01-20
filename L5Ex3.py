# Lista 5 Exercício 3

# Escreva a função n_primos que recebe um número inteiro maior
# ou igual a 2 como parâmetro e devolve a quantidade de números
# primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).


def éPrimo(x):
	fator = 2
	if x == 2:
		return True
	while x % fator != 0 and fator <= x/2:
		fator = fator + 1
	if x % fator == 0:
		return False
	else:
		return True


def n_primos(n):

	somaPrimo = 0

	while n > 1:
		if éPrimo(n):
			somaPrimo = somaPrimo + 1
			#print("n:", n, "---> soma:", somaPrimo)
		n = n-1

	return somaPrimo


n = int(input("Digite um número inteiro:"))

print (n_primos(n))