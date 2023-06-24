class Evento:
    def __init__(self, fecha, cliente, tipoEvento, servicios, precioTotal):
        self._fecha = fecha
        self._cliente = cliente
        self._tipoEvento = tipoEvento
        self._servicios = servicios
        self._precioTotal = precioTotal
    
    def getFecha(self):
        return self._fecha
    
    def setFecha(self, fecha):
        self._fecha = fecha
    
    def getCliente(self):
        return self._cliente
    
    def setCliente(self, cliente):
        self._cliente = cliente
    
    def getTipoEvento(self):
        return self._tipoEvento
    
    def setTipoEvento(self, tipoEvento):
        self._tipoEvento = tipoEvento
    
    def getServicios(self):
        return self._servicios
    
    def setServicios(self, servicio):
        self._servicios.append(servicio)
    
    def getPrecioTotal(self):
        return self._precioTotal
    
    def setPrecioTotal(self, precioTotal):
        self._precioTotal = precioTotal
    
    def __str__(self) -> str:
        return str(self._fecha)+";"+str(self._cliente)+";"+str(self._tipoEvento)+";"+str(self._servicios)+";"+str(self._precioTotal)
    