class VistaCliente:
    def menuClientes(self):
        print(f"°{'MENU CLIENTES':-^46}°")
        print(f"{'1- Registrar nuevo cliente.': >37}")
        print(f"{'2- Consultar cliente.': >31}")
        print(f"{'3- Modificar datos de cliente.': >40}")
        print(f"{'4- Volver al menú principal.': >38}")
        print(f"°{'-':-^46}°")
        return int(input("Ingrese la opción deseada (1/2/3/4): "))
    
    def archivoNoEncontrado(self):
        print("No se encontró ningún archivo de clientes. Se creará uno nuevo.")
    
    def apellido(self):
        return input("Ingrese el apellido: ")
    
    def nombre(self):
        return input("Ingrese el nombre: ")
    
    def dni(self):
        return int(input("Ingrese el número de DNI del cliente: "))
    
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
    
    def mostrar(self, dato):
        print(dato)