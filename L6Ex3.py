 #Lista 6 Exercício 3

# Escreva a função maior_elemento que recebe como parâmetro uma lista 
# com números inteiros e retorna um número inteiro correspondente ao
# maior valor presente na lista recebida.


def maior_elemento(lista):
	max = -99999999
	for i in lista:
		if max < i:
			max = i
	return max


#lis = [99999999, 2000, 10, 1000, 2500]
#print(maior_elemento(lis))
