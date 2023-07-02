from datetime import datetime
import pytz
from random import randint

class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%y; %H:%M:%S')

    def __init__(self,nome,cpf, agencia , num_conta):
        self._nome = nome
        self.cpf = cpf
        self._saldo = 0
        self.limite = None
        self.__agencia = agencia
        self.conta = num_conta
        self.transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print('Seu saldo é de R${:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self.consultar_saldo()
        self.transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        return self._saldo

    def _limite_(self):
        self.limite = -1000
        return self.limite

    def sacar(self, saque):
        if self._saldo - saque < self._limite_():
            print('Você não pssui saldo suficiente.')
            self.consultar_saldo()
        else:
            self._saldo -= saque
            self.transacoes.append((-saque, self._saldo, ContaCorrente._data_hora()))
            return(self._saldo)

    def cosultar_chequeespecial(self):
        print('Seu limite de cheque especial é de R${:,.2f}'.format(self._limite_()))

    def consultar_transacoes(self):
        print('Histórico de Transações de:')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, value, conta_destino):
        self._saldo -= value
        self.transacoes.append((-value, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += value
        conta_destino.transacoes.append((value, conta_destino._saldo, ContaCorrente._data_hora()))

class CartaoCredito:

    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR


    def __init__(self,titular, conta_corrente):
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular = titular
        self.validade ='{}/{}' .format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_segurança = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = 1000
        self._senha = '2021'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor)==4 and valor.isnumeric():
            self._senha= valor
        else:
            print('NOVA SENHA INVÁLIDA')





