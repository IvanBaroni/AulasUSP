# Lista 7 Exercício 3

# Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes 
# e retorna uma matriz que represente sua soma caso as matrizes
# tenham dimensões iguais. Caso contrário, a função retorna False.

def dim(matriz):
	j = 0
	i = 0
	for linha in matriz:
		i = i + 1
	for num in linha:
		j = j + 1
	return "{}X{}".format(i,j)

def soma_lista(l1,l2):
	lisSoma=[]
	i = 0
	while i < len(l1):
		lisSoma.append(l1[i]+l2[i])
		i = i + 1
	return lisSoma

def soma_matrizes(m1, m2):
	if dim(m1) != dim(m2):
		return False
	else:
		matSoma=[]
		j = 0
		while j < len(m1):
			matSoma.append(soma_lista(m1[j],m2[j]))
			j = j + 1
	return matSoma

mat1a = [1,2],[3,4],[5,6]
mat2a = [[1, 2, 3], [4, 5, 6]]
mat3a = [[1], [2], [3]]

mat1b = [6,5],[4,3],[2,1]
mat2b = [[6, 5, 4], [3, 2, 1]]
mat3b = [[3], [2], [1]]

#print(mat1a[0])

print(soma_matrizes(mat3a,mat3b))