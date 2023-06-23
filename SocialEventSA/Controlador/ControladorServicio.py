from Modelo.Servicio import Servicio
from Vista.VistaServicio import VistaServicio

class ControladorServicio:
    def __init__(self, archivo):
        self.archivo = archivo
        self.vista = VistaServicio()
        self.servicio = Servicio()
        self.listaServicios = []
    
    def inicializarServicios(self):
        with open(self.archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                atributos = linea.strip().split(";")
                self.servicio = Servicio(int(atributos[0]), atributos[1], atributos[2], bool(atributos[3]), float(atributos[4]))
                self.listaServicios.append(self.servicio)
    
    def elegirServicios(self):
        for servicio in self.listaServicios:
            if servicio.getDisponibilidad() == True:
                self.vista.mostrarServicio(str(servicio.getCodigo())+" - "+servicio.getTipoServicio()+" - "+servicio.getDescripcion()+" - $"+str(servicio.getPrecio()))
        opcionServicio = self.vista.elegirServicios()
        return opcionServicio
    
