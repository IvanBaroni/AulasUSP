 #Lista 6 Exercício 2

# escreva a função soma_elementos que recebe como parâmetro
# uma lista com números inteiros e retorna um número inteiro
# correspondente à soma dos elementos da lista recebida.


def soma_elementos(lista):
	soma = 0
	for i in lista:
		soma = soma + i
	return soma


# a = [1, 2, 10, 1000]
# print(soma_elementos(a))
