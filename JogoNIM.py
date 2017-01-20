def computador_escolhe_jogada(n, m):
    for i in range(m):
        if (n - (i + 1)) % (m + 1) == 0:
            print("O computador tirou %s peça(s)." % (i + 1))
            if (n - (i + 1)) > 0:
                print("Agora resta(m) %s peça(s) no tabuleiro.\n" % (n - (i + 1))) 
            else:
                print("Fim do jogo! O computador ganhou!\n")
            return i + 1



def usuario_escolhe_jogada(n, m):
    while True:
        jogadas_usuario = int(input("Quantas peças você vai tirar? "))
        if jogadas_usuario > m:
            print("Oops! Jogada inválida! Tente de novo.\n") 
            usuario_escolhe_jogada
        else:    
            if n - jogadas_usuario > 0:
                print("\nVocê tirou %s peça(s)\n" % jogadas_usuario)
            else:
                print("Fim do jogo! Você ganhou!\n")
            return jogadas_usuario



def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if (n % (m + 1)) != 0:
        print("\nComputador começa!\n") 
        n = n - computador_escolhe_jogada(n, m)
    else:
        print("\nVocê começa!\n")

    while n > 0:
        n = n - usuario_escolhe_jogada(n, m)
        if n == 0:
            break

        n = n - computador_escolhe_jogada(n, m)
        if n == 0:
            break



print("\nBem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
game_type = int(input())


print("Voce escolheu um campeonato!\n") if game_type == 2 \
else print("Voce escolheu uma partida isolada!\n")

matches = 3 if game_type == 2 else 1



if game_type == 2:
    while matches > 0:
        print("**** Rodada", (4 - matches), " ****\n")
        partida()
        matches = matches - 1

    print("**** Final do campeonato! ****")
    print("Placar: você 0 x 3 Computador")

else:
    while matches > 0:
        partida()
        matches = matches - 1