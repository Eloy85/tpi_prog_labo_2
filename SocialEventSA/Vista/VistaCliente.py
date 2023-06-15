class VistaCliente:
    def menuClientes(self):
        print("1- Registrar nuevo cliente")
        print("2- Consultar cliente")
        print("3- Modificar datos de cliente")
        print("4- Volver al menú principal")
        return input("Ingrese la opción deseada (1/2/3/4): ")
    
    def archivoNoEncontrado(self):
        print("No se encontró ningún archivo de clientes. Se creará uno nuevo.")
    
    def apellido(self):
        return input("Ingrese el apellido: ")
    
    def nombre(self):
        return input("Ingrese el nombre: ")
    
    def dni(self):
        return int(input("Ingrese el número de DNI: "))
    
    def domicilio(self):
        return input("Ingrese el domicilio: ")
    
    def telefono(self):
        return int(input("Ingrese el teléfono: "))
    
    def email(self):
        return input("Ingrese el email: ")
    
    def datoInvalido(self):
        print("Error, dato ingresado no válido.")
    
    def registroExitoso(self):
        print("El cliente se ha registrado exitosamente.")
    
    def clienteNoEncontrado(self):
        print("No se encontró el cliente.")