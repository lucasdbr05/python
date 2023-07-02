""""""

"""
Encapsulamento e Abstração

Encapsulamento - Em POO ocorre o encapsulamento do código dentro das classes, promovendo mais segurança
ao sistema e limitando o acesso de objetos a determinados atributos. Agrupamento de métodos e atributos.
Com o encapsulamento é possível a realização da abstração.

Abstração - Disponibilização ao usuário somente de métodos e atributos realmente necessários de serem
apresentados. Métodos e atributos privados permanecem ocultos.
"""

class Jogo:

    nivel = 8

    def __init__(self, forca, magia, resistencia):
        self.__forca = forca
        self.__magia = magia
        self.__res = resistencia
        self.__nivel = Jogo.nivel

    def atacar_raio(self):
        self.__res -= 5
        self.__magia -= 10

    def atacar_soco(self):
        self.__res -= 10
        self.__forca -= 10

    def __pular_nivel(self):
        Jogo.nivel += 1
        self.__nivel = Jogo.nivel

    def exercicio(self):
        self.__res += 5
        self.__forca += 10

    def cheat(self):
        self.__pular_nivel()

    def status(self):
        print(f'Força: {self.__forca}| Magia: {self.__magia}| Resistência: {self.__res}| '
              f'Nível: {self.__nivel}|')


player1 = Jogo(76, 95, 88)
player1.status()

player1.atacar_raio()
player1.status()

player1.atacar_soco()
player1.status()

player1.exercicio()
player1.status()

player1.cheat()
player1.status()

