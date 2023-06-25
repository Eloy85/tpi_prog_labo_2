from Modelo.Cliente import Cliente
from Vista.VistaCliente import VistaCliente
from Vista.VistaEvento import VistaEvento

class ControladorCliente:
    def __init__(self, archivoClientes):
        self.cliente = Cliente(apellido='', nombre='', dni=0, domicilio='', telefono=0, email='')
        self.vista = VistaCliente()
        self.vistaEvento = VistaEvento()
        self.archivo = archivoClientes
        self.listaClientes = []
        self.opcion = 0
    
    def cargarArchivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    linea = line.strip().split(",")
                    self.cliente = Cliente(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5])
                    self.listaClientes.append(self.cliente)
        except FileNotFoundError:
            self.vista.archivoNoEncontrado()
    
    def registrarCliente(self):
        nuevoCliente = Cliente(apellido='', nombre='', dni=0, domicilio='', telefono=0, email='')
        self.vistaEvento.limpiar_pantalla()
        nuevoCliente.setApellido(self.vista.apellido())
        nuevoCliente.setNombre(self.vista.nombre())
        nuevoCliente.setDni(self.vista.dni())
        nuevoCliente.setDomicilio(self.vista.domicilio())
        nuevoCliente.setTelefono(self.vista.telefono())
        nuevoCliente.setEmail(self.vista.email())
        self.listaClientes.append(nuevoCliente)
        self.vista.registroExitoso()
        self.vistaEvento.limpiar_pantalla()
        self.vistaEvento.tiempo_espera()
    
    def consultarCliente(self):
        dniCliente = self.vista.dni()
        for cliente in self.listaClientes:
            if int(cliente.getDni()) == dniCliente:
                self.vista.mostrar(str(cliente.getApellido())+", "+str(cliente.getNombre())+", "+str(cliente.getDomicilio())+", "+str(cliente.getTelefono())+", "+str(cliente.getEmail()))
                self.cliente = cliente
                return True
        self.vista.clienteNoEncontrado()
        self.vistaEvento.limpiar_pantalla()
        self.vistaEvento.tiempo_espera()
        return False

    def guardarArchivo(self):
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            for cliente in self.listaClientes:
                archivo.write(str(cliente.getApellido()) + "," + str(cliente.getNombre()) + "," + str(cliente.getDni()) + "," + str(cliente.getDomicilio()) + "," + str(cliente.getTelefono()) + "," + str(cliente.getEmail()) + "\n")