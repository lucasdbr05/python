from random import *
from time import *


class Personagem:
    def __pular(self):
        print('PULOU')

    def apertar_w(self, personagem):
        personagem.__pular()

    def __abaixar(self):
        print('ABAIXOU')

    def apertar_s(self, personagem):
        personagem.__abaixar()

    def __direita(self):
        print('DIREITA')

    def apertar_d(self, personagem):
        personagem.__direita()

    def __esquerda(self):
        print('ESQUERDA')

    def apertar_a(self, personagem):
        personagem.__esquerda()

class Controle:

    def tecla_w(self, personagem):
        personagem.apertar_w(personagem)

    def tecla_a(self, personagem):
        personagem.apertar_a(personagem)

    def tecla_s(self, personagem):
        personagem.apertar_s(personagem)

    def tecla_d(self, personagem):
        personagem.apertar_d(personagem)


pontos = -1
tempo = 3
obstaculos = ['CIMA', 'BAIXO', 'ESQUERDA', 'DIREITA']
vivo = True

console = Controle()
jogador = Personagem()

while vivo:
    passou = False
    pontos +=1
    if pontos < 22:
        sleep(tempo - pontos/10)
    print('\n')
    obstaculo = choice(obstaculos)
    print(f'Obstáculo: {obstaculo}')
    comando = input('Comando: ')
    if comando == 'w' and obstaculo=='BAIXO':
        console.tecla_w(jogador)
        passou = True
    elif comando == 's' and obstaculo=='CIMA':
        console.tecla_s(jogador)
        passou = True
    elif comando == 'a' and obstaculo=='DIREITA':
        console.tecla_a(jogador)
        passou = True
    elif comando == 'd' and obstaculo=='ESQUERDA':
        console.tecla_d(jogador)
        passou = True
    else:
        vivo = False

print(f'Fim de Jogo\nPontauçao: {pontos}')
