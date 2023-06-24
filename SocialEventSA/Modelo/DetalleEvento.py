class DetalleEvento:
    def __init__(self, costoServicios=0.0, iva=0.0, costoTotal=0.0, costoAdministrativo=0.0, precio_congelado=0.0):
        self._costoServicios = costoServicios
        self._costoAdministrativo = costoAdministrativo
        self._iva = iva
        self._costoTotal = costoTotal
        self.precio_congelado = precio_congelado
        

    
    def setCostoServicios(self, costoServicios):
        self._costoServicios = costoServicios
    
    def setCostoAdministrativo(self, costo):
        self._costoAdministrativo = costo

    def setIva(self, iva):
        self._iva = iva

    def setCostoTotal(self, total):
        self._costoTotal = total
    
    def getCostoServicios(self):
        return self._costoServicios

    def getCostoAdministrativo(self):
        return self._costoAdministrativo

    def getIva(self):
        return self._iva

    def getCostoTotal(self):
        return self._costoTotal
    
    def calcularIva(self):
        self.setIva((self._costoAdministrativo + self._costoServicios) * 0.21)

    def obtenerTotal(self):
        iva = self.getIva()
        costoAdministrativo = self.getCostoAdministrativo()
        costoServicios = self.getCostoServicios()
        total = iva + costoAdministrativo + costoServicios
        self.setCostoTotal(total)
        return total

    def calcularSenia(self):
        return self._costoTotal * 0.3
    
    def agregar_pago(self, monto, fecha):
        self.pagos.append((monto, fecha))

    def obtener_pagos(self):
        return self.pagos

    def calcular_deuda(self):
        pagado = sum([p[0] for p in self.pagos])
        deuda = self.precio_congelado - pagado
        return deuda