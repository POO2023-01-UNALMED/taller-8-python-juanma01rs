class Deportista:
     
    def __init__ (self, añosPracticando, deporte = "Futbol"):
        self._añosPracticando = añosPracticando
        self._deporte = deporte
    
    def setDeporte(self, deporte):    
        self._deporte = deporte
        
    def getDeporte(self):
        return self._deporte  
    
    def setAñosPracticando(self, añosPracticando):    
        self._añosPracticando = añosPracticando
        
    def getAñosPracticando(self):
        return self._añosPracticando      