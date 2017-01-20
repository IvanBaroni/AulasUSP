# Lista 5 Exercício 2

# Escreva uma função 'soma_hipotenusas' que receba como parâmetro um número inteiro 
# positivo e retorna a soma de todos os inteiros entre 1 e n que são comprimento da 
# hipotenusa de alum triângulo retângulo com catetos inteiros.

import math

def hip(ca,cb):
	return math.sqrt(ca**2 + cb**2)

def soma_hipotenusas(x):
	ca = x
	cb = x

	soma = 0

	while cb > 0:
		while ca > 0:
			if hip(ca,cb) % 1 == 0:
				# print (ca, cb, "--->", hip(ca,cb))
				if hip(ca,cb) <= x:
					soma = soma + hip(ca,cb)
			ca = ca - 1
		cb = cb - 1
		ca = x

	return (soma/2)


x = int(input("digite um número inteiro positivo: "))

print (soma_hipotenusas(x))
