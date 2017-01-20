### Ex2. Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais. 


num = int(input("Digite o valor de n: "))

i=0
impar = -1

while i != num:
	impar = impar + 2
	i = i + 1
	print(impar)	