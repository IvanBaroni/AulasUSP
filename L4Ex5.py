### Lista 4 Ex5

# Escreva a função vogal que recebe um único caractere como parâmetro e retorna True
# se ele for uma vogal e False se for uma consoante.


def vogal(l):

	vog = False

	if (l == "a" or l == "e" or l == "i" or l == "o" or l == "u" or 
		l == "A" or l == "E" or l == "I" or l == "O" or l == "U") :
		vog = True
	
	return vog


#l = input("Digie a letra: ")
#print(vogal(l))