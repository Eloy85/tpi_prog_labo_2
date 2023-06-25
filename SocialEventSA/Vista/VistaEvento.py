import os
import time

class VistaEvento:
    def menuPrincipal(self):
        print(f".{'-':-^46}.")
        print(f"|{'-SISTEMA DE ADMINISTRACION DE EVENTOS-': ^46}|")
        print(f"|{'-':-^46}|")
        print(f"|{'1- Eventos.': >26}                    |")
        print(f"|{'2- Clientes.': >27}                   |")
        print(f"|{'3- Costos/Precios.': >33}             |")
        print(f"|{'4- Salir.': >24}                      |")
        print(f"|{'_':_^46}|")
        return int(input("Ingrese la opción deseada (1/2/3/4): "))

    def menuEventos(self):
        print(f".{'-':-^46}.")
        print(f"|{'-MENU EVENTOS-': ^46}|")
        print(f"|{'-':-^46}|")
        print(f"|{'1- Registrar nuevo evento.': >35}           |")
        print(f"|{'2- Consultar evento.': >29}                 |")
        print(f"|{'3- Cancelar evento.': >28}                  |")
        print(f"|{'4- Volver al menú principal.': >37}         |")
        print(f"|{'_':_^46}|")
        return int(input("Ingrese la opción deseada (1/2/3/4): "))
    
    def noSeEncontroCliente(self):
        return input("No se encontró el cliente ingresado. ¿Desea registrarlo? S/N: ")
    
    def tipoEvento(self):
        print(f".{'-':-^46}.")
        print(f"|{'-TIPO DE EVENTO-': ^46}|")
        print(f"|{'-':-^46}|")
        print(f"|{'1- Casamiento.': >30}                |")
        print(f"|{'2- Cumpleaños.': >30}                |")
        print(f"|{'3- Bautismo.': >28}                  |")
        print(f"|{'4- Aniversario.': >31}               |")
        print(f"|{'5- Otro.': >24}                      |")
        print(f"|{'_':_^46}|")
        return int(input("Ingrese su opción (1/2/3/4/5): "))
    
    def mostrar(self, dato):
        print(dato)
    
    def confirmarEvento(self):
        return input("¿Desea confirmar el evento? S/N: ")
    
    def eventoRegistrado(self):
        print("¡El evento se registró exitosamente!")
    
    def costosPrecios(self):
        print(f".{'-':-^46}.")
        print(f"|{'-PRECIOS-': ^46}|")
        print(f"|{'-':-^46}|")
        print(f"|{'1- Modificar precio del costo administrativo.': >0} |")
        print(f"|{'2- Modificar precio de los servicios.': >0}         |")
        print(f"|{'3- Modificar estado de los servicios.': >0}         |")
        print(f"|{'4- Volver al menú principal.': >0}                  |")
        print(f"|{'_':_^46}|")
        return int(input("Ingrese su opción (1/2/3/4): "))
    
    def costoAdministrativo(self, precio):
        print(f"El costo administrativo actual está establecido en ${precio}")
        return input("¿Desea modificarlo? S/N: ")
    
    def nuevoPrecio(self):
        return float(input("Ingrese el nuevo precio: "))
    
    def consultarEvento(self):
        print(f".{'-':-^46}.")
        print(f"|{'-CONSULTAR EVENTO-': ^46}|")
        print(f"|{'-':-^46}|")
        print(f"|{'1- Consultar por fecha.': >31}               |")
        print(f"|{'2- Consultar por cliente.': >33}             |")
        print(f"|{'3- Consultar por tipo de evento.': >40}      |")
        print(f"|{'4- Volver al menú principal.': >36}          |")
        print(f"|{'_':_^46}|")
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

    def cerrando_programa(self):
        print(f".{'-':-^46}.")
        print(f"|{'-CERRANDO PROGRAMA-': ^46}|")
        print(f"|{'_':_^46}|")

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
    def valorIncorrecto(self):
        print("¡Error!: Valor ingresado incorrecto.")
