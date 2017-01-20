### Testar se o número tem dois dígitos adjacentes iguais


num = int(input("Digite o número: "))



N = len(str(num))
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
	print("É... tem número adjacente repetido ae")
else:
	print("Ta de boa. Não tem num adj repetido")



