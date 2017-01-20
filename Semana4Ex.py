### Programa pra testar se a sequência está em ordem decrescente


decrescente = True
anterior = int(input("Digite o primeiro número da sequência:  "))

valor = 1

while valor !=0 and decrescente:     # decrescente=true
	valor = int(input("Digite o próximo número da sequência:  "))
	if valor > anterior:
		decrescente = False
	anterior = valor

if decrescente:
	print("A sequência está em ordem decrescente!")
else:
	print("A sequência não está em ordem decrescente!")