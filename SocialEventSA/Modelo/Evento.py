class Evento:
    def __init__(self, tipoEvento, lugar, fecha, precioTotal):
        self._tipoEvento = tipoEvento
        self._lugar = lugar
        self._fecha = fecha
        self._precioTotal = precioTotal
    
    def get_tipoEvento(self):
        return self._tipoEvento
    
    def set_tipoEvento(self, tipoEvento):
        self._tipoEvento = tipoEvento
    
    def get_lugar(self):
        return self._lugar
    
    def set_lugar(self, lugar):
        self._lugar = lugar
    
    def get_fecha(self):
        return self._fecha
    
    def set_fecha(self, fecha):
        self._fecha = fecha
    
    def get_precioTotal(self):
        return self._precioTotal
    
    def set_precioTotal(self, precioTotal):
        self._precioTotal = precioTotal
    