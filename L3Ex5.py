### Ex.5 Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
### Se o número for primo, imprima "primo". Caso contrário, imprima "nao primo".


num = int(input("Digite um número inteiro: "))


divisivel = False

i = num - 1
sobra = 0
numMenor = num - 1



if num == 1:
	print("nao primo")
else:	
	while i != 1 and not divisivel:
		sobra = num % numMenor
		if sobra == 0:
			divisivel = True
		numMenor = numMenor - 1
		i = i - 1
	
	
	if divisivel:
		print("nao primo")
	else:
		print("primo")