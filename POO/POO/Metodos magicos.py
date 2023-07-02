""""""
"""
Métodos Mágicos

- Métodos mágicos são métodos que possuem dunder (__) em seus nomes.

#Exemplos:
__init__
__repr__
__str__
__add__
__mul__
__len__
__del__

class Carro:

    def __init__(self, cor, portas, valor, ano):
        self.cor = cor
        self.portas = portas
        self.valor = valor
        self.ano = ano

    def __repr__(self):
        return f'{self.portas} portas e ano {self.ano}'

    def __str__(self):
        return f'Carro {self.cor} que vale {self.valor}'

    def __add__(self, other):
        return f'{self} ..... {other}'

    def __mul__(self, other):
        if isinstance(other, int):
            result = ' '
            for i in range(other): # 0, 1, 2, 3, 4
                result += ' ' + str(self)
            return result
        return 'É necessário um número inteiro para multiplicar'

    def __len__(self):
        return self.portas

    def __del__(self):
        print('Objeto do tipo Carro deletado!')


carro1 = Carro('prata', 4, 30000, 2011)
carro2 = Carro('vermelho', 2, 130000, 2016)

print(carro1)
print(carro2)

print(carro1 + carro2)

print(carro1 * 5)

print(len(carro1))
print(len(carro2))

print(dir(object))

"""

#Exercicio
from random import *


class Books:

    def __init__(self,nome_livro, n_paginas, edicao):
        self.nome_livro = nome_livro
        self.n_paginas = n_paginas
        self.edicao = edicao
        self.arrecadacao = randint(0,500000)

    def __repr__(self):
        return f'{self.nome_livro} | Edition {self.edicao}'

    def __len__(self):
        return self.n_paginas


livro1 = Books('Harry Potter e as Relíquias da Morte', 551, 1)
livro2 = Books('O Pequeno Príncipe', 96, 2)
livro3 = Books('Mar Sem Fim', 308, 3)

print(livro1)
print(livro2)
print(livro3)

print('\n')
print(f'Livro 1: {len(livro1)} páginas')
print(f'Livro 2: {len(livro2)} páginas')
print(f'Livro 3: {len(livro3)} páginas')

print('\n')
print(f'Arrecadação Livro 1: {livro1.arrecadacao}')
print(f'Arrecadação Livro 2: {livro2.arrecadacao}')
print(f'Arrecadação Livro 3: {livro3.arrecadacao}')

valorTotal = livro1.arrecadacao + livro2.arrecadacao + livro3.arrecadacao
if valorTotal > 1000000:
    print('\nParabéns! Você agora é um milionário!')
else:
    print('\nTente criar mais livros!')
print(f'Valor arrecadado: {valorTotal}')
