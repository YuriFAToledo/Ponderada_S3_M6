class Animal:
    def __init__(self, nome, especie, nivel_felicidade):
        self.nome = nome
        self.especie = especie
        self.nivel_felicidade = nivel_felicidade

    def alimentar(self):
        if(self.nivel_felicidade == 5):
            print("Animal já está feliz")
        else:
            self.nivel_felicidade += 1
            print("Animal alimentado")

class Recinto:
    def __init__(self, nome, cuidado):
        self.nome = nome
        self.animais = []
        self.cuidado = cuidado

    def adicionar_animal(self, animal):
        
        self.animais.append(animal)

    def alterar_cuidado(self, acao):
        if(acao == 'cuidar'):
            if(self.cuidado == 5):
                print("Recinto já está cuidado")
            else: 
                self.cuidado += 1 
        elif (acao == 'descuidar') : 
            if(self.cuidado == 0):
                print("Recinto está no mínimo de cuidado")
            else:
                self.cuidado -= 1 
        else :
            print("É necessário que a ação seja cuidar ou descuidar")


class Zoologico:
    def __init__(self):
        self.recintos = []
        self.caixa = 0

    def adicionar_recinto(self, recinto):
        self.recintos.append(recinto)

    # o número de visiantes é calculado com base no nível de felicidade e quantidade de animais além do cuidado aos recintos, sendo o ingresso calculado a 30 unidades monetárias
    def receber_visitantes(self):
        bonus_felicidade = sum(animal.nivel_felicidade for recinto in self.recintos for animal in recinto.animais)
        bonus_cuidado = sum(recinto.cuidado for recinto in self.recintos)
        numero_visitantes = bonus_cuidado * bonus_felicidade
        self.caixa += numero_visitantes * 30
