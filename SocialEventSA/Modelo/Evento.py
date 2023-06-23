class Evento:
    def __init__(self, cliente, tipoEvento, fecha, servicios, precioTotal):
        self._cliente = cliente
        self._tipoEvento = tipoEvento
        self._fecha = fecha
        self._servicios = servicios
        self._precioTotal = precioTotal
    
    def getCliente(self):
        return self._cliente
    
    def setCliente(self, cliente):
        self._cliente = cliente
    
    def getTipoEvento(self):
        return self._tipoEvento
    
    def setTipoEvento(self, tipoEvento):
        self._tipoEvento = tipoEvento
    
    def getFecha(self):
        return self._fecha
    
    def setFecha(self, fecha):
        self._fecha = fecha
    
    def getServicios(self):
        return self._servicios
    
    def setServicios(self, servicios):
        self._servicios.append(servicios)
    
    def getPrecioTotal(self):
        return self._precioTotal
    
    def setPrecioTotal(self, precioTotal):
        self._precioTotal = precioTotal
    
    def __str__(self) -> str:
        return "Cliente: "+self._cliente+"\nTipo de evento: "+self._tipoEvento+"\nFecha: "+self._fecha+"\nPrecio total: $"+self._precioTotal
    
    def calcularSenia(self):
        return self._precioTotal * 0.3
    