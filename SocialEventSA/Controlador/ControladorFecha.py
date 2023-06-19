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
        fecha = str(self.fecha.getDia())+"/"+str(self.fecha.getMes())+"/"+str(self.fecha.getAnio())
        fecha = datetime.strptime(fecha, "%d/%m/%Y")  # Convertir la fecha solicitada a un objeto datetime
        for element in self.fechasReservadas:
            if element.getDia() == self.fecha.getDia() and element.getMes() == self.fecha.getMes() and element.getAnio() == self.fecha.getAnio():
                disponible = False
                fechaLibre = self.encontrarFechaLibreCercana(fecha)
                self.ofrecerFecha(fechaLibre)
        if disponible == True:
            self.fechasReservadas.append(self.fecha)
            self.vista.reservaExitosa()

    def encontrarFechaLibreCercana(self, fecha):
        delta = timedelta(days=1)
        fechaAnterior = fecha - delta
        fechaPosterior = fecha + delta
        while fechaAnterior in self.fechasReservadas or fechaPosterior in self.fechasReservadas:
            if fechaAnterior in self.fechasReservadas:
                fechaAnterior -= delta
            if fechaPosterior in self.fechasReservadas:
                fechaPosterior += delta
        if fecha - fechaAnterior < fechaPosterior - fecha:
            return fechaAnterior.strftime("%d/%m/%Y")
        else:
            return fechaPosterior.strftime("%d/%m/%Y")
    
    def ofrecerFecha(self, fecha):
        self.vista.mostrarFecha(fecha)
        opcion = self.vista.confirmarFechaProxima()
        if opcion.upper() == "S":
            fecha = fecha.split("/")
            nuevaFecha = Fecha(int(fecha[0]), int(fecha[1]), int(fecha[2]))
            self.fechasReservadas.append(nuevaFecha)
            return self.vista.reservaExitosa()
    
    def guardarArchivo(self):
        self.fechasReservadas.sort(key=lambda fecha: datetime(fecha.getAnio(), fecha.getMes(), fecha.getDia()))
        with open(self.archivo, "w") as archivo:
            for element in self.fechasReservadas:
                archivo.write(str(element))
                archivo.write("\n")