class TV:
    def __init__(self, tamanho):
        self.volume = 50
        self.canal = 1
        self.tamanho = tamanho
        self.ligada = False

    def aumentar_volume(self):
        if self.volume <= 99:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume >= 0:
            self.volume -= 1

    def modificar_canal(self, canal):
        if 0 <= canal <= 99:
            self.canal = canal
        else:
            raise ValueError

    def ligar_desligar(self):
        self.ligada = not self.ligada
