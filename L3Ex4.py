### Ex.4  Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido pussui ao
### menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim". Se não existir, imprima "nao".


num = int(input("Digite o número: "))


N = len(str(num))

if N == 1:
	print("nao")


else: 

	i = 0

	repetido = False


	while i != N and not repetido:
		digitoA = (num % 10)    # Esquerda 1
		num = (num // 10)         # Define o número sem o esquerda 1
		digitoB = (num % 10)    # Esquerda 1 de novo, mas com o número já mudado

		if digitoA == digitoB:
			repetido = True
		else:
			i = 1 + i


	if repetido:
		print("sim")
	else:
		print("nao")
