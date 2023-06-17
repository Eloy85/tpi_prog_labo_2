class Calendario:
    def __init__(self, fecha="", estado=bool):
        self._fecha = fecha
        self._estado = estado

    def getFecha(self):
        return self._fecha

    def setFecha(self, fecha):
        self._fecha = fecha

    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado
        
    def __str__(self):
        return ""
