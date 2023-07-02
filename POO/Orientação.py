class TV:
    cor = 'preta'
    def __init__(self,tamanho):
        self.ligado = False
        self.tamanho = tamanho
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
tv_sala = TV(25)
tv_quarto = TV(42)

tv_sala.mudar_canal('SporTV')
print(tv_quarto.canal, tv_sala.canal)
print(tv_quarto.tamanho, tv_sala.tamanho)
print(tv_sala.cor)
TV.cor= 'BRANCO'
print(tv_quarto.cor)