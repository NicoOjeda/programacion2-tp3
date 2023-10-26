from humano import Humano
from monstruo import Monstruo
from puerta import Puerta
from monsterInc import MonsterInc

class TesterMonstersInc:

    def main(self):
        
        
        print('-------------------')
        print('A- Agregar y eliminar monstruos')
        sullivan = Monstruo("James P. Sullivan", "leon", 'asistente')
        mike = Monstruo("Mike Wazowski", "ciclope", 'asustador')
        sam = Monstruo("Sam Thomas", "ganso", 'asistente')
        laura = Monstruo("Laura Ingals", "raton", 'asustador')
        monsterInc = MonsterInc()
        monsterInc.agregarMonstruo({'asistente': sullivan, 'asustador':mike})
        monsterInc.agregarMonstruo({'asistente': sam, 'asustador':laura})
        print(monsterInc.obtenerMonstruos())
        print('------------')
        monsterInc.eliminarMonstruo(sam)
        print(monsterInc.obtenerMonstruos())
        
        print('------------')
        print('------------')
        print('agregar y eliminar puertas')
        puerta1 = Puerta(1,mike)
        puerta2 = Puerta(2,sullivan)
        monsterInc.agregarPuertas(puerta1)
        monsterInc.agregarPuertas(puerta2)
        print(monsterInc.obtenerPuertas())
        monsterInc.eliminarPuertas(puerta2)
        print(monsterInc.obtenerPuertas())
        
        print('------------')
        print('------------')
        print('agregar y obtener humano')
        boo = Humano("Boo")
        chuchu = Humano("chuchu")
        puerta1.establecerHumano(boo)
        puerta2.establecerHumano(chuchu)
        print(puerta1.obtenerHumano())
        print(puerta2.obtenerHumano())
        
        pass



if __name__ == "__main__":
    testerMonstersInc = TesterMonstersInc()
    testerMonstersInc.main()