import os
import time

class VistaEvento:
    def menuPrincipal(self):
        print(f".{'-':-^46}.")
        print(f"|{'SISTEMA DE ADMINISTRACION DE EVENTOS': ^46}|") # este tipo de format sirve para agregarle al costado caracteres
        print(f"|{'-':-^46}|")
        print(f"|{'1- Eventos.': ^41}     |")
        print(f"|{'2- Clientes.': ^42}    |")
        print(f"|{'3- Costos/Precios.': >33}             |")
        print(f"|{'4- Salir.': ^39}       |")
        print(f"|{'_':_^46}|")
        return int(input("Ingrese la opción deseada (1/2/3/4): "))

    def menuEventos(self):
        print(f"°{'MENU EVENTOS':-^46}°")
        print(f"{'1- Registrar nuevo evento.': >35}")
        print(f"{'2- Consultar evento.': >29}")
        print(f"{'3- Cancelar evento.': >28}")
        print(f"{'4- Volver al menú principal.': >37}")
        print(f"°{'-':-^46}°")
        return int(input("Ingrese la opción deseada (1/2/3/4): "))
    
    def noSeEncontroCliente(self):
        return input("No se encontró el cliente ingresado. ¿Desea registrarlo? S/N: ")
    
    def tipoEvento(self):
        print(f"°{'TIPO DE EVENTO':-^46}°")
        print(f"{'1- Casamiento.': >31}")
        print(f"{'2- Cumpleaños.': >31}")
        print(f"{'3- Bautismo.': >29}")
        print(f"{'4- Aniversario.': >32}")
        print(f"{'5- Otro.': >25}")
        print(f"°{'-':-^46}°")
        return int(input("Ingrese su opción (1/2/3/4/5): "))
    
    def mostrar(self, dato):
        print(dato)
    
    def confirmarEvento(self):
        return input("¿Desea confirmar el evento? S/N: ")
    
    def eventoRegistrado(self):
        print("¡El evento se registró exitosamente!")
    
    def costosPrecios(self):
        print("1- Modificar el precio del costo administrativo")
        print("2- Modificar el precio de los servicios")
        print("3- Modificar el estado de los servicios")
        print("4- Volver al menú principal")
        return int(input("Ingrese su opción (1/2/3/4): "))
    
    def costoAdministrativo(self, precio):
        print(f"El costo administrativo actual está establecido en ${precio}")
        return input("¿Desea modificarlo? S/N: ")
    
    def nuevoPrecio(self):
        return input("Ingrese el nuevo precio: ")
    
    def consultarEvento(self):
        print("1- Consultar por fecha")
        print("2- Consultar por cliente")
        print("3- Consultar por tipo de evento")
        print("4- Volver al menú principal")
        return int(input("Ingrese su opción (1/2/3/4): "))
    
    def eventoNoEncontrado(self):
        print("No se encontraron eventos de este tipo.")
    
    def cancelarEvento(self):
        return input("¿Desea cancelar el evento? S/N: ")
    
    def eventoCancelado(self):
        print("¡El evento se canceló exitosamente!")
    
    def montoDevuelto(self, monto):
        print(f"El monto a devolver al cliente es ${monto}")
    
    def noHayDevolucion(self):
        print("No corresponde devolver dinero al cliente ya que la cancelación no se realizó con 15 días de anticipación.")

    def tiempo_espera(self):
        os.system("cls")
        for i in range(1):
            print("Cargando.")
            time.sleep(0.5)
            os.system("cls")
            print("Cargando..")
            time.sleep(0.5)
            os.system("cls")
            print("Cargando...")
            time.sleep(0.5)
            os.system("cls")

    def limpiar_pantalla(self):
        time.sleep(1.5)
        os.system("cls")