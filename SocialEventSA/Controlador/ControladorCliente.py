from Modelo.Cliente import Cliente
from Vista.VistaCliente import VistaCliente

class ControladorCliente:
    def __init__(self, archivoClientes):
        self.cliente = Cliente(apellido='', nombre='', dni=0, domicilio='', telefono=0, email='')
        self.vista = VistaCliente()
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
        nuevoCliente.setApellido(self.vista.apellido())
        nuevoCliente.setNombre(self.vista.nombre())
        nuevoCliente.setDni(self.vista.dni())
        nuevoCliente.setDomicilio(self.vista.domicilio())
        nuevoCliente.setTelefono(self.vista.telefono())
        nuevoCliente.setEmail(self.vista.email())
        self.listaClientes.append(nuevoCliente)
        self.vista.registroExitoso()
    
    def consultarCliente(self):
        encontrado = False
        dniCliente = self.vista.dni()
        for cliente in self.listaClientes:
            if cliente.getDni() == dniCliente:
                print(cliente)
                encontrado = True
        if encontrado == False:
            self.vista.clienteNoEncontrado()
