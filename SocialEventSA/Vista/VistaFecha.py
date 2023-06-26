import os
import time

class VistaFecha:
    def ingresarDia(self):
        return int(input("Ingrese el día a realizar el evento: "))
    
    def ingresarMes(self):
        return int(input("Ingrese el mes a realizar el evento: "))
    
    def ingresarAnio(self):
        return int(input("Ingrese el año a realizar el evento: "))
    
    def valorIncorrecto(self):
        print("¡Error!: Valor ingresado incorrecto.")
    
    def mostrarFecha(self, fecha):
        print(f"¡La fecha seleccionada está ocupada! -> La fecha más próxima disponible es {fecha}.")
    
    def confirmarFechaProxima(self):
        respuesta = input("¿Desea reservar esta fecha? S/N: ")
        return respuesta.upper() == "S"
    
    def reservaExitosa(self):
        print("¡Reserva Exitosa!")
    
    def reservaCancelada(self):
        print("Reserva Cancelada.")

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

    def tiempo_espera_extenso(self):
        time.sleep(5)
        os.system("cls")