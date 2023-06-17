from Modelo.DetalleEvento import DetalleEvento
from Vista.VistaDetalleEvento import VistaDetalleEvento

class ControladorDetalleEvento:
    def __init__(self, modelo = DetalleEvento(), vista = VistaDetalleEvento()):
        self.modelo = modelo
        self.vista = vista

    def calcularTotalServicios(self):
        lista = DetalleEvento.GetServicios()
        for objeto in lista:
            precio = objeto.GetPrecio() #traer get del modelo de servicios

