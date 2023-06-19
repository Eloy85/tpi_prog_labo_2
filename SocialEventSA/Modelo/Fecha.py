import datetime

class Fecha:
    def __init__(self, dia=1, mes=1, anio=2000):
        self._dia = dia
        self._mes = mes
        self._anio = anio
    
    def getDia(self):
        return self._dia
    
    def getMes(self):
        return self._mes
    
    def getAnio(self):
        return self._anio
    
    def setDia(self, dia):
        self._dia = dia
    
    def setMes(self, mes):
        self._mes = mes
    
    def setAnio(self, anio):
        self._anio = anio

    def __str__(self):
        return "{}/{}/{}".format(self._dia, self._mes, self._anio)
    
    def esBisiesto(self):
        if self._anio % 4 == 0:
            if self._anio % 100 == 0:
                if self._anio % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def obtenerDiaSemana(self):
        fecha = datetime(self._anio, self._mes, self._dia)
        diasSemana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        return diasSemana[fecha.weekday()]
