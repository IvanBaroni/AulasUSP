### Confere o número do cartão


meuCartão = int(input("Digite o número de seu cartão de crédito:"))

cartãoLido = 1
encontreiMeuCartãoNaLista = False



while cartãoLido != 0  and not encontreiMeuCartãoNaLista:
	cartãoLido = int(input("Digite o número do próximo cartão de crétido:"))
	if cartãoLido == meuCartão:
		encontreiMeuCartãoNaLista = True


if encontreiMeuCartãoNaLista:
	print("EBA!!! Meu cartão está lá!")
else:
	print("Xi, não ta lá...")