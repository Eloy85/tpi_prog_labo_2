class VistaFecha:
    def ingresarDia(self):
        return int(input("Ingrese el día: "))
    
    def ingresarMes(self):
        return int(input("Ingrese el mes: "))
    
    def ingresarAnio(self):
        return int(input("Ingrese el año: "))
    
    def valorIncorrecto(self):
        print("Error, valor ingresado incorrecto.")
    
    def mostrarFecha(self, fecha):
        print(f"La fecha seleccionada está ocupada. La más próxima disponible es el {fecha}.")
    
    def confirmarFechaProxima(self):
        respuesta = input("¿Desea reservar esta fecha? S/N: ")
        return respuesta.upper() == "S"
    
    def reservaExitosa(self):
        print("Reserva exitosa.")
    
    def reservaCancelada(self):
        print("Reserva cancelada.")