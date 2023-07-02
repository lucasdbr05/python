"""
Polimorfismo

- Significa muitas formas (poli - muitas; morfis - formas)

- Por exemplo, um overriding é uma representação de polimorfismo.

#Exemplo

class Comida:

    def __init__(self, alimento):
        self.__alimento = alimento

    @property
    def alimento(self):
        return self.__alimento

    def apresentar(self):
        raise NotImplementedError('Esse método só funciona se a Sub Classe implementá-lo '
                                  '(sobrescrevê-lo)')

class Fruta(Comida):

    def __init__(self, alimento):
        super().__init__(alimento)

    def apresentar(self):
        print(f'Sou uma fruta, voce gosta de {self.alimento}?')


class Carne(Comida):

    def __init__(self, alimento):
        super().__init__(alimento)

    def apresentar(self):
        print(f'Sou uma carne, voce gosta de {self.alimento}?')


fruta = Fruta('laranja')
fruta.apresentar()

carne = Carne('frango')
carne.apresentar()

"""
#Exercicio
from math import pi
class FormaGeometrica:
    def __init__(self, name):
        self.__name = name
    def calcular_area(self):
        if self.__name[0] == 'q':
            print(f"Área: {float(input('Lado do Quadrado: '))**2}")
        elif self.__name[0] == 'c':
            print(f"Área: {(float(input('Raio do Circulo'))**2)*pi}")




class SquareArea(FormaGeometrica):
    def __init__(self, name, lado):
        super().__init__(name)
        self.__lado = lado

    def calcular_area(self):
        return print(f'Área do quadrado: {self.__lado**2}')


class CircleArea(FormaGeometrica):
    def __init__(self, name, raio):
        super().__init__(name)
        self.__raio = raio

    def calcular_area(self):
        return print(f'Área da circunferência: {(self.__raio**2)*pi}')



quadrado = SquareArea('quadrado',6)
quadrado.calcular_area()

circulo = CircleArea('circulo',4)
circulo.calcular_area()