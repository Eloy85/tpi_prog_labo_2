class Servicio:
    def __init__(self, tipoServicio, descripcion, disponibilidad, precio):
        self._tipoServicio = tipoServicio
        self._descripcion = descripcion
        self._disponibilidad = disponibilidad
        self._precio = precio
    
    def get_tipoServicio(self):
        return self._tipoServicio
    
    def set_tipoServicio(self, tipoServicio):
        self._tipoServicio = tipoServicio
    
    def get_descripcion(self):
        return self._descripcion
    
    def set_descripcion(self, descripcion):
        self._descripcion = descripcion
    
    def get_disponibilidad(self):
        return self._disponibilidad
    
    def set_disponibilidad(self, disponibilidad):
        self._disponibilidad = disponibilidad
    
    def get_precio(self):
        return self._precio
    
    def set_precio(self, precio):
        self._precio = precio
    