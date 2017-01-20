# Faça programa que vai lendo do teclado uma sequência de números inteiros terminadas
# por zero e quando o usuário digita o zero, ele imprimi essa sequência na ordem inversa.
# Na ordem ao contrário da ordem que o usuário digitou. 


lis = []



while True:
	n = int(input("Digite um número:"))
	if n == 0:
		break
	lis.append(n)



sil = lis[::-1]

#print(len(sil))


i=0

while i < len(sil) :
	print(sil[i])
	i = i + 1

