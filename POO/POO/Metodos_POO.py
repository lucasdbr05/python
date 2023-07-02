""""""
"""
Métodos - POO

- São funções como quaiquer outras, mas estão dentro de uma classe.(A function inside a Class)

- Basicamente, métodos são divididos em dois grupos: Métodos de instância e Métodos de classe.

#Métodos de instância

- Tem esse nome porque precisamos de uma instância da classe para utilizar este método.

- Método construtor: Um método especial, conhecido também como 'método mágico' (assim como outros que 
começam e terminam com dunder). Possui esse nome pois constrói objetos da classe a que pertence.

Sintaxe: def __init__(self, parâmetros):

#Self é o objeto/instância. O nome self é convencional, pode-se utilizar qualquer nome.

#Exemplo

class Carro:

    def __init__(self, portas, cor):
        #Atributos (características) do carro
        self.portas = portas #Público
        self.cor = cor #Público
        self.__arcondicionado = True #Privado


carroPai = Carro(4, 'prata')
print(carroPai.cor)
#print(carroPai.__arcondicionado) #AttributeError

#_____________________________________________________________________________________________

class Sapato:

    qtdd = 7 #Atributo de classe

    def __init__(self, cor, tamanho, preco, qtddComprada):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.qtddComprada = qtddComprada
        Sapato.qtdd += self.qtddComprada


tamanco = Sapato('azul', 42, 1200, 2)
print(tamanco.qtdd)
print(Sapato.qtdd)

#_____________________________________________________________________________________________

class Computador:

    def __init__(self, cor, peso, polegadas):
        self.cor = cor
        self.peso = peso
        self.polegadas = polegadas

    def memoria(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram


pcPrimo = Computador('vermelho', 0.5, 14)
#print(pcPrimo.cor)

pcPrimo.memoria(1024, 8)
#Computador.memoria(1024, 8) #TypeError

print(pcPrimo.hdd)

#___________________________________________________________________________________________

#Sempre evite criar métodos que comecem e terminem com dunder. Pode haver conflito com alguns métodos 
# internos da linguagem.
#Ex: __name__ e __main__

#Nome de métodos possuem APENAS letras minúsculas. Em caso de haver mais de uma palavra, separar por '_'
#controle_remoto

#Métodos de classe

- Necessário utilizar o decorador: @classmethod

- Não há o 'self', mas sim o 'cls', que se refere a prórpia classe onde está o método.

- 'cls' é também convencional

Sintaxe:
    @classmethod
    def nome_método(cls):

#Método de classe não faz acesso a atributos de objeto/instância.

#_________Subtipos_________
#Construtor
#Públicos
#Privados
#Estáticos

- Necessário utilizar o decorador: @staticmethod

- Sem parâmetros

#Exemplo

class Computador:

    peixes = 98

    @classmethod
    def conta_peixes(cls):
        print(f'Nome da classe: {cls}')
        print(f'Existem {cls.peixes} peixes na classe {cls}')

    @staticmethod
    def modelo():
        return 'HJEF348UG3HWFH'

    def __init__(self, cor, peso, polegadas):
        self.cor = cor
        self.peso = peso
        self.polegadas = polegadas

    def memoria(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram

    def __caracteristicas(self):
        return f'{self.cor} e com {self.hdd} GB'


pcVovo = Computador('dourado', 0.1, 52)
pcVovo.memoria(256, 2)

#print(pcVovo.__caracteristicas) #AttributeError
print(pcVovo._Computador__caracteristicas()) #Name Mangling

print(Computador.modelo())
print(pcVovo.modelo())
"""


class Computador:

    peixes = 98

    @classmethod
    def conta_peixes(cls):
        print(f'Nome da classe: {cls}')
        print(f'Existem {cls.peixes} peixes na classe {cls}')

    @staticmethod
    def modelo():
        return 'HJEF348UG3HWFH'

    def __init__(self, cor, peso, polegadas):
        self.cor = cor
        self.peso = peso
        self.polegadas = polegadas

    def memoria(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram

    def __caracteristicas(self):
        return f'{self.cor} e com {self.hdd} GB'


pcVovo = Computador('dourado', 0.1, 52)
pcVovo.memoria(256, 2)

#print(pcVovo.__caracteristicas) #AttributeError
print(pcVovo._Computador__caracteristicas()) #Name Mangling

print(Computador.modelo())
print(pcVovo.modelo())