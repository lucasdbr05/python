"""
Atributos e Objetos
"""
"""
Definição:
a) Atributo: Caracteristicas do Objeto que a Classe irá controlar.
Ex: Uma classe Carro pode ter como atributo a potencia, numero de bancos, velocidade maxima, dentre outros.
b) Objeto: É justamnete o objeto da vida real que será controlado no programa..
Ex: na classe Carro podemos receber como objeto, um Corolla,Civic, Porshe, dentre outros.

Vamos começar pelos objetos:
Ex:
class Carro:

    def __init__(self): #Lembrando que o __init__ é o método contrutor que irá construir nosso objeto
        print(self)

#Self é o objeto em si que voce criar
#Como eu crio um objeto?
#nome = nome_da_classe(atributos que deseja)
Jaguar = Carro() #Criei o onjeto Jaguar que será controlado pela Classe Carro
print(Jaguar) #Ao imprimir Jaguar aparecerá o endereço de memória dele, que é o mesmo do self
#Por baixo dos panos oque acontece?
#Assim que passo Carro(), é como se a palavra init fosse substituida por Carro e Jaguar passasse como primeiro atributo
#Ficando assim: Jaguar = Carro(Jaguar), todo método deve receber a palavra self.

Agora, vamos aos atributos:
a) Atributos de instância: São os atributos declarados dentro do método construtor.
Ex:
class Carro:

    def __init__(self,vel_maxima,potencia,num_bancos):
        #vel_maxima,potencia e num_bancos são os meus atributos de instância
        self.vel_maxima = vel_maxima
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False #A variavel estado irá representar se o carro está ligado ou desligado

#Jaguar = Carro() #Se rodar assim, dará erro, porque o método construtor requisita os atributos para passar como parametro
Jaguar = Carro(250,350,5)
print(Jaguar.potencia) #Maneira de acessar atributos do nosso objeto.

b) Atributos de Classe: São os atributos que são declarados diretamente na Classe, fora de qualquer método
 - A principal caracteristica é justamente que esses atributos servem para todos os objetos declarados.
 Ex:
 class Carro:

    nitro = 1.1 #Vamos aumentar a velocidade maxima de cada objeto em 10%

    def __init__(self,vel_maxima,potencia,num_bancos):
        #vel_maxima,potencia e num_bancos são os meus atributos de instância
        self.vel_maxima = vel_maxima * Carro.nitro #Para acessar essa variavel agora utiliza: nome_classe.atributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False #A variavel estado irá representar se o carro está ligado ou desligado

Jaguar = Carro(250,350,5)
print(Jaguar.vel_maxima)
print(Jaguar.nitro) #Percebe-se que automaticamente criou-se o atributo nitro para Jaguar
print(Carro.nitro)
print(Carro.potencia) #AttributeError, pois potencia é um atributo de instancia

Obs: A vantagem de usar atributo de classe é o menor uso da memória. Pois requer apenas 1 espaço para todos os objetos.

c) Atributos dinamicos: São os atributos que são criados ao longo da execução do programa, sendo que ele estará vinculado
                        apenas ao objeto que o criou.
Ex: 
class Carro:

    nitro = 1.1 #Vamos aumentar a velocidade maxima de cada objeto em 10%

    def __init__(self,vel_maxima,potencia,num_bancos):
        #vel_maxima,potencia e num_bancos são os meus atributos de instância
        self.vel_maxima = vel_maxima * Carro.nitro #Para acessar essa variavel agora utiliza: nome_classe.atributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False #A variavel estado irá representar se o carro está ligado ou desligado

    def cria_atributo(self):
        self.preco = 300000

Jaguar = Carro(250,350,5)
Porshe = Carro(260,310,5)
Jaguar.preco = 300000
print(Jaguar.preco)
#Jaguar.cria_atributo()
#print(Jaguar.preco)
print(Porshe.preco) #AttributeError pois o atributo dinamico pertence apenas ao objeto que o criou

#Complementação:
- Como deletar atributos? Comando del
Ex:
class Carro:

    nitro = 1.1 #Vamos aumentar a velocidade maxima de cada objeto em 10%

    def __init__(self,vel_maxima,potencia,num_bancos):
        #vel_maxima,potencia e num_bancos são os meus atributos de instância
        self.vel_maxima = vel_maxima * Carro.nitro #Para acessar essa variavel agora utiliza: nome_classe.atributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False #A variavel estado irá representar se o carro está ligado ou desligado


Jaguar = Carro(250,350,5)
Porshe = Carro(260,310,5)
Jaguar.preco = 300000
print(Jaguar.__dict__)
del Jaguar.preco
print(Jaguar.__dict__)
print(Porshe.__dict__) #Mesmo deletando um atributo de Jaguar, todos os atributos de Porshe se mantem intactos.

- Subdivisão: Atributos Publicos x Privados
 - Na teoria, atributos publicos podem ser acessados por todos, enquanto privados não.
Como declarar cada uma?
Ex:
self.potencia = potencia #Declarei um atributo publico
self.__potencia = potencia #Declarei um atributo privado

class Carro:

    nitro = 1.1 #Vamos aumentar a velocidade maxima de cada objeto em 10%

    def __init__(self,vel_maxima,potencia,num_bancos):
        #vel_maxima,potencia e num_bancos são os meus atributos de instância
        self.__vel_maxima = vel_maxima * Carro.nitro #Para acessar essa variavel agora utiliza: nome_classe.atributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False #A variavel estado irá representar se o carro está ligado ou desligado


Jaguar = Carro(250,350,5)
Porshe = Carro(260,310,5)
#print(Porshe.vel_maxima) #Nao consigo acessar o atributo
#print(Porshe.__vel_maxima) #Nao consigo acessar o atributo
print(Porshe.potencia) #Consigo acessar o atributo
print(Porshe._Carro__vel_maxima)
print(Jaguar._Carro__vel_maxima) #Percebe-se que o Python apresenta erro, porem é possivel acessar com o Name Mangling: objeto._classe__atributo

Incrementando nosso programa:
class Carro:

    nitro = 1.1 #Vamos aumentar a velocidade maxima de cada objeto em 10%

    def __init__(self,vel_maxima,potencia,num_bancos):
        #vel_maxima,potencia e num_bancos são os meus atributos de instância
        self.__vel_maxima = vel_maxima * Carro.nitro #Para acessar essa variavel agora utiliza: nome_classe.atributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False #A variavel estado irá representar se o carro está ligado ou desligado

    def liga_desliga(self):
        if self.estado == False:
            self.estado = True
        else:
            self.estado = False


Jaguar = Carro(250,350,5)
print(Jaguar.estado)
Jaguar.liga_desliga()
print(Jaguar.estado)
Jaguar.liga_desliga()
print(Jaguar.estado)
Jaguar.liga_desliga()
print(Jaguar.estado)
"""

class Carro:

    nitro = 1.1 #Vamos aumentar a velocidade maxima de cada objeto em 10%

    def __init__(self,vel_maxima,potencia,num_bancos):
        #vel_maxima,potencia e num_bancos são os meus atributos de instância
        self.__vel_maxima = vel_maxima * Carro.nitro #Para acessar essa variavel agora utiliza: nome_classe.atributo
        self.potencia = potencia
        self.num_bancos = num_bancos
        self.estado = False #A variavel estado irá representar se o carro está ligado ou desligado

    def liga_desliga(self):
        if self.estado == False:
            self.estado = True
        else:
            self.estado = False


Jaguar = Carro(250,350,5)
print(Jaguar.estado)
Jaguar.liga_desliga()
print(Jaguar.estado)
Jaguar.liga_desliga()
print(Jaguar.estado)
Jaguar.liga_desliga()
print(Jaguar.estado)
Jaguar = Carro(250,350,5)
Porshe = Carro(260,310,5)
#print(Porshe.vel_maxima) #Nao consigo acessar o atributo
#print(Porshe.__vel_maxima) #Nao consigo acessar o atributo
print(Porshe.potencia) #Consigo acessar o atributo
print(Porshe._Carro__vel_maxima)
print(Jaguar._Carro__vel_maxima)