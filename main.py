import Jogo
from os import system


play = Jogo()
n  = 20
while n != 0:
    print("Jogo da velha")
    print("1) Jogar")
    print("2) Placar")
    print("3) Reiniciar")
    print("0) Sair")

    n = int(input())

    if n == 1:
        play = Jogo()
        while not play.acabo:
            play.imprime(play.tabela)
            print(f"Jogador {play.jogador[play.vez]} sua vez")
            play.aux = int(input())
            play.jogar(play.vez, play.jogadas, play.tabela, play.aux)
    elif n == 2:
        play.imprimirPlacar(play.placar)
    elif n == 3:
        system("cls")
        play = Jogo()
