class VistaCliente:
    def menuClientes(self):
        print(f".{'-':-^46}.")
        print(f"|{'-MENU CLIENTES-': ^46}|")
        print(f"|{'-':-^46}|")
        print(f"|{'1- Registrar nuevo cliente.': >37}         |")
        print(f"|{'2- Consultar cliente.': >31}               |")
        print(f"|{'3- Modificar datos de cliente.': >40}      |")
        print(f"|{'4- Volver al menú principal.': >38}        |")
        print(f"|{'_':_^46}|")
        return int(input("Ingrese la opción deseada (1/2/3/4): "))
    
    def archivoNoEncontrado(self):
        print("No se encontró ningún archivo de clientes. Se creará uno nuevo.")
    
    def apellido(self):
        return input("Ingrese el apellido del cliente: ")
    
    def nombre(self):
        return input("Ingrese el nombre del cliente: ")
    
    def dni(self):
        return int(input("Ingrese el número de DNI del cliente: "))
    
    def domicilio(self):
        return input("Ingrese el domicilio del cliente: ")
    
    def telefono(self):
        return int(input("Ingrese el teléfono del cliente: "))
    
    def email(self):
        return input("Ingrese el email del cliente: ")
    
    def datoInvalido(self):
        print("¡Error!: Dato ingresado no válido.")
    
    def registroExitoso(self):
        print("¡El cliente se ha registrado exitosamente!")
    
    def clienteNoEncontrado(self):
        print("No se encontró el cliente.")
    
    def mostrar(self, dato):
        print(dato)
    
    def menuModificarCliente(self):
        print(f"{'1- Modificar apellido.': >37}")
        print(f"{'2- Modificar nombre.': >31}")
        print(f"{'3- Modificar DNI.': >40}")
        print(f"{'4- Modificar domicilio.': >38}")
        print(f"{'5- Modificar teléfono.': >38}")
        print(f"{'6- Modificar email.': >38}")
        print(f"{'7- Volver al menú principal.': >38}")
        return int(input("Ingrese la opción deseada (1-7): "))