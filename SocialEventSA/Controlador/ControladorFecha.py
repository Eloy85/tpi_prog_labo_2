from Modelo.Fecha import Fecha
from Vista.VistaFecha import VistaFecha
from datetime import datetime, timedelta

class ControladorFecha:
    def __init__(self, archivo):
        self.fecha = Fecha(0, 0, 0)
        self.vista = VistaFecha()
        self.archivo = archivo
        self.fechasReservadas = []
    
    def cargarArchivo(self):
        with open(self.archivo, "r") as archivo:
            for linea in archivo.readlines():
                linea = linea.split(",")
                self.fecha = Fecha(linea[0], linea[1], linea[2])
                self.fechasReservadas.append(self.fecha)
    
    def ingresarDia(self):
        self.fecha.setDia(self.vista.ingresarDia())
        if self.fecha.getDia() < 1 or self.fecha.getDia() > 31:
            self.fecha.setDia(self.vista.ingresarDia())
    
    def ingresarMes(self):
        meses30 = [4, 6, 9, 11]
        self.fecha.setMes(self.vista.ingresarMes())
        if self.fecha.getMes() < 1 or self.fecha.getMes() > 12:
            self.fecha.setMes(self.vista.ingresarMes())
        if self.fecha.getMes() in meses30 and self.fecha.getDia() > 30:
            self.ingresarDia()
        elif self.fecha.getMes() == 2 and self.fecha.getDia() > 29:
            self.ingresarDia()
    
    def ingresarAnio(self):
        self.fecha.setAnio(self.vista.ingresarAnio())
        if self.fecha.getMes() == 2 and self.fecha.esBisiesto() == False and self.fecha.getDia() > 28:
            self.ingresarDia()
    
    def verificarDisponibilidad(self):
        fecha = str(self.fecha.getDia())+"/"+str(self.fecha.getMes())+"/"+str(self.fecha.getAnio())
        fecha = datetime.strptime(fecha, "%d-%m-%Y")  # Convertir la fecha solicitada a un objeto datetime
        if fecha in self.agenda:
            # La fecha solicitada está ocupada
            fechaLibre = self.encontrarFechaLibreCercana(fecha)
            return False, fechaLibre
        else:
            # La fecha solicitada está disponible
            return True, None

    def encontrarFechaLibreCercana(self, fecha):
        delta = timedelta(days=1)
        fechaAnterior = self.fecha - delta
        fechaPosterior = self.fecha + delta

        while fechaAnterior in self.agenda or fechaPosterior in self.agenda:
            if fechaAnterior in self.agenda:
                fechaAnterior -= delta
            if fechaPosterior in self.agenda:
                fechaPosterior += delta
        
        # Devolver la fecha libre más cercana
        if self.fecha - fechaAnterior < fechaPosterior - self.fecha:
            return fechaAnterior.strftime("%d-%m-%Y")
        else:
            return fechaPosterior.strftime("%d-%m-%Y")