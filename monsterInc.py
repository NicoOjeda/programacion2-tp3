from humano import Humano
from monstruo import Monstruo


class MonsterInc:
    
    def __init__(self):
        
        self.monstruos = []
        self.humanos = []
        
    def agregarMonstruo(self, mon: Monstruo):
        self.monstruos.append(mon)
    
    def agregarHumano(self, hum: Humano):
        self.humanos.append(hum)
        
    def obtenerMonstruos(self):
        return self.monstruos
    
    def obtenerHumanos(self):
        return self.humanos
    
    def eliminarMonstruo(self, monstruo: Monstruo):
        self.monstruos.remove(monstruo)
    
    def eliminarHumano(self, humano: Humano):
        self.humanos.remove(humano)