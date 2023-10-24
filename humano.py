class Humano:
    
    especie= "humano"
    
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.estadoAsustado = False
        self.especie = Humano.especie
        
    def establecerNombre(self, nom: str):
        self.nombre = nom
    
    def obtenerNombre(self):
        return self.nombre
    
    def establecerEstadoAsustado(self, est: bool):
        self.estadoAsustado = est
    
    def obtenerEstadoAsustado(self):
        return self.estadoAsustado
    
    def imprimir(self):
        print(self.nombre + " " + str(self.estadoAsustado) + " " + str(self.especie))
