### Lista 4 Ex3

# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como
# parâmetro e retorna o maior número primo menor ou igual ao número passado à função


def maior_primo(N):
	i = N
	while N >= 2:
		if	testaSePrimo(N):
			return N
		N = N-1



def testaSePrimo(num):         
	if num < 2:
		return "não primo"
	else:

		i = num - 1                
		divisivel = False

		while i > 1 and not divisivel:  
			if (num % i) == 0:           
				divisivel = True
			i = i - 1                    

		if divisivel:
			return False
		else:
			return True



# num = int(input("Digite um número inteiro: "))

# print(maior_primo(num))