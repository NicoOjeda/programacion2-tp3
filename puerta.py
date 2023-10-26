from humano import Humano
from monstruo import Monstruo
# from monsterInc import MonsterInc

class Puerta:
    
    def __init__(self, num:int, hum):
        self.numero = num
        self.humano = hum
        self.monstruo = None
        self.estadoActiva = False
    
    def obtenerNumero(self):
        return self.numero
    
    def establecerHumano(self, hum):
        self.humano = hum
        
    def obtenerHumano(self):
        return self.humano
    
    def establecerMonstruo(self,mon):
        self.monstruo= mon
    
    def obtenerMonstruo(self):
        return self.monstruo
    
    def establecerEstadoActiva(self,est: bool):
        self.estadoActiva= est
    
    def obtenerEstadoActiva(self):
        return self.estadoActiva
    
    def obtenerEstadoEnUso(self):
        return self.estadoActiva and self.monstruo != None
        
    def equals(self,pue):
        return (self.humano == pue.obtenerHumano() and self.monstruo == pue.obtenerMonstruo() and self.estadoActiva == pue.obtenerEstadoActiva())
    
    def __repr__(self):
        return str(self.numero)
    
    
        
# 1-e.i: la ejecucion del metodo equals que compara humanos y monstruos esta refiriendo a una comparacion de identidad (igualdad superficial)

# sullivan = Monstruo("James P. Sullivan", "leon","asistente")
# mike = Monstruo("Mike Wazowski", "ciclope","asustador")
# boo = Humano("Boo")
# puerta1 = Puerta(1,boo)
# sullivan.establecerPareja(mike)
# print(sullivan.obtenerPareja())
# print(puerta1.obtenerNumero())
# print('--------------------')
# sullivan.activarPuerta(puerta1,sullivan)
# print(puerta1.obtenerEstadoActiva())
# print(puerta1.obtenerMonstruo())
# mike.asustar(boo,puerta1)

# print(boo.obtenerEstadoAsustado())