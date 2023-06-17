from Modelo.Calendario import Calendario
from Vista.VistaCalendario import VistaCalendario

class ControladorCalendario:
    def __init__(self):
        self.vista = VistaCalendario()
        self.calendario = Calendario()