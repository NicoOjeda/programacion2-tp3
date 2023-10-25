from humano import Humano

class Monstruo:
    
    maxEnergia= 100
    minEnergia= 15
    
    def __init__(self, nom: str, esp: str, tipo:str):
        self.__nombre = nom
        self.__especie = esp
        self.__energia = Monstruo.maxEnergia
        self.__estadoDormido = False
        self.__tipo = tipo if tipo in ["asustador", "asistente"] else "asustador"
        self.__pareja = None
    
    def establecerNombre(self,nom:str):
        self.__nombre = nom
            
    def obtenerNombre(self):
        return self.__nombre
    
    def establecerEspecie(self,esp: int):
        self.__especie = esp
            
    def obtenerEspecie(self):
        return self.__especie
    
    def establecerEnergia(self,ene: int):
        self.__energia = ene
    
    def obtenerEnergia(self):
        return self.__energia
    
    def obtenerTipo(self):
        return self.__tipo
    
    def establecerPareja(self, mon):
        if self.__tipo != mon.obtenerTipo():
            self.__pareja = mon
        else:
            print('los monstruos deben ser de tipo diferente')
        
            # if mon.obtenerPareja() 
            
    def obtenerPareja(self):
        return self.__pareja
    
    def asustar(self, hum: Humano):
        if self.__estadoDormido == False and self.__energia == Monstruo.minEnergia:
            self.__energia -= 10
            if self.__energia < 0:
                self.__energia = 0
            hum.establecerEstadoAsustado(True)
    
    def divertir(self, hum: Humano):
        if self.__estadoDormido == False and self.__energia == Monstruo.minEnergia:
            self.__energia -= 10
            if self.__energia < 0:
                self.__energia = 0
            hum.establecerEstadoAsustado(False)
    
    def dormir(self):
        self.__estadoDormido = True
        self.__energia += 15
        if self.__energia > self.maxEnergia:
            self.__energia = self.maxEnergia
    
    def despertar(self):
        self.__estadoDormido = False
    
    def establecerEstadoDormido(self,est: bool):
        self.establecerEstadoDormido = est
        
    def obtenerEstadoDormido(self):
        return self.__estadoDormido
    
    def __repr__(self):
        return self.__nombre
    

sullivan = Monstruo("James P. Sullivan", "leon","nose")

mike = Monstruo("Mike Wazowski", "ciclope","asustador")
# boo = Humano("Boo")
# print(sullivan.obtenerEnergia())
# print(mike.establecerEnergia(10))
# print(mike.obtenerEnergia())
print(sullivan.obtenerTipo())
sullivan.establecerPareja(mike)
print(sullivan.obtenerPareja())
# mike.dormir()

# print(mike.obtenerEstadoDormido())
# mike.despertar()
# print(mike.obtenerEstadoDormido())
# print(mike.obtenerEnergia())
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# print(sullivan.obtenerEnergia())
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# sullivan.asustar(boo)
# print(boo.obtenerEstadoAsustado())
# print(sullivan.obtenerEnergia())
# print(sullivan.obtenerEnergia())
# print(mike.obtenerEnergia())
# print(boo.obtenerEstadoAsustado())
# mike.divertir(boo)
# print(sullivan.obtenerEnergia())
# print(mike.obtenerEnergia())
# print(boo.obtenerEstadoAsustado())