from Modelo.Servicio import Servicio
from Vista.VistaServicio import VistaServicio

class ControladorServicio:
    def __init__(self,vista=VistaServicio(),servicio=Servicio(),servicios=[]):
        self.vista=vista
        self.servicio=servicio
        self.servicios=servicios
    def inicializar_servicios(self):
        with open("servicios.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                atributos = linea.strip().split(';')
                servicio = Servicio(atributos[0], atributos[1], atributos[2], atributos[3])
                self.servicios.append(servicio)
    
def lectura_tipos_servicios(servicios):
    tipos_servicios = []
    with open(servicios.txt, 'r') as archivo:
        for linea in archivo:
            tipo_servicio = linea.strip()
            tipos_servicios.append(tipo_servicio)
    return tipos_servicios  