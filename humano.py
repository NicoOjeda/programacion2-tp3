class Humano:
    
    especie= "humano"
    
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__estadoAsustado = False
        self.especie = Humano.especie
        
    def establecerNombre(self, nom: str):
        self.__nombre = nom
    
    def obtenerNombre(self):
        return self.__nombre
    
    def establecerEstadoAsustado(self, est: bool):
        self.__estadoAsustado = est
    
    def obtenerEstadoAsustado(self):
        return self.__estadoAsustado
    
    def imprimir(self):
        print(self.__nombre + " " + str(self.__estadoAsustado) + " " + str(self.especie))

    def __repr__(self):
        return self.__nombre