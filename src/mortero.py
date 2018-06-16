class Mortero():
    
    def __init__(self, matrizDeDanios):
        self.matrizDeDanios = matrizDeDanios
        
    def atacar(self,barco):
        barco.setVida(barco.getVida()-self.matrizDeDanios[barco.getPosX()][barco.getPosY()])
        