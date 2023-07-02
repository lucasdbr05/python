"""
Herança

- Aumentar o alcance de nossas classes utilizando menos código.
- Se uma classe herda de outra classe, ela passa a herdar todos os atributos e métodos da classe
herdada.

A classe herdada é conhecida como:
    Classe Mãe
    Classe Pai
    Classe Base
    Classe Genérica
    Super Classe

A classe que herda é conhecida como:
    Classe Filha
    Classe Específica
    Sub Classe

class Aparelho:

    def __init__(self, marca, peso, volume):
        self.__marca = marca
        self.__peso = peso
        self.__volume = volume

    def volume(self):
        return f'O volume está em {self.__volume}'

class Televisao(Aparelho):

    def __init__(self, marca, peso, volume, polegadas):
        super().__init__(marca, peso, volume)
        self.__polegadas = polegadas

    def volume(self):
        print(super().volume())
        return f'Olha só, {super().volume()}'


class Radio(Aparelho):

    def __init__(self, marca, peso, volume, frequencia):
        super().__init__(marca, peso, volume)
        self.__frequencia = frequencia


tv = Televisao('LG', 2.5, 80, 52)
radio = Radio('Sony', 1, 75, 105)

print(tv.volume())
print(radio.volume())

#Método super() pode acessar qualquer atributo e método da Super Classe.

#Overriding: Reescrever um método presente na Super Classe em uma Sub Classe.
"""

#Exercicio


class Control:

    ligado = False
    def liga_desliga(self):
        self.ligado = not self.ligado


class ArCondicionado(Control):
    def __init__(self, temperatura_atual):
        self.__temperatura_atual = temperatura_atual

    def controle_temperatura(self, temperatura):
        self.__temperatura_atual =  temperatura

    @property
    def temperatura_atual(self):
        return f'Temperatura Atual: {self.__temperatura_atual}'

class Microondas(Control):
    def __init__(self, tempo_atual):
        self.__tempo_atual = tempo_atual

    def controle_tempo(self, tempo):
        self.__tempo_atual = tempo

    @property
    def tempo_atual(self):
        return f'Tempo Atual: {self.__tempo_atual}'

class Televisao(Control):
    def __init__(self,volume_atual):
        self.__volume_atual = volume_atual

    def controle_volume(self, volume):
        self.__volume_atual= volume

    @property
    def volume_atual(self):
        return f'Volume Atual: {self.__volume_atual}'


arc = ArCondicionado(45)
mic = Microondas(60)
tv = Televisao(85)

print(arc.ligado)
arc.liga_desliga()
print(arc.ligado)
print(arc.temperatura_atual)
arc.controle_temperatura(35)
print(arc.temperatura_atual)

print('\n')
print(mic.ligado)
mic.liga_desliga()
print(mic.ligado)
print(mic.tempo_atual)
mic.controle_tempo(40)
print(mic.tempo_atual)

print('\n')
print(tv.ligado)
tv.liga_desliga()
print(tv.ligado)
print(tv.volume_atual)
tv.controle_volume(100)
print(tv.volume_atual)

