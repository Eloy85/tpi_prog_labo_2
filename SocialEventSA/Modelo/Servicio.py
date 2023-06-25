class Servicio:
    def __init__(self, codigo=0, tipoServicio='', descripcion='', disponibilidad=True, precio=0.0, fueElegido=False, cantidad=1):
        self._codigo = codigo
        self._tipoServicio = tipoServicio
        self._descripcion = descripcion
        self._disponibilidad = disponibilidad
        self._precio = precio
        self._fueElegido = fueElegido
        self._cantidad = cantidad
    
    def getCodigo(self):
        return self._codigo
    
    def setCodigo(self, codigo):
        self._codigo = codigo
    
    def getTipoServicio(self):
        return self._tipoServicio
    
    def setTipoServicio(self, tipoServicio):
        self._tipoServicio = tipoServicio
    
    def getDescripcion(self):
        return self._descripcion
    
    def setDescripcion(self, descripcion):
        self._descripcion = descripcion
    
    def getDisponibilidad(self):
        return self._disponibilidad
    
    def setDisponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad
    
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio
    
    def getFueElegido(self):
        return self._fueElegido
    
    def setFueElegido(self, fueElegido):
        self._fueElegido = fueElegido
    
    def getCantidad(self):
        return self._cantidad
    
    def setCantidad(self, cantidad):
        self._cantidad = cantidad
    
    def __str__(self) -> str:
        return str(self._codigo)+";"+self._tipoServicio+";"+self._descripcion+";"+str(self._disponibilidad)+";"+str(self._precio)