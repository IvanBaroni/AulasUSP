 #Lista 6 Exercício 4

# Escreva a função remove_repetidos que recebe como parâmetro uma lista
# com números inteiros, verifica se tal lista possui elementos repetidos
# e os remove. A função deve retornar uma lista correspondente à primeira
# lista, sem elementos repetidos. A lista retornada deve estar ordenada.


def tira_repetidos(lista):
	for i in lista:
		if i not in semRepetLis:
			semRepetLis.append(i)
	return semRepetLis


def menor_elemento(lista):
	min = 99999999999
	for i in lista:
		if min > i:
			min = i
	return min


def ordena_lista(lista):
	i = 0
	limite = len(lista)
	while i < limite:
		menor = menor_elemento(lista)
		ordenadaLis.append(menor)
		lista.remove(menor)
		i = i + 1
	return ordenadaLis



def remove_repetidos(lista):
	return ordena_lista(tira_repetidos(lista))



lis = [3, 1, 1, 2, 1, 3, 1]
semRepetLis = []
ordenadaLis = []


#print(lis)
#print(tira_repetidos(lis))
#print(remove_repetidos(lis))