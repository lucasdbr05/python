class Robo:

    def __init__(self, bateria):
        self.bateria = bateria
        self.ligado = False

    def liga_desliga(self):
        if self.bateria == 0:
            print('Robo sem bateria')
            self.ligado = False
        else:
            if self.ligado== False:
                self.ligado = True
                print('Ligado')
            else:
                self.ligado = False
                print('Desligado')

    def movimento(self, lado):
        self.lado = str(lado).lower()
        if self.ligado == False:
            print('Robo desligado. Ligue-o para movê-lo.')
        else:
            if self.bateria >10:
                self.bateria -= 10
            else:
                self.bateria=0
                self.ligado = False
        print(f'{self.lado}')

    def controle_energia(self):
        print(self.ligado)
        print(self.bateria)

def interface():
    print('-----------MENU----------')
    try:
        energy = -1
        while energy < 0 or energy> 100:
            nome = input('Type the name of your robot?').lower()
            energy = int(input('Type the value of the power: '))
            nome = Robo(energy)

    except ValueError:
        print('OPÇÃO INVÁLIDA!')

    else:
        finalizar = ''
        while finalizar!='Sair':
            try:
                opcao = int(input('Escolha sua opção:\n->1: Checar a bateria do robo\n->2:Ligar/Desligar\n->3:Mover\n'))

            except ValueError:
                print('Valor inválido!')
            else:
                if opcao ==1:
                    nome.controle_energia()
                elif opcao==2:
                    nome.liga_desliga()
                elif opcao ==3:
                    lado = input('Informe o lado: ')
                    nome.movimento(lado)
                elif opcao==0:
                    finalizar ='Sair'
                else:
                    print('Valor inválido')

    finally:
        print('Obrigado pela participação')

interface()
