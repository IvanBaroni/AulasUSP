### Lista 4 Ex4

# Reescreva a função 'maximo' do exercício 2, que devolve o maior valor dentre dois inteiros recebidos,
# para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.


def maximoDois(a,b):
	if a > b:
		return a
	else:
		return b


def maximo(a,b,c):
	ab = maximoDois(a,b)
	return maximoDois(ab,c)


#b = int(input("Digie b: "))
#c = int(input("Digie b: "))

#print(maximo(a,b,c))