from Modelo.DetalleEvento import DetalleEvento
from Modelo.Evento import Evento
from Vista.VistaDetalleEvento import VistaDetalleEvento

class ControladorDetalleEvento:
    def __init__(self, modelo = DetalleEvento(), vista = VistaDetalleEvento()):
        self.detalleEvento = modelo
        self.vista = vista
        self.evento = Evento(fecha='', cliente='', tipoEvento='', servicios=[], precioTotal=0.0) 

    def calcularTotalServicios(self):
        lista = DetalleEvento.GetServicios()
        for objeto in lista:
            precio = objeto.GetPrecio() #traer get del modelo de servicios

    def cargar_detalle_de_clientes(self, nombre_cliente, fecha_evento):
        with open(f"Detalle Clientes\\D_{fecha_evento}-{nombre_cliente}.txt", 'w') as archivo:
            self.detalleEvento.calcularIva()
            archivo.write(f"Cliente: {self.evento.getCliente()}")
            archivo.write(f"Evento: {self.evento.getTipoEvento()}")
            archivo.write(f"Fecha: {self.evento.getFecha()}")
            archivo.write("Servicios seleccionados:")
            for servicio in self.evento.getServicios():
                archivo.write(f"{servicio.getTipoServicio()} - ${servicio.getPrecio()}")
            archivo.write(f"Costo administrativo: ${self.detalleEvento.getCostoAdministrativo()}")
            archivo.write(f"Servicios seleccionados: ${self.detalleEvento.getCostoServicios()}")
            archivo.write(f"IVA: ${self.detalleEvento.getIva()}")
            archivo.write(f"TOTAL: ${self.detalleEvento.obtenerTotal()}")
            archivo.write("\n") # comprobar si funciona

