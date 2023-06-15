from Modelo.Evento import Evento
from Vista.VistaEvento import VistaEvento
from datetime import datetime, timedelta

class ControladorEvento:
    def __init__(self, archivoEventos):
        self.archivoEventos = archivoEventos
        self.evento = Evento(tipoEvento='', lugar='', fecha='', precioTotal=0.0)
        self.vista = VistaEvento()
        self.fechaSolicitada = ''
        self.agenda = []
    
    def verificarDisponibilidad(self):
        self.fechaSolicitada = datetime.strptime(self.fechaSolicitada, "%d-%m-%Y")  # Convertir la fecha solicitada a un objeto datetime
        if self.fechaSolicitada in self.agenda:
            # La fecha solicitada está ocupada
            fechaLibre = self.encontrarFechaLibreCercana()
            return False, fechaLibre
        else:
            # La fecha solicitada está disponible
            return True, None

    def encontrarFechaLibreCercana(self):
        delta = timedelta(days=1)
        fechaAnterior = self.fechaSolicitada - delta
        fechaPosterior = self.fechaSolicitada + delta

        while fechaAnterior in self.agenda or fechaPosterior in self.agenda:
            if fechaAnterior in self.agenda:
                fechaAnterior -= delta
            if fechaPosterior in self.agenda:
                fechaPosterior += delta
        
        # Devolver la fecha libre más cercana
        if self.fechaSolicitada - fechaAnterior < fechaPosterior - self.fechaSolicitada:
            return fechaAnterior.strftime("%d-%m-%Y")
        else:
            return fechaPosterior.strftime("%d-%m-%Y")