from Modelo.Fecha import Fecha
from Vista.VistaFecha import VistaFecha
from datetime import datetime, timedelta

class ControladorFecha:
    def __init__(self, archivo):
        self.fecha = Fecha()
        self.vista = VistaFecha()
        self.archivo = archivo
        self.fechasReservadas = []
    
    def cargarArchivo(self):
        with open(self.archivo, "r") as archivo:
            for linea in archivo.readlines():
                linea = linea.strip().split("/")
                fecha = Fecha(int(linea[0]), int(linea[1]), int(linea[2]))
                self.fechasReservadas.append(fecha)
    
    def ingresarDia(self):
        var1=1
        while var1<2:
            try:
                self.fecha.setDia(self.vista.ingresarDia())
                while self.fecha.getDia() < 1 or self.fecha.getDia() > 31:
                    self.vista.valorIncorrecto()
                    self.fecha.setDia(self.vista.ingresarDia())
                var1=3
            except ValueError:
                self.vista.valorIncorrecto()
        
    
    def ingresarMes(self):
        meses30 = [4, 6, 9, 11]
        var1=1
        while var1<2:
            try:
                self.fecha.setMes(self.vista.ingresarMes())
                while self.fecha.getMes() < 1 or self.fecha.getMes() > 12:
                    self.vista.valorIncorrecto()
                    self.fecha.setMes(self.vista.ingresarMes())
                if self.fecha.getMes() in meses30 and self.fecha.getDia() > 30:
                    self.vista.valorIncorrecto()
                    self.ingresarDia()
                elif self.fecha.getMes() == 2 and self.fecha.getDia() > 29:
                    self.vista.valorIncorrecto()
                    self.ingresarDia()
                var1=3
            except ValueError:
                self.vista.valorIncorrecto()
    
    def ingresarAnio(self):
        var1=1
        while var1<2:
            try:
                self.fecha.setAnio(self.vista.ingresarAnio())
                var1=3
                while self.fecha.getMes() == 2 and self.fecha.esBisiesto() == False and self.fecha.getDia() > 28:
                    self.vista.valorIncorrecto()
                    self.ingresarDia()
            except ValueError:
                self.vista.valorIncorrecto()
    
    def verificarDisponibilidad(self):
        fecha = datetime(self.fecha.getAnio(), self.fecha.getMes(), self.fecha.getDia())
        for element in self.fechasReservadas:
            if datetime(element.getAnio(), element.getMes(), element.getDia()) == fecha:
                return False
        self.fechasReservadas.append(self.fecha)
        self.vista.reservaExitosa()
        return True

    def encontrarFechaLibreCercana(self):
        fecha = datetime(self.fecha.getAnio(), self.fecha.getMes(), self.fecha.getDia())
        delta = timedelta(days=1)
        fechaAnterior = fecha - delta
        fechaPosterior = fecha + delta
        while fechaAnterior in self.fechasReservadas or fechaPosterior in self.fechasReservadas:
            if fechaAnterior in self.fechasReservadas:
                fechaAnterior -= delta
            if fechaPosterior in self.fechasReservadas:
                fechaPosterior += delta
        return fechaAnterior.strftime("%d/%m/%Y") if fechaAnterior not in self.fechasReservadas else fechaPosterior.strftime("%d/%m/%Y")
    
    def ofrecerFecha(self, fecha):
        self.vista.mostrarFecha(fecha)
        opcion = self.vista.confirmarFechaProxima()
        if opcion:
            fechaSplit = fecha.split("/")
            nuevaFecha = Fecha(int(fechaSplit[0]), int(fechaSplit[1]), int(fechaSplit[2]))
            self.fechasReservadas.append(nuevaFecha)
            self.fecha = nuevaFecha
            self.vista.reservaExitosa()
            return True
        else:
            self.vista.reservaCancelada()
            return False
    
    def guardarArchivo(self):
        self.fechasReservadas.sort(key=lambda fecha: datetime(fecha.getAnio(), fecha.getMes(), fecha.getDia()))
        with open(self.archivo, "w") as archivo:
            for element in self.fechasReservadas:
                archivo.write(str(element))
                archivo.write("\n")