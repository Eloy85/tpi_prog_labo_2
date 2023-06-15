class Servicio:
    def __init__(self, tipoServicio, descripcion, disponibilidad, precio):
        self._tipoServicio = tipoServicio
        self._descripcion = descripcion
        self._disponibilidad = disponibilidad
        self._precio = precio
    
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
    