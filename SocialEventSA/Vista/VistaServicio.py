class VistaServicio:
    def mostrarServicio(self, servicio):
        print(servicio)
    
    def elegirServicios(self):
        return int(input("Ingrese el número del servicio que desea agregar o ingrese 0 para terminar: "))
    
    def seleccionarServicio(self):
        return int(input("Ingrese el número del servicio al que desea modificar: "))
    
    def precioServicio(self):
        return float(input("Ingrese el nuevo precio: "))
    
    def estadoServicio(self):
        print("El estado del servicio fue cambiado con éxito.")
    
    def cantidadServicio(self):
        return int(input("Ingrese la cantidad que desea contratar de este servicio: "))
    
    def valorIncorrecto(self):
        print("¡Error!: Valor ingresado incorrecto.")
