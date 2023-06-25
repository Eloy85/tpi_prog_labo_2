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