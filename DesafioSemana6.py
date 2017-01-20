### Desafio semana 6

# Programa que receba uma sequencia do usuário e pra cada número, faça o fatorial

def fatorial(num):
	fat = 1

	while num > 1:
		fat = fat * num
		num = num -1

	return print(fat)



num = int(input("Digite um número inteiro e positivo: "))

while num >= 0:
	fatorial(num)
	num = int(input("Digite um número inteiro e positivo: "))