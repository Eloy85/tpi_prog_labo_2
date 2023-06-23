from Modelo.Evento import Evento
from Vista.VistaEvento import VistaEvento
from Controlador.ControladorCliente import ControladorCliente
from Controlador.ControladorFecha import ControladorFecha
from Controlador.ControladorServicio import ControladorServicio

class ControladorEvento:
    def __init__(self, archivoEventos):
        self.archivoEventos = archivoEventos
        self.evento = Evento(cliente='', tipoEvento='', fecha='', servicios=[], precioTotal=0.0)
        self.vista = VistaEvento()
        self.precioServicios = 0.0
    
    def ingresarCliente(self):
        controladorCliente = ControladorCliente("")
        controladorCliente.cargarArchivo()
        dniCliente = controladorCliente.vista.dni()
        encontrado = False
        for cliente in controladorCliente.listaClientes:
            if dniCliente == cliente.getDni():
                encontrado = True
                print(cliente)
                self.evento.setCliente(cliente)
        if encontrado == False:
            registrarCliente = self.vista.noSeEncontroCliente()
            if registrarCliente.upper() == "S":
                nuevoCliente = controladorCliente.registrarCliente()
                self.evento.setCliente(nuevoCliente)
    
    def ingresarFecha(self):
        controladorFecha = ControladorFecha("")
        controladorFecha.ingresarDia()
        controladorFecha.ingresarMes()
        controladorFecha.ingresarAnio()
        controladorFecha.verificarDisponibilidad()
        self.evento.setFecha(controladorFecha.fecha)
        controladorFecha.guardarArchivo()
    
    def ingresarTipoEvento(self):
        tipoEvento = self.vista.tipoEvento()
        match tipoEvento:
            case 1:
                self.evento.setTipoEvento("Casamiento")
            case 2:
                self.evento.setTipoEvento("Cumpleaños")
            case 3:
                self.evento.setTipoEvento("Bautismo")
            case 4: 
                self.evento.setTipoEvento("Aniversario")
            case 5:
                self.evento.setTipoEvento("Otro")
    
    def elegirServicios(self):
        controladorServicio = ControladorServicio("")
        controladorServicio.inicializarServicios()
        opcion = 1
        while opcion != 0:
            for linea in self.evento.getServicios():
                self.vista.mostrar(linea)
            self.vista.mostrar(f"Precio total de los servicios seleccionados: ${self.precioServicios}")
            opcion = controladorServicio.elegirServicios()
            for servicio in controladorServicio.listaServicios:
                if opcion == servicio.getCodigo():
                    self.evento.setServicios(servicio)
                    self.precioServicios += servicio.getPrecio()
                    if servicio.getCodigo() != 7:
                        servicio.setFueElegido(True)
    
    def confirmarEvento(self):
        self.vista.mostrar(f"Cliente: {self.evento.getCliente().getApellido()}, {self.evento.getCliente().getNombre()}")
        self.vista.mostrar(f"Evento: {self.evento.getTipoEvento()}")
        self.vista.mostrar(f"Fecha: {self.evento.getFecha()}")
        self.vista.mostrar("Servicios seleccionados:")
        for servicio in self.evento.getServicios():
            self.vista.mostrar(f"{servicio.getTipoServicio()} - ${servicio.getPrecio()}")
            self.vista.mostrar(f"\n")
        self.vista.mostrar("--------------------------")
        self.vista.mostrar("Conceptos a abonar:")
        self.vista.mostrar(f"Tarifa base: $")
        self.vista.mostrar(f"Servicios seleccionados: ${self.precioServicios}")
        self.vista.mostrar(f"Impuestos: $")
        self.vista.mostrar(f"TOTAL: $")
        self.vista.mostrar("\n")
        self.vista.mostrar(f"Si los datos son correctos, el monto de la seña que se debe abonar en este acto es de ${self.evento.calcularSenia()}")
        opcion = self.vista.confirmarEvento()
        if opcion.upper() == "S":
            self.vista.eventoRegistrado()