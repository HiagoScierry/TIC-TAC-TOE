from random import randint
from os import system

class Jogo:
    def __init__(self):
        self.jogador = ("X","O")
        self.vez = randint(0,1)
        self.jogadas = 9
        self.placar = [0,0,0]
        self.acabo = False
        self.tabela = [" "," "," "," "," "," "," "," "," "]
        self.aux = 0

    def jogar(self, vez, jogadas, tabela, aux):
        self.vez = vez
        self.jogadas = jogadas
        self.tabela = tabela
        self.aux = aux

        if 1 <= self.aux <=9 and self.tabela[self.aux - 1] == " ":
            self.jogadas -= 1
            self.tabela[self.aux - 1] = self.jogador[self.vez]
            self.verifica(self.tabela)
            
        else:
            print("numero incorreto")

    def verifica(self , tabela):
        if  self.tabela[0] == self.tabela[1] == self.tabela[2] == "X" or \
            self.tabela[3] == self.tabela[4] == self.tabela[5] == "X" or \
            self.tabela[6] == self.tabela[7] == self.tabela[8]  == "X" or \
            self.tabela[0] == self.tabela[3] == self.tabela[6] == "X" or \
            self.tabela[1] == self.tabela[4] == self.tabela[7] == "X" or \
            self.tabela[2] == self.tabela[5] == self.tabela[8] == "X" or \
            self.tabela[2] == self.tabela[4] == self.tabela[6] == "X" or \
            self.tabela[0] == self.tabela[4] == self.tabela[8] == "X" :
                self.acabo = True
                self.imprime(self.tabela)
                print("X ganhou")
                self.placar[0] += 1 

        if  self.tabela[0] == self.tabela[1] == self.tabela[2] == "O" or \
            self.tabela[3] == self.tabela[4] == self.tabela[5] == 'O' or \
            self.tabela[6] == self.tabela[7] == self.tabela[8]  == "O" or \
            self.tabela[0] == self.tabela[3] == self.tabela[6] == "O" or \
            self.tabela[1] == self.tabela[4] == self.tabela[7] == "O" or \
            self.tabela[2] == self.tabela[5] == self.tabela[8] == "O" or \
            self.tabela[2] == self.tabela[4] == self.tabela[6] == "O" or \
            self.tabela[0] == self.tabela[4] == self.tabela[8] == "O" :
                self.acabo = True
                self.imprime(self.tabela)
                print("O ganhou")
                self.placar[2] += 1

        elif self.jogadas == 0:
            self.acabo = True
            self.imprime(self.tabela)
            print("Empate")
            self.placar[1] += 1

        elif self.jogador[self.vez] == "X":
            self.vez = 1
        else:
            self.vez = 0
            

    def imprime(self, tabela):
        system("cls")
        print(f" ╔═══╦═══╦═══╗ ")
        print(f" ║ {self.tabela[6]} ║ {self.tabela[7]} ║ {self.tabela[8]} ║")
        print(f" ╠═══╬═══╬═══╣ ")
        print(f" ║ {self.tabela[3]} ║ {self.tabela[4]} ║ {self.tabela[5]} ║")
        print(f" ╠═══╬═══╬═══╣ ")
        print(f" ║ {self.tabela[0]} ║ {self.tabela[1]} ║ {self.tabela[2]} ║")
        print(f" ╚═══╩═══╩═══╝")

    def imprimirPlacar(self, placar):
        system("cls")
        print(f" ╔═════════════╦═════════╦═════════════╗ ")
        print(f" ║  Jogador X  ║  Velha  ║  Jogador O  ║ ")
        print(f" ╠═════════════╬═════════╬═════════════╣ ")
        print(f" ║  {str(placar[0]).center(9)}  ║  {str(placar[1]).center(5)}  ║  {str(placar[2]).center(9)}  ║ ")
        print(f" ╚═════════════╩═════════╩═════════════╝")