""""""
"""
Propriedades

- Métodos públicos utilizados para manipular atributos/métodos privados.

#Exemplos
class Celular:

    def __init__(self, data, senha, saldoBanco, msg):
        self.__data = data
        self.__senha = senha
        self.__saldoBanco = saldoBanco
        self.__msg = msg

    @property
    def data(self):
        return f'Data de hoje: {self.__data}'

    @property
    def senha(self):
        return self.__senha

    @property
    def saldoBanco(self):
        return self.__saldoBanco

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, resposta):
        self.__msg = resposta

    @property
    def mensagem(self):
        return f'Data: {self.__data}. Mensagem: {self.__msg}'


cel1 = Celular('18/11/2024', 'Mortadela1', 3210, 'Ei, sumido(a)!')
cel2 = Celular('10/03/2023', 'Ab4caxi', 4210, 'Tirou a carne do congelador?')

print(cel1.data)

print(cel1.senha)

print(f'Saldo total: {cel1.saldoBanco + cel2.saldoBanco}')

print(cel1.msg)
cel1.msg = 'Olá, como vai?'
print(cel1.msg)

print(cel2.msg)
cel2.msg = 'Esqueci!! :('
print(cel2.msg)

#Método como propriedade
print(cel1.mensagem)
print(cel2.mensagem)

"""

#Exercicios

class ObjetosPessoais:

    def __init__(self, video_game, senha_celular, dinheiro, camisa, livro):
        self.__video_game = video_game
        self.__senha_celular = senha_celular
        self.__dinheiro = dinheiro
        self.__camisa = camisa
        self.__livro = livro

    @property
    def video_game(self):
        return f'Video Game: {self.__video_game}'

    @property
    def senha_celular(self):
        return self.__senha_celular

    @property
    def dinheiro(self):
        return f'Saldo: {self.__dinheiro}'

    @dinheiro.setter
    def dinheiro(self, novo_saldo):
        self.__dinheiro = novo_saldo

    @property
    def camisa(self):
        return self.__camisa

    @property
    def livro(self):
        return self.__livro


joao = ObjetosPessoais('Playstation 2', 'joaozinho007', 135, 'adidas', 'Cálculo 1')
maria = ObjetosPessoais('Xbox 360', 'floremel', 800, 'Gucci', 'Inglês em 1 hora')

print(joao.video_game)
print(joao.senha_celular)
print(joao.dinheiro)
joao.dinheiro = 5000
print(joao.dinheiro)
print(joao.camisa)
print(joao.livro)

print('\n')
print(maria.video_game)
print(maria.senha_celular)
print(maria.dinheiro)
maria.dinheiro = 14000
print(maria.dinheiro)
print(maria.camisa)
print(maria.livro)