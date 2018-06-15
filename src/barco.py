from observer import Observable
class Barco(Observable):
    
    def __init__(self,vida):
        super().__init__()
        self.posX = None
        self.posY = None
        self.vida = vida
        
    def getPosX(self):
        return self.posX
    
    def setPosX(self,pos):
        self.posX=pos
        
    def getPosY(self):
        return self.posY
    
    def setPosY(self,pos):
        self.posY=pos
        
        
    def getVida(self):
        return self.vida
    
    def avanzar(self):
        xInicial = self.posX
        yInicial = self.posY
        self.posX = xInicial + 1
        self.notify_observers(xInicial,yInicial,xInicial+1,yInicial)