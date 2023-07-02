"""
Classes
"""
"""
O que são?
 - Conjunto de métodos e atributos que constroem o objeto.
Ex: Poderiamos criar uma Classe chamada Controle que justamente controla o objeto ar condicionado tendo como
    Atributo o nivel de temperatura, ligado/desligado, dentre outros.
Como declaro a classe?
class nome_definido:
    #Processo
Ex:
class Controle:
    pass #Utilizada para apenas passar a classe/função

Regras de nomeclatura de classes:
a) palavras compostas devem ser separados por letras maiusculas(SEM UNDERLINE)
b) A primeira letra deve sempre ser maiuscula.
c) Sem acentos,caracteres especiais,dentro outros.
Modo certo:
class ControlaRobo:
    pass #Utilizada para apenas passar a classe/função
Modo errado: #Será aceito, ams nao é o convencional
class controlarobo:
    pass #Utilizada para apenas passar a classe/função
class Controla_Robo:
    pass #Utilizada para apenas passar a classe/função  
Por que deve ser assim?
  - As classes embutidas na linguagem Python tem sempre letras minusculas, por isso, é interessante diferenciar
    nossas proprias classes com letras maiusculas.

Por que criar classe?
 - Para criar novos tipos de dados
Ex:
class Animal:
    pass

leao = Animal()
macaco = Animal()
print(type(leao))
print(type(macaco))
"""

print(help(set)) #Retorna a própria classe
print(dir(set)) #Retorna os métodos e atributos dentro da classe