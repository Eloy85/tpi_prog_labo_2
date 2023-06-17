from Modelo.Calendario import Calendario
from Vista.VistaCalendario import VistaCalendario
import datetime

class ControladorCalendario:
    def __init__(self):
        self.vista = VistaCalendario()
        self.calendario = Calendario()

    def realizar_reservas(self):
        pass