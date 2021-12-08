# Que tal agora então modelarmos uma televisão?
#  Pense em como encapsular comportamentos como o estado (ligado/desligado),
#  ou a taxa de variação do volume, que muda de TV para TV etc.

class TV:
    def __init__(self, polegadas, cor, marca):
        self.polegadas = polegadas
        self.cor = cor
        self.marca = marca
        self.estado = False
        self.volume = 0

    def ligada(self):
        self.estado = True
        return self.estado

    def desligada(self):
        self.estado = False
        return self.estado

    def aumentar_volume(self):
        self.volume += 1
        return self.volume

    def diminuir_volume(self):
        self.volume -= 1
        return self.volume
