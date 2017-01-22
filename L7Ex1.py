# Lista 7 Exercício 1

# Escreva uma função imprime_matriz(matriz), que recebe uma matriz
# como parâmetro e imprime a matriz, linha por linha. Note que NÃO
# se deve imprimir espaços após o último elemento de cada linha!



#def imprime_matriz2(matriz):
#	for linha in matriz:
#	    for num in linha:
#	    	print(num, end=" ")
#	    print("", end="\n")
#	return ""


def imprime_matriz(matriz):
	i=0
	while i < len(matriz):
		j=0
		while j < len(matriz[i]):
			linha = matriz[i]
			print(linha[j], end="")
			j = j + 1
			if j < (len(matriz[i])):
				print(" ", end="")
		i = i + 1
		if i < (len(matriz)):
			print("")
	return ""

mat = [1,2],[3,4],[5,6]
mat2 = [[1, 2, 3], [4, 5, 6]]
mat3 = [[1], [2], [3]]

test1 = [[1], [2]]
test2 = [[1, 2], [3, 4]]
test3 = [[1, 2, 7], [3, 4, 8], [1, 2, 3]]


#print(imprime_matriz(test2), end="")
#print(len(mat))