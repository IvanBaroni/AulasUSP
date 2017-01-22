# Lista 7 Exercício 4

# Duas matrizes são multiplicáveis se o número de colunas da primeira é igual
# ao número de linhas da segunda.Escreva a função sao_multiplicaveis(m1, m2)
# que recebe duas matrizes # como parâmetro e retorna True se as matrizes
# forem multiplicavéis e False caso contrário.

def numColunasPri(matriz):
	j = 0
	i = 0
	for linha in matriz:
		i = i + 1
	for num in linha:
		j = j + 1
	return j

def numLinhaSeg(matriz):
	a = 0
	b = 0
	for linha in matriz:
		b = b + 1
	for num in linha:
		a = a + 1
	return b

def sao_multiplicaveis(m1,m2):
	if numColunasPri(m1) == numLinhaSeg(m2):
		return True
	else:
		return False


mat1a = [[3], [2], [1]]
mat1b = [[3, 2, 1]]
mat2a = [[3, 2, 1],[4, 5, 6]]

print(sao_multiplicaveis(mat1a,mat1b))