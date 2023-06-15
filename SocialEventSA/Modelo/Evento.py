class Evento:
    def __init__(self, tipoEvento, lugar, fecha, precioTotal):
        self._tipoEvento = tipoEvento
        self._lugar = lugar
        self._fecha = fecha
        self._precioTotal = precioTotal
    
    def getTipoEvento(self):
        return self._tipoEvento
    
    def setTipoEvento(self, tipoEvento):
        self._tipoEvento = tipoEvento
    
    def getLugar(self):
        return self._lugar
    
    def setLugar(self, lugar):
        self._lugar = lugar
    
    def getFecha(self):
        return self._fecha
    
    def setFecha(self, fecha):
        self._fecha = fecha
    
    def getPrecioTotal(self):
        return self._precioTotal
    
    def setPrecioTotal(self, precioTotal):
        self._precioTotal = precioTotal
    