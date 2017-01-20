### Semana 2, Exercício 7

# Bibliotecas
import math


#Pede os Xs e Ys
x1 = int(input("Digite o x do primeiro ponto: "))
y1 = int(input("Digite o y do primeiro ponto: "))
x2 = int(input("Digite o x do segundo ponto: "))
y2 = int(input("Digite o y do segundo ponto: "))

#Calculando a distância Cartesiana entre os pontos
distX = x1 - x2
distY = y1 - y2

Hipotenusa = math.sqrt( distX**2  +  distY**2 )


if Hipotenusa >=10:
	print("longe")
else:
	print("perto")