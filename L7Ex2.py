# Lista 7 Exercício 2

# Escreva uma função dimensoes(matriz) que recebe uma matriz como
# parâmetro e imprime as dimensões da matrix recebida, no formato iXj.



def dimensoes(matriz):
	j = 0
	i = 0
	for linha in matriz:
		i = i + 1
	for num in linha:
		j = j + 1
	print("{}X{}".format(i,j), end="")
	return


mat = [1,2],[3,4],[5,6]
mat2 = [[1, 2, 3], [4, 5, 6]]
mat3 = [[1], [2], [3]]


#print(dimensoes(mat))
#print(dimensoes(mat2))
#print(dimensoes(mat3))