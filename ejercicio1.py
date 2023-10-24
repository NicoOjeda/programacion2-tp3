from humano import Humano
from monstruo import Monstruo
from monsterInc import MonsterInc

class Puerta:
    
    def __init__(self, num, hum: Humano):
        self.numero = num
        self.humano = hum
        self.monstruo = None
        self.estadoActiva = False
    
    def establecerHumano(self, hum: Humano):
        self.humano = hum
        
    def obtenerHumano(self):
        return self.humano
    
    def establecerMonstruo(self,mon: Monstruo):
        self.monstruo= mon
    
    def obtenerMonstruo(self):
        return self.monstruo
    
    def establecerEstadoActiva(self,est: bool):
        self.estadoActiva= est
    
    def obtenerEstadoActiva(self):
        return self.estadoActiva
    
    def obtenerEstadoEnUso(self):
        return self. estadoActiva and self.monstruo != None
        
    def equals(self,pue):
        return (self.humano == pue.obtenerHumano() and self.monstruo == pue.obtenerMonstruo() 
                and self.estadoActiva == pue.obtenerEstadoActiva())
