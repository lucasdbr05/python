class Pessoa:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        self.__salario = valor


class Funcionario(Pessoa):
    def promocao(self):
        self.salario *=1.1


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, codigo, num_estagiarios, codigo_estgiarios):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo
        self.__num_estagiarios = num_estagiarios
        self.__codigo_estagiarios = codigo_estgiarios

    def alterar_codigo(self, novocodigo):
       self.__codigo_estagiarios = novocodigo

    def __repr__(self):
        return f'Gerente: {self.nome}\n Salary: {self.salario}\n'

class Estagiario(Funcionario):
    def __init__(self, nome, cpf, salario, codigo):
        super().__init__(nome, cpf, salario)
        self.__codigo = codigo


    def __repr__(self):
        return f'Estagiario: {self.nome}\n Salary: {self.salario}\n'



gerente = Gerente('Pablo', 12345678900, 12000, 'gege123', 3, 'es1234')
estagiario1 = Estagiario('João', 12345678911, 400, 'es1234')
estagiario2 = Estagiario('Larissa', 12345678922, 400, 'es1234')
estagiario3 = Estagiario('Pedro', 12345678933, 400, 'es1234')

print(gerente.__repr__())
print(estagiario1.__repr__())
print(estagiario2.__repr__())
print(estagiario3.__repr__())

print('\n')
estagiario1.promocao()
estagiario2.promocao()
gerente.promocao()
print(gerente.__repr__())
print(estagiario1.__repr__())
print(estagiario2.__repr__())
print(estagiario3.__repr__())