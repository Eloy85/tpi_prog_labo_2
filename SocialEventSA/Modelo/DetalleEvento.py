class DetalleEvento:
    def __init__(self, fecha = "", servicios = [], iva = 0, costototal = 0, costoadministrativo = 0):
        self._fecha = fecha
        self._servicios = servicios
        self._costoadministrativo = costoadministrativo
        self._iva = iva
        self._costototal = costototal

    def SetFecha(self, fecha):
        self._fecha = fecha

    def SetCostoAdministrativo(self, costo ):
        self._costoadministrativo = costo

    def SetIva(self, iva):
        self._iva = iva

    def SetCostoTotal(self, total):
        self._costototal = total

    def GetFecha(self):
        return self._fecha

    def GetCostoAdministrativo(self):
        return self._costoadministrativo

    def GetIva(self):
        return self._iva

    def GetCostoTotal(self):
        return self._costototal

    def obtenerTotal(self, Iva, costoadministrativo):
        total = int(self.GetIva()) + int(self.GetCostoAdministrativo()) #falta total de servicios
        self.SetCostoTotal(total)


