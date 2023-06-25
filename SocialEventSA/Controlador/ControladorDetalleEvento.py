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

    def cargar_detalle_de_clientes(self, nombre_cliente):
        with open(f"C:\\Users\\facuu\\OneDrive\\Escritorio\\Integrador\\tpi_prog_labo_2\\SocialEventSA\\Detalle Clientes\\D_{nombre_cliente}.txt", 'w') as archivo:
            self.detalleEvento.calcularIva()
            archivo.write(f"Cliente: {self.evento.getCliente()}")
            archivo.write(f"Evento: {self.evento.getTipoEvento()}")
            archivo.write(f"Fecha: {self.evento.getFecha()}")
            archivo.write("Servicios seleccionados:")
            for servicio in self.evento.getServicios():
                archivo.write(f"{servicio.getTipoServicio()} - ${servicio.getPrecio()}")
            archivo.write("--------------------------")
            archivo.write("Conceptos a abonar:")
            archivo.write(f"Costo administrativo: ${self.detalleEvento.getCostoAdministrativo()}")
            archivo.write(f"Servicios seleccionados: ${self.detalleEvento.getCostoServicios()}")
            archivo.write(f"IVA: ${self.detalleEvento.getIva()}")
            archivo.write(f"TOTAL: ${self.detalleEvento.obtenerTotal()}")
            archivo.write("\n")

