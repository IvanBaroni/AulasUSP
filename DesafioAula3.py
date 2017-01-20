### somar todos os dígitos de um numero inteiro

num = int(input("Digite o número: "))

N = len(str(num))
soma = 0

i = 0

while i != N:
	soma = (num % 10) + soma
	num = (num // 10)
	i = 1 + i


print(soma)
