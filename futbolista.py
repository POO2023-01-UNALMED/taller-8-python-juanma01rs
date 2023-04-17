from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    
    _listaFutbolistas = []
    
    def __init__(self, nombre, edad, altura, sexo, deporte = 'Futbol', añosPracticando = 0, golesMarcados = 0, tarjetasRojas = 0, piernaHabil = 0):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)
        
    def __str__(self):
        str = "Mi nombre es " + self.getNombre() + " soy profesional en el deporte " + self.getDeporte() + " Tengo " + str(self.getEdad()) + " años de edad y llevo " + str(self.getAñosPracticando()) + " años en el deporte"
        return str   
    
    def setGolesMarcados(self, golesMarcados):    
        self._golesMarcados = golesMarcados
        
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setTarjetasRojas(self, tarjetasRojas):    
        self._tarjetasRojas = tarjetasRojas
        
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setPiernaHabil(self, piernaHabil):    
        self._piernaHabil = piernaHabil
        
    def getPiernaHabil(self):
        return self._piernaHabil 