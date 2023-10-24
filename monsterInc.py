from humano import Humano
from monstruo import Monstruo


class MonsterInc:
    
    def __init__(self):
        
        self.__monstruos = []
        self.__humanos = []
        
    def agregarMonstruo(self, mon: Monstruo):
        self.__monstruos.append(mon)
    
    def agregarHumano(self, hum: Humano):
        self.__humanos.append(hum)
        
    def obtenerMonstruos(self):
        return self.__monstruos
    
    def obtenerHumanos(self):
        return self.__humanos
    
    def eliminarMonstruo(self, monstruo: Monstruo):
        self.__monstruos.remove(monstruo)
    
    def eliminarHumano(self, humano: Humano):
        self.__humanos.remove(humano)
        
sullivan = Monstruo("James P. Sullivan", "leon")
mike = Monstruo("Mike Wazowski", "ciclope")
boo = Humano("Boo")

monsterInc = MonsterInc()
monsterInc.agregarMonstruo(mike)
monsterInc.agregarMonstruo(sullivan)
print(monsterInc.obtenerMonstruos())