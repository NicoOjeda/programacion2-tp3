from humano import Humano

class Monstruo:
    
    maxEnergia= 100
    
    def __init__(self, nom: str, esp: str, est: bool):
        self.nombre = nom
        self.especie = esp
        self.energia = Monstruo.maxEnergia
        self.estadoDormido: False
    
    def establecerNombre(self,nom:str):
        self.nombre = nom
            
    def obtenerNombre(self):
        return self.nombre
    
    def establecerEspecie(self,esp: int):
        self.especie = esp
            
    def obtenerEspecie(self):
        return self.nombre
    
    def establecerEnergia(self,ene: int):
        self.energia = ene
    
    def obtenerEnergia(self):
        return self.energia
    
    def asustar(self, hum: Humano):
        self.energia -= 10
        hum.establecerEstadoAsustado(True)
    
    def divertir(self, hum: Humano):
        self.energia += 20
        hum.establecerEstadoAsustado(False)