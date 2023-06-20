class VistaEvento:
    def menuPrincipal(self):
        print(f"{'SISTEMA DE ADMINISTRACION DE EVENTOS':-^46}") # este tipo de format sirve para agregarle al costado caracteres
        print("1- Eventos")
        print("2- Clientes")
        print("3- Salir")
        return input("Ingrese la opción deseada (1/2/3): ")

    def menuEventos(self):
        print("1- Registrar nuevo evento")
        print("2- Consultar evento")
        print("3- Modificar evento")
        print("4- Cancelar evento")
        print("5- Volver al menú principal")
        return input("Ingrese la opción deseada (1/2/3/4/5): ")
    
    