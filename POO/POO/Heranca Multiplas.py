"""
Herança Múltipla

- Uma classe pode herdar múltiplas classes ao mesmo tempo.

- Existem dois tipos de herança múltipla: Direta e Indireta.

- Independente do tipo, a Sub Classe herda todos os métodos e atributos das Super Classes.

#Herança múltipla Direta

class Energia:

    def __init__(self, ligado):
        self.__ligado = ligado

    @property
    def ligado(self):
        return self.__ligado

    def botao(self):
        self.__ligado = not self.__ligado


class Memoria:

    def __init__(self, ram):
        self.__ram = ram

    @property
    def ram(self):
        return self.__ram

class Monitor:

    def __init__(self, polegadas):
        self.__polegadas = polegadas

    @property
    def polegadas(self):
        return self.__polegadas

class Computador(Energia, Memoria, Monitor):

    def __init__(self, ligado, ram, polegadas, valor):
        Energia.__init__(self, ligado)
        Memoria.__init__(self, ram)
        Monitor.__init__(self, polegadas)
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

meuPC = Computador(True, 8, 15.6, 3200)
print(meuPC.ram)
print(meuPC.polegadas)
print(meuPC.valor)
print(meuPC.ligado)
meuPC.botao()
print(meuPC.ligado)

#Herança múltipla Indireta

class Energia:

    def __init__(self, ligado):
        self.__ligado = ligado

    @property
    def ligado(self):
        return self.__ligado

    def botao(self):
        self.__ligado = not self.__ligado

class Memoria(Energia):

    def __init__(self, ligado, ram):
        super().__init__(ligado)
        self.__ram = ram

    @property
    def ram(self):
        return self.__ram

class Monitor(Memoria):

    def __init__(self, ligado, ram, polegadas):
        super().__init__(ligado, ram)
        self.__polegadas = polegadas

    @property
    def polegadas(self):
        return self.__polegadas

class Computador(Monitor):

    def __init__(self, ligado, ram, polegadas, valor):
        super().__init__(ligado, ram, polegadas)
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

meuPC = Computador(True, 8, 15.6, 3200)
print(meuPC.ram)
print(meuPC.polegadas)
print(meuPC.valor)
print(meuPC.ligado)
meuPC.botao()
print(meuPC.ligado)

# Testando o objeto
print(f'meuPC é do tipo Energia? {isinstance(meuPC, Energia)}')
print(f'meuPC é do tipo Memoria? {isinstance(meuPC, Memoria)}')
print(f'meuPC é do tipo Monitor? {isinstance(meuPC, Monitor)}')
print(f'meuPC é do tipo Computador? {isinstance(meuPC, Computador)}')
print(f'meuPC é do tipo object? {isinstance(meuPC, object)}')
print(f'Computador é do tipo object? {isinstance(Computador, object)}')

#MRO - Method Resolution Order

class Estado:

    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f'Eu sou {self.nome} e estou em algum estado por aí'

class Bahia(Estado):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):
        return f'Eu sou {self.nome} e estou na Bahia'

class Alagoas(Estado):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):
        return f'Eu sou {self.nome} e estou em Alagoas'

class Nordeste(Bahia, Alagoas):

    def __init__(self, nome):
        super().__init__(nome)

    def apresentar(self):
        return f'Eu sou {self.nome} e estou no Nordeste'

turista = Nordeste('Gerson')
print(turista.apresentar())

print(Nordeste.__mro__)
print(Nordeste.mro())
print(help(Nordeste))

"""
#Exercicio

class Animal:
    def andar(self):
        print('Walking')
    def correr(self):
        print('Running')

class Carnivoro(Animal):
    def cacar_animal(self):
        print('Hunting animal')
    def comer_carne(self):
        print('Eating meat')

class Herbivoro(Animal):
    def procurar_arvore(self):
        print('Looking for trees')
    def comer_folhas(self):
        print('Eating leaves')

class Human(Carnivoro, Herbivoro):
    def __init__(self, nome):
        self.nome = nome
    def ler_livro(self):
        print('Reading')

class Bear(Carnivoro, Herbivoro):
    def __init__(self, nome):
        self.nome = nome

    def hibernar(self):
        print('Hibernating')


lucas = Human('Lucas')
lucas.ler_livro()
lucas.andar()
lucas.procurar_arvore()
lucas.correr()
lucas.cacar_animal()
lucas.comer_folhas()
lucas.comer_carne()

print('\n')
ze = Bear('Zé Colmeia')
ze.hibernar()
ze.andar()
ze.procurar_arvore()
ze.correr()
ze.cacar_animal()
ze.comer_folhas()
ze.comer_carne()
