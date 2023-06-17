from Modelo.Calendario import Calendario
from Vista.VistaCalendario import VistaCalendario
import datetime
import os

class ControladorCalendario:
    def __init__(self):
        self.vista = VistaCalendario()
        self.calendario = Calendario()        