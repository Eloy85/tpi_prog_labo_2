import os
from Modelo.Evento import Evento
from Modelo.DetalleEvento import DetalleEvento
from Vista.VistaEvento import VistaEvento
from Controlador.ControladorCliente import ControladorCliente
from Controlador.ControladorFecha import ControladorFecha
from Controlador.ControladorServicio import ControladorServicio
from Vista.VistaCliente import VistaCliente
from datetime import datetime, timedelta

class ControladorEvento:
    def __init__(self, archivoEventos, archivoClientes, archivoFecha, archivoServicios, archivoCosto):
        self.archivoEventos = archivoEventos
        self.archivoClientes = archivoClientes
        self.archivoFecha = archivoFecha
        self.archivoServicios = archivoServicios
        self.evento = Evento(fecha='', cliente='', tipoEvento='', servicios=[], precioTotal=0.0, nombreArchivo='')
        self.vista = VistaEvento()
        self.detalleEvento = DetalleEvento()
        self.vista_cliente = VistaCliente()
        self.listaEventos = []
        self.archivoCosto = archivoCosto
    
    def cargarArchivo(self):
        with open(self.archivoEventos, "r", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                linea = linea.strip().split(";")
                evento = Evento(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5])
                self.listaEventos.append(evento)
        with open(self.archivoCosto, "r", encoding="utf-8") as archivo:
            for linea in archivo.readlines():
                self.detalleEvento.setCostoAdministrativo(float(linea))
    
    def ingresarCliente(self):
        controladorCliente = ControladorCliente(self.archivoClientes)
        controladorCliente.cargarArchivo()
        if controladorCliente.consultarCliente():
            self.evento.setCliente(controladorCliente.cliente)
            self.detalleEvento.setCliente(controladorCliente.cliente)
            return True
        else:
            registrarCliente = self.vista.noSeEncontroCliente()
            if registrarCliente.upper() == "S":
                nuevoCliente = controladorCliente.registrarCliente()
                self.evento.setCliente(nuevoCliente)
                self.detalleEvento.setCliente(nuevoCliente)
                controladorCliente.guardarArchivo()
                return True
            else:
                return False
    
    def ingresarFecha(self):
        controladorFecha = ControladorFecha(self.archivoFecha)
        controladorFecha.cargarArchivo()
        controladorFecha.ingresarDia()
        controladorFecha.ingresarMes()
        controladorFecha.ingresarAnio()
        if controladorFecha.verificarDisponibilidad():
            self.evento.setFecha(controladorFecha.fecha)
            self.detalleEvento.setFecha(controladorFecha.fecha)
            return True
        else:
            fechaNueva = controladorFecha.encontrarFechaLibreCercana()
            if controladorFecha.ofrecerFecha(fechaNueva):
                controladorFecha.guardarArchivo()
                return True
            else:
                return False
    
    def ingresarTipoEvento(self):
        var1=1
        while var1<2:
            try:
                tipoEvento = self.vista.tipoEvento()
                while tipoEvento < 1 or tipoEvento > 5:
                    tipoEvento = self.vista.tipoEvento()
                match tipoEvento:
                    case 1:
                        self.evento.setTipoEvento("Casamiento")
                        self.detalleEvento.setTipoEvento("Casamiento")
                    case 2:
                        self.evento.setTipoEvento("Cumpleaños")
                        self.detalleEvento.setTipoEvento("Cumpleaños")
                    case 3:
                        self.evento.setTipoEvento("Bautismo")
                        self.detalleEvento.setTipoEvento("Bautismo")
                    case 4: 
                        self.evento.setTipoEvento("Aniversario")
                        self.detalleEvento.setTipoEvento("Aniversario")
                    case 5:
                        self.evento.setTipoEvento("Otro")
                        self.detalleEvento.setTipoEvento("Otro")
                var1=3
            except ValueError: self.vista.dato_incorrecto()
    def elegirServicios(self):
        controladorServicio = ControladorServicio(self.archivoServicios)
        controladorServicio.inicializarServicios()
        precioServicios = 0.0
        opcion = 1
        while opcion != 0:
            for linea in self.evento.getServicios():
                self.vista.limpiar_pantalla()
                self.vista.mostrar(linea)
            self.vista.mostrar(f"Precio total de los servicios seleccionados: ${precioServicios}")
            opcion = controladorServicio.elegirServicios()
            for servicio in controladorServicio.listaServicios:
                if opcion == servicio.getCodigo() and servicio.getFueElegido() == False:
                    if servicio.getCodigo() == 7:
                        servicio.setCantidad(controladorServicio.vista.cantidadServicio())
                    self.evento.setServicios(servicio.getTipoServicio())
                    self.detalleEvento.setServicios(f"{servicio.getTipoServicio()} - ${servicio.getPrecio()} - Cantidad", servicio.getCantidad())
                    precioServicios += (servicio.getPrecio() * servicio.getCantidad())
                    servicio.setFueElegido(True)
        self.detalleEvento.setCostoServicios(precioServicios)
    
    def confirmarEvento(self):
        self.detalleEvento.calcularIva()
        self.evento.setPrecioTotal(self.detalleEvento.obtenerTotal())
        self.detalleEvento.calcularSenia()
        self.vista.mostrar(self.detalleEvento)
        opcion = self.vista.confirmarEvento()
        if opcion.upper() == "S":
            self.evento.setNombreArchivo(f"{str(self.detalleEvento.getFecha()).replace('/', '-')}-{str(self.detalleEvento.getCliente()).strip().split('_')}.txt")
            self.listaEventos.append(self.evento)
            controladorFecha = ControladorFecha(self.archivoFecha)
            controladorFecha.cargarArchivo()
            controladorFecha.fechasReservadas.append(self.evento.getFecha())
            controladorFecha.guardarArchivo()
            self.guardarDetalleEvento()
            self.vista.eventoRegistrado()
            self.vista.tiempo_espera_extenso()
            self.vista.tiempo_espera()
    
    def guardarDetalleEvento(self):
        with open(f"Archivos\\Eventos\\{str(self.detalleEvento.getFecha()).replace('/', '-')}-{str(self.detalleEvento.getCliente()).strip().split('_')}.txt", 'w+', encoding='utf-8') as archivo:
            archivo.write(self.detalleEvento.__str__())

    def modificarCostoAdministrativo(self):
        opcion = self.vista.costoAdministrativo(self.detalleEvento.getCostoAdministrativo())
        if opcion.upper() == "S":
            self.detalleEvento.setCostoAdministrativo(float(self.vista.nuevoPrecio()))
    
    def guardarArchivo(self):
        with open(self.archivoEventos, "w", encoding="utf-8") as archivo:
            for evento in self.listaEventos:
                cadena = ";".join([str(evento.getFecha()), str(evento.getCliente()), str(evento.getTipoEvento()), str(evento.getServicios()), str(evento.getPrecioTotal()), str(evento.getNombreArchivo())])
                archivo.write(cadena + "\n")

    def consultarEvento(self):
        opcion = 0
        while opcion != 4:
            var1=1
            while var1<2:
                try:
                    opcion = self.vista.consultarEvento()
                    var1=3  
                except ValueError:
                    self.vista.dato_incorrecto()
            
            if opcion == 1:
                controladorFecha = ControladorFecha(self.archivoFecha)
                controladorFecha.ingresarDia()
                controladorFecha.ingresarMes()
                controladorFecha.ingresarAnio()
                fecha = datetime(controladorFecha.fecha.getAnio(), controladorFecha.fecha.getMes(), controladorFecha.fecha.getDia())
                fecha = fecha.strftime("%#d/%#m/%Y")
                for element in self.listaEventos:
                    if element.getFecha() == fecha:
                        archivo = element.getNombreArchivo()
                        with open(f"Archivos\\Eventos\\{archivo}", "r", encoding="utf-8") as file:
                            self.vista.mostrar(file.read())
            elif opcion == 2:
                clienteBuscado = ''
                encontrado = False
                controladorCliente = ControladorCliente(self.archivoClientes)
                controladorCliente.cargarArchivo()
                dni = controladorCliente.vista.dni()
                for cliente in controladorCliente.listaClientes:
                    if int(cliente.getDni()) == dni:
                        clienteBuscado = f"{cliente.getApellido()}, {cliente.getNombre()}"
                        encontrado = True
                for element in self.listaEventos:
                    if element.getCliente() == clienteBuscado:
                        archivo = element.getNombreArchivo()
                        try:
                            with open(f"Archivos\\Eventos\\{archivo}", "r", encoding="utf-8") as file:
                                self.vista.mostrar(file.read())
                                self.vista.mostrar("\n")
                        except FileNotFoundError:
                            self.vista.archivoNoEncontrado()
                if encontrado == False:
                    controladorCliente.vista.clienteNoEncontrado()
            elif opcion == 3:
                encontrado = False
                self.ingresarTipoEvento()
                for element in self.listaEventos:
                    if element.getTipoEvento() == self.evento.getTipoEvento():
                        archivo = element.getNombreArchivo()
                        with open(f"Archivos\\Eventos\\{archivo}", "r", encoding="utf-8") as file:
                            self.vista.mostrar(file.read())
                        encontrado = True
                if encontrado == False:
                    self.vista.eventoNoEncontrado()
    
    def cancelarEvento(self):
        controladorFecha = ControladorFecha(self.archivoFecha)
        controladorFecha.ingresarDia()
        controladorFecha.ingresarMes()
        controladorFecha.ingresarAnio()
        fecha = datetime(controladorFecha.fecha.getAnio(), controladorFecha.fecha.getMes(), controladorFecha.fecha.getDia())
        fecha_str = fecha.strftime("%#d/%#m/%Y")
        for element in self.listaEventos:
            if element.getFecha() == fecha_str:
                archivo = element.getNombreArchivo()
                with open(f"Archivos\\Eventos\\{archivo}", "r", encoding="utf-8") as file:
                    self.vista.mostrar(file.read())
                respuesta = self.vista.cancelarEvento()
                if respuesta.upper() == "S":
                    self.calcularReintegro(fecha, float(element.getPrecioTotal()))
                    nombreArchivo = "Archivos\\Eventos\\"+element.getNombreArchivo()
                    if os.path.exists(nombreArchivo):
                        os.remove(nombreArchivo)
                    self.listaEventos.remove(element)
                    self.guardarArchivo()
                    controladorFecha.cargarArchivo()
                    for linea in controladorFecha.fechasReservadas:
                        if linea.getDia() == controladorFecha.fecha.getDia() and linea.getMes() == controladorFecha.fecha.getMes() and linea.getAnio() == controladorFecha.fecha.getAnio():
                            controladorFecha.fechasReservadas.remove(linea)
                            controladorFecha.guardarArchivo()
                    self.vista.eventoCancelado()
    
    def calcularReintegro(self, fecha, monto):
        now = datetime.now()
        delta = timedelta(days=15)
        if fecha - delta > now:
            devolucion = (monto * 0.3) * 0.2
            self.vista.montoDevuelto(devolucion)
        else:
            self.vista.noHayDevolucion()
    
    def ejecutar(self):
        opcion = 0
        opcionEventos = 0
        opcionClientes = 0
        while opcion != 4:
            self.vista.tiempo_espera()
            var1=1
            while var1<2:
                try:
                    opcion = self.vista.menuPrincipal()
                    var1=3
                    while opcion < 1 or opcion > 4:
                        self.vista.limpiar_pantalla()
                        self.vista.dato_incorrecto()
                        self.vista.limpiar_pantalla()
                        opcion = self.vista.menuPrincipal()
                except ValueError:
                    self.vista.limpiar_pantalla()
                    self.vista.dato_incorrecto()
                    self.vista.limpiar_pantalla()
            
            if opcion == 1:
                self.vista.tiempo_espera()
                self.cargarArchivo()
                while opcionEventos != 4:
                    var1=1
                    while var1<2:
                        try:
                            opcionEventos = self.vista.menuEventos()
                            var1=3
                            while opcionEventos < 1 or opcionEventos > 4:
                                self.vista.limpiar_pantalla()
                                self.vista.dato_incorrecto()
                                self.vista.limpiar_pantalla()
                                opcionEventos = self.vista.menuEventos()
                        except ValueError:
                            self.vista.limpiar_pantalla()
                            self.vista.dato_incorrecto()
                            self.vista.limpiar_pantalla()
                    
                    if opcionEventos == 1:
                        if self.ingresarCliente():
                            if self.ingresarFecha() == True:
                                self.ingresarTipoEvento()
                                self.elegirServicios()
                                self.confirmarEvento()
                                self.guardarArchivo()
                    elif opcionEventos == 2:
                        self.consultarEvento()
                    elif opcionEventos == 3:
                        self.cancelarEvento()
            elif opcion == 2:
                self.vista.tiempo_espera()
                controladorCliente = ControladorCliente(self.archivoClientes)
                controladorCliente.cargarArchivo()
                while opcionClientes != 4:
                    var1=1
                    while var1<2:
                        try:
                            opcionClientes = controladorCliente.vista.menuClientes()
                            var1=3  
                        except ValueError:
                            self.vista.dato_incorrecto()
                    
                    while opcionClientes < 1 or opcionClientes > 4:
                        self.vista.limpiar_pantalla()
                        self.vista.dato_incorrecto()
                        self.vista.limpiar_pantalla()
                        opcionClientes = controladorCliente.vista.menuClientes()
                    if opcionClientes == 1:
                        self.vista.tiempo_espera()
                        controladorCliente.registrarCliente()
                        controladorCliente.guardarArchivo()
                    elif opcionClientes == 2:
                        self.vista.tiempo_espera()
                        controladorCliente.consultarCliente()
                        self.vista.tiempo_espera_extenso()
                        self.vista.tiempo_espera()
                    elif opcionClientes == 3:
                        self.vista.tiempo_espera()
                        controladorCliente.modificarCliente()
            
            elif opcion == 3:
                self.vista.tiempo_espera()
                opcionCostos = 0
                while opcionCostos != 3:
                    var1=1
                    while var1<2:
                        try:
                            opcionCostos = self.vista.costosPrecios()
                            var1=3  
                        except ValueError:
                            self.vista.dato_incorrecto()
                    if opcionCostos == 1:
                        opcionAdmin = self.vista.costoAdministrativo(self.detalleEvento.getCostoAdministrativo())
                        if opcionAdmin.upper() == "S":
                            self.detalleEvento.setCostoAdministrativo(self.vista.nuevoPrecio())
                            with open(self.archivoCosto, "w") as archivo:
                                archivo.write(str(self.detalleEvento.getCostoAdministrativo()))
                    elif opcionCostos == 2:
                        controladorServicio = ControladorServicio(self.archivoServicios)
                        try:
                            controladorServicio.inicializarServicios()
                        except FileNotFoundError:
                            self.vista.archivoNoEncontrado()
                            break
                        for servicio in controladorServicio.listaServicios:
                            self.vista.mostrar(f"{servicio.getCodigo()} - {servicio.getTipoServicio()} - ${servicio.getPrecio()}")
                        self.vista.mostrar("0 - Volver al menú anterior")
                        opcionServiciosPrecio = 1
                        while opcionServiciosPrecio != 0:
                            try:
                                opcionServiciosPrecio = controladorServicio.vista.seleccionarServicio()
                                while opcionServiciosPrecio < 0 or opcionServiciosPrecio > 7:
                                    opcionServiciosPrecio = controladorServicio.vista.seleccionarServicio()
                            except ValueError:
                                self.vista.dato_incorrecto()
                        for servicio in controladorServicio.listaServicios:
                            if servicio.getCodigo() == opcionServiciosPrecio:
                                try:
                                    nuevoPrecio = self.vista.nuevoPrecio()
                                    servicio.setPrecio(nuevoPrecio)
                                except ValueError:
                                    self.vista.dato_incorrecto()
                        controladorServicio.guardarArchivo()

            elif opcion == 4:
                self.vista.cerrando_programa()
                self.vista.limpiar_pantalla()