class VistaEvento:
    def menuPrincipal(self):
        print(f"{'SISTEMA DE ADMINISTRACION DE EVENTOS':-^46}") # este tipo de format sirve para agregarle al costado caracteres
        print("1- Eventos")
        print("2- Clientes")
        print("3- Salir")
        return int(input("Ingrese la opción deseada (1/2/3): "))

    def menuEventos(self):
        print("1- Registrar nuevo evento")
        print("2- Consultar evento")
        print("3- Modificar evento")
        print("4- Cancelar evento")
        print("5- Volver al menú principal")
        return int(input("Ingrese la opción deseada (1/2/3/4/5): "))
    
    def noSeEncontroCliente(self):
        return input("No se encontró el cliente ingresado. ¿Desea registrarlo? S/N: ")
    
    def tipoEvento(self):
        print("Seleccione el tipo de evento que desea realizar:")
        print("1- Casamiento")
        print("2- Cumpleaños")
        print("3- Bautismo")
        print("4- Aniversario")
        print("5- Otro")
        return int(input("Ingrese su opción (1/2/3/4/5): "))
    
    def mostrar(self, dato):
        print(dato)
    
    def confirmarEvento(self):
        return input("¿Desea confirmar el evento? S/N: ")
    
    def eventoRegistrado(self):
        print("¡El evento se registró exitosamente!")