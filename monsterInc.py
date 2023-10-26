from monstruo import Monstruo
from puerta import Puerta

class MonsterInc:
    
    def __init__(self):
        
        self.__monstruos = []
        self.__puertas = []
        
    def agregarMonstruo(self, mon: {'asistente': Monstruo, 'asustador': Monstruo}):
        self.__monstruos.append(mon)
    
    def eliminarMonstruo(self, mon: Monstruo):
        for monstruo in self.__monstruos:
            if monstruo['asistente'].equals(mon) or monstruo['asustador'].equals(mon):
                self.__monstruos.remove(monstruo)
                break
    
    def obtenerMonstruos(self):
        return self.__monstruos
    
    def agregarPuertas(self, pue):
        self.__puertas.append(pue)
    
    def eliminarPuertas(self, pue):
        for puerta in self.__puertas:
            if puerta.equals(pue):
                self.__puertas.remove(pue)
                break
            
    def obtenerPuertas(self):
        return self.__puertas
    
monsterInc = MonsterInc()
sullivan = Monstruo("James P. Sullivan", "leon", 'asistente')
mike = Monstruo("Mike Wazowski", "ciclope", 'asustador')
# sullivan.establecerPareja(mike)
# mike.establecerPareja(sullivan)
sam = Monstruo("Sam Thomas", "ganso", 'asistente')
laura = Monstruo("Laura Ingals", "raton", 'asustador')
# sam.establecerPareja(laura)
# laura.establecerPareja(sam)
# puerta1 = Puerta(1,mike)
# puerta2 = Puerta(2,sullivan)
# monsterInc.agregarPuertas(puerta1)
# monsterInc.agregarPuertas(puerta2)
# print(monsterInc.obtenerPuertas())
# monsterInc.eliminarPuertas(puerta2)
# print(monsterInc.obtenerPuertas())
monsterInc.agregarMonstruo({'asistente': sullivan, 'asustador':mike})
monsterInc.agregarMonstruo({'asistente': sam, 'asustador':laura})
# print()
# print(monsterInc.obtenerMonstruos())
# print('-------------')
# monsterInc.eliminarMonstruo(sam)
# print(monsterInc.obtenerMonstruos())
# boo = Humano("Boo")
# monsterInc = MonsterInc()
# monsterInc.agregarMonstruo(mike)
# monsterInc.agregarMonstruo(sullivan)