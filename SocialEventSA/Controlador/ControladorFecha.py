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
                print(fecha)
    
    def ingresarDia(self):
        self.fecha.setDia(self.vista.ingresarDia())
        if self.fecha.getDia() < 1 or self.fecha.getDia() > 31:
            self.vista.valorIncorrecto()
            self.fecha.setDia(self.vista.ingresarDia())
    
    def ingresarMes(self):
        meses30 = [4, 6, 9, 11]
        self.fecha.setMes(self.vista.ingresarMes())
        if self.fecha.getMes() < 1 or self.fecha.getMes() > 12:
            self.vista.valorIncorrecto()
            self.fecha.setMes(self.vista.ingresarMes())
        if self.fecha.getMes() in meses30 and self.fecha.getDia() > 30:
            self.vista.valorIncorrecto()
            self.ingresarDia()
        elif self.fecha.getMes() == 2 and self.fecha.getDia() > 29:
            self.vista.valorIncorrecto()
            self.ingresarDia()
    
    def ingresarAnio(self):
        self.fecha.setAnio(self.vista.ingresarAnio())
        if self.fecha.getMes() == 2 and self.fecha.esBisiesto() == False and self.fecha.getDia() > 28:
            self.vista.valorIncorrecto()
            self.ingresarDia()
    
    def verificarDisponibilidad(self):
        disponible = True
        fecha = datetime(self.fecha.getAnio(), self.fecha.getMes(), self.fecha.getDia())
        for element in self.fechasReservadas:
            if datetime(element.getAnio(), element.getMes(), element.getDia()) == fecha:
                respuesta = self.vista.confirmarFechaProxima()
                if respuesta:
                    disponible = False
                else:
                    return False  # Agregar esta línea

        if disponible:
            self.fechasReservadas.append(self.fecha)
            self.vista.reservaExitosa()
            return True

    def encontrarFechaLibreCercana(self, fecha):
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
            fecha = fecha.split("/")
            nuevaFecha = Fecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))
            self.fechasReservadas.append(nuevaFecha)
            return True, self.vista.reservaExitosa()
        else:
            return False, self.vista.reservaCancelada()
    
    def guardarArchivo(self):
        self.fechasReservadas.sort(key=lambda fecha: datetime(fecha.getAnio(), fecha.getMes(), fecha.getDia()))
        with open(self.archivo, "w") as archivo:
            for element in self.fechasReservadas:
                archivo.write(str(element))
                archivo.write("\n")