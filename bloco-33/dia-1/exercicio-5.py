class Televisao:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligada = False
        self.canal = 1
        self.volume = 0
        self.mudo = True

    def liga_desliga(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def mudar_canal(self, canal):
        if 0 < canal > 100:
            print("Os canais vão de 1 a 100")
        else:
            self.canal = canal

    def proximo_canal(self):
        if self.canal == 100:
            self.canal = 1
        else:
            self.canal += 1

    def canal_anterior(self):
        if self.canal == 1:
            self.canal = 100
        else:
            self.canal -= 1

    def mutar_desmutar(self):
        if self.mudo:
            self.mudo = False
        else:
            self.mudo = True

    def aumentar_volume(self):
        if self.volume == 100:
            print("Volume máximo")
        else:
            self.mudo = False
            self.volume += 1

    def diminuir_volume(self):
        if self.volume == 0:
            print("Volume mínimo")
        else:
            self.mudo = False
            self.volume -= 1
