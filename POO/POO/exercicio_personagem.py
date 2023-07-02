class Personagem:

    def __init__(self, nome_completo, altura, peso, resistencia):
        self.nome_completo = nome_completo
        self.altura = altura
        self.peso = peso
        self.resistencia = resistencia

    def poder(self, magia, persuasao, agilidade, forca):
        self.__magia = magia
        self.__persuasao = persuasao
        self.__agilidade = agilidade
        self.__forca = forca
        return magia + persuasao + agilidade + forca

dict_poder = {}

lucas = Personagem('Lucas Lima', 1.78, 76,92)
print(lucas.poder(69,85,78,92))
dict_poder[lucas.nome_completo] = lucas.poder(69,85,78,92)

joel = Personagem('Joel Troy Baker', 1.80, 80, 60)
dict_poder[joel.nome_completo] = joel.poder(0, 60, 60, 55)

ezio = Personagem('Ezio Auditore da Firenze', 1.8, 85, 65)
dict_poder[ezio.nome_completo] = ezio.poder(50, 80, 80, 70)

print(dict_poder)
maior = 0
nome = ''
for chave,poder in dict_poder.items():
    if maior < poder:
        nome = chave
        maior = poder

print(f'{nome} foi vencedor| Power= {maior}')

