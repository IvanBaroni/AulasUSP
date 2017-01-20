### Calcular o coeficiente binomial, com função pre definida pra fatorial

n = int(input("Digite n: "))
k = int(input("Digite k: "))

def  fatorial(num):     # Função pra num!
	fat = 1
	while ( num > 1 ):
		fat = fat * num
		num = num - 1
	return fat

bin = fatorial(n) // (fatorial(k) * fatorial(n-k))

print(bin)
