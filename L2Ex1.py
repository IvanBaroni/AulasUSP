### Semana 2, Exercício 1

# Bibliotecas
import math

#Pede as parada
a = int(input("Digite o valor do termo A: "))
b = int(input("Digite o valor do termo B: "))
c = int(input("Digite o valor do termo C: "))

delta = b**2 - 4*a*c



# Devolve com todos os possíveis casos
if delta < 0:
	print("esta equação não possui raízes reais")
else:
	if delta == 0:
		raiz1 = (-b + math.sqrt(delta)) / (2*a)
		print ("a raiz desta equação é", raiz1)
	else:
		raiz1 = (-b + math.sqrt(delta)) / (2*a)
		raiz2 = (-b - math.sqrt(delta)) / (2*a)
		if raiz1 < raiz2:    
			# Para exibir as raízes em ordem crescente
			print ("as raízes da equação são", raiz1, "e", raiz2 )
		else:
			print ("as raízes da equação são", raiz2, "e", raiz1 )
