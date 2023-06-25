from Modelo.Evento import Evento
from Modelo.DetalleEvento import DetalleEvento
from Vista.VistaEvento import VistaEvento
from Controlador.ControladorCliente import ControladorCliente
from Controlador.ControladorFecha import ControladorFecha
from Controlador.ControladorServicio import ControladorServicio
from Controlador.ControladorDetalleEvento import ControladorDetalleEvento
from Vista.VistaCliente import VistaCliente
from datetime import datetime

class ControladorEvento:
    def __init__(self, archivoEventos, archivoClientes, archivoFecha, archivoServicios):
        self.archivoEventos = archivoEventos
        self.archivoClientes = archivoClientes
        self.archivoFecha = archivoFecha
        self.archivoServicios = archivoServicios
        self.evento = Evento(fecha='', cliente='', tipoEvento='', servicios=[], precioTotal=0.0)
        self.vista = VistaEvento()
        self.detalleEvento = DetalleEvento()
        self.controlador_detalle_evento = ControladorDetalleEvento()
        self.vista_cliente = VistaCliente()
        self.listaEventos = []
    
    def cargarArchivo(self):
        with open(self.archivoEventos, "r") as archivo:
            for linea in archivo.readlines():
                linea = linea.strip().split(";")
                evento = Evento(linea[0], linea[1], linea[2], linea[3], linea[4])
                self.listaEventos.append(evento)
    
    def ingresarCliente(self):
        controladorCliente = ControladorCliente(self.archivoClientes)
        controladorCliente.cargarArchivo()
        if controladorCliente.consultarCliente():
            self.evento.setCliente(controladorCliente.cliente)
        else:
            registrarCliente = self.vista.noSeEncontroCliente()
            if registrarCliente.upper() == "S":
                nuevoCliente = controladorCliente.registrarCliente()
                self.evento.setCliente(nuevoCliente)
                controladorCliente.guardarArchivo()
    
    def ingresarFecha(self):
        controladorFecha = ControladorFecha(self.archivoFecha)
        controladorFecha.cargarArchivo()
        controladorFecha.ingresarDia()
        controladorFecha.ingresarMes()
        controladorFecha.ingresarAnio()
        if controladorFecha.verificarDisponibilidad():
            self.evento.setFecha(controladorFecha.fecha)
            controladorFecha.guardarArchivo()
            return True
        else:
            fechaNueva = controladorFecha.encontrarFechaLibreCercana()
            if controladorFecha.ofrecerFecha(fechaNueva):
                controladorFecha.guardarArchivo()
                return True
            else:
                return False
    
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
        controladorServicio = ControladorServicio(self.archivoServicios)
        controladorServicio.inicializarServicios()
        precioServicios = 0.0
        opcion = 1
        while opcion != 0:
            for linea in self.evento.getServicios():
                self.vista.mostrar(linea)
            self.vista.mostrar(f"Precio total de los servicios seleccionados: ${precioServicios}")
            opcion = controladorServicio.elegirServicios()
            for servicio in controladorServicio.listaServicios:
                if opcion == servicio.getCodigo():
                    self.evento.setServicios(servicio)
                    precioServicios += servicio.getPrecio()
                    if servicio.getCodigo() != 7:
                        servicio.setFueElegido(True)
        self.detalleEvento.setCostoServicios(precioServicios)
    
    def confirmarEvento(self):
        self.detalleEvento.calcularIva()
        self.vista.mostrar(f"Cliente: {self.evento.getCliente()}")
        self.vista.mostrar(f"Evento: {self.evento.getTipoEvento()}")
        self.vista.mostrar(f"Fecha: {self.evento.getFecha()}")
        self.vista.mostrar("Servicios seleccionados:")
        for servicio in self.evento.getServicios():
            self.vista.mostrar(f"{servicio.getTipoServicio()} - ${servicio.getPrecio()}")
        self.vista.mostrar("--------------------------")
        self.vista.mostrar("Conceptos a abonar:")
        self.vista.mostrar(f"Costo administrativo: ${self.detalleEvento.getCostoAdministrativo()}")
        self.vista.mostrar(f"Servicios seleccionados: ${self.detalleEvento.getCostoServicios()}")
        self.vista.mostrar(f"IVA: ${self.detalleEvento.getIva()}")
        self.vista.mostrar(f"TOTAL: ${self.detalleEvento.obtenerTotal()}")
        self.vista.mostrar("\n")
        self.vista.mostrar(f"Si los datos son correctos, el monto de la seña que se debe abonar en este acto es de ${self.detalleEvento.calcularSenia()}")
        opcion = self.vista.confirmarEvento()
        if opcion.upper() == "S":
            self.vista.eventoRegistrado()
        self.controlador_detalle_evento.cargar_detalle_de_clientes(self.vista_cliente.nombre()) # comprobar si funciona
    
    def modificarCostoAdministrativo(self):
        opcion = self.vista.costoAdministrativo(self.detalleEvento.getCostoAdministrativo())
        if opcion.upper() == "S":
            self.detalleEvento.setCostoAdministrativo(float(self.vista.nuevoPrecio()))
    
    def guardarArchivo(self):
        with open(self.archivoEventos, "w", encoding="utf-8") as archivo:
            for evento in self.listaEventos:
                servicios = [str(servicio.getTipoServicio()) for servicio in evento.getServicios()]
                cadena = ";".join([str(evento.getFecha()), str(evento.getCliente()), str(evento.getTipoEvento())] + servicios + [str(evento.getPrecioTotal())])
                archivo.write(cadena + "\n")

    def consultarEvento(self):
        opcion = 0
        while opcion != 4:
            opcion = self.vista.consultarEvento()
            if opcion == 1:
                controladorFecha = ControladorFecha(self.archivoFecha)
                controladorFecha.ingresarDia()
                controladorFecha.ingresarMes()
                controladorFecha.ingresarAnio()
                fecha = datetime(controladorFecha.fecha.getAnio(), controladorFecha.fecha.getMes(), controladorFecha.fecha.getDia())
                fecha = fecha.strftime("%#d/%#m/%Y")
                for element in self.listaEventos:
                    if element.getFecha() == fecha:
                        self.vista.mostrar(element)
    
    def ejecutar(self):
        opcion = 0
        opcionEventos = 0
        opcionClientes = 0
        while opcion != 4:
            opcion = self.vista.menuPrincipal()
            while opcion < 1 or opcion > 4:
                opcion = self.vista.menuPrincipal()
            if opcion == 1:
                self.cargarArchivo()
                while opcionEventos != 5:
                    opcionEventos = self.vista.menuEventos()
                    while opcionEventos < 1 or opcionEventos > 5:
                        opcionEventos = self.vista.menuEventos()
                    if opcionEventos == 1:
                        self.ingresarCliente()
                        if self.ingresarFecha() == True:
                            self.ingresarTipoEvento()
                            self.elegirServicios()
                            self.confirmarEvento()
                    elif opcionEventos == 2:
                        self.consultarEvento()
            elif opcion == 2:
                controladorCliente = ControladorCliente(self.archivoClientes)
                controladorCliente.cargarArchivo()
                while opcionClientes != 4:
                    opcionClientes = controladorCliente.vista.menuClientes()
                    while opcionClientes < 1 or opcionClientes > 4:
                        opcionClientes = controladorCliente.vista.menuClientes()
                    if opcionClientes == 1:
                        controladorCliente.registrarCliente()
                    elif opcionClientes == 2:
                        controladorCliente.consultarCliente()