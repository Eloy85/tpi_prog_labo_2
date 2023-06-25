from typing import Any


class DetalleEvento:
    def __init__(self, cliente='', tipoEvento='', fecha='', servicios={}, costoServicios=0.0, iva=0.0, costoTotal=0.0, costoAdministrativo=0.0):
        self._cliente = cliente
        self._tipoEvento = tipoEvento
        self._fecha = fecha
        self._servicios = servicios
        self._costoServicios = costoServicios
        self._costoAdministrativo = costoAdministrativo
        self._iva = iva
        self._costoTotal = costoTotal
    
    def setCliente(self, cliente):
        self._cliente = cliente
    
    def getCliente(self):
        return self._cliente
    
    def setTipoEvento(self, tipoEvento):
        self._tipoEvento = tipoEvento

    def getTipoEvento(self):
        return self._tipoEvento

    def setFecha(self, fecha):
        self._fecha = fecha
    
    def getFecha(self):
        return self._fecha
    
    def setServicios(self, servicio, cantidad):
        self._servicios[servicio] = cantidad
    
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

    def calcularDeuda(self):
        deuda = self._costoTotal - self.calcularSenia()
        return deuda
    
    def __str__(self) -> str:
        return f'Cliente: {self._cliente}\nTipo de evento: {self._tipoEvento}\nFecha: {self._fecha}\nServicios: {self._servicios}\nSubtotal: ${self._costoServicios}\nCosto administrativo: ${self._costoAdministrativo}\nIVA: ${self._iva}\nTOTAL: ${self._costoTotal}\nMonto de la seña: ${self.calcularSenia()}\nSaldo restante: ${self.calcularDeuda()}'