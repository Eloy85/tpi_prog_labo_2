from Modelo.Servicio import Servicio
from Vista.VistaServicio import VistaServicio

class ControladorServicio:
    def __init__(self, archivo):
        self.archivo = archivo
        self.vista = VistaServicio()
        self.servicio = Servicio()
        self.listaServicios = []
    
    def inicializarServicios(self):
        with open(self.archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                atributos = linea.strip().split(";")
                self.servicio = Servicio(int(atributos[0]), atributos[1], atributos[2], bool(atributos[3]), float(atributos[4]), False, 1)
                self.listaServicios.append(self.servicio)
    
    def elegirServicios(self):
        for servicio in self.listaServicios:
            if servicio.getDisponibilidad() == True and servicio.getFueElegido() == False:
                self.vista.mostrarServicio(str(servicio.getCodigo())+" - "+servicio.getTipoServicio()+" - "+servicio.getDescripcion()+" - $"+str(servicio.getPrecio()))
        var1=1
        while var1<2:
            try:
                opcionServicio = self.vista.elegirServicios()
                var1=3  
            except ValueError:
                self.vista.valorIncorrecto()        
        
        return opcionServicio
    
    def modificarPrecioServicios(self):
        for servicio in self.listaServicios:
            self.vista.mostrarServicio(str(servicio.getCodigo())+" - "+servicio.getTipoServicio()+" - "+servicio.getDescripcion()+" - $"+str(servicio.getPrecio()))
        opcion = self.vista.seleccionarServicio()
        for servicio in self.listaServicios:
            if opcion == servicio.getCodigo():
                servicio.setPrecio(self.vista.precioServicio())
    
    def modificarEstadoServicio(self):
        for servicio in self.listaServicios:
            self.vista.mostrarServicio(str(servicio.getCodigo())+" - "+servicio.getTipoServicio()+" - "+servicio.getDescripcion()+" - Estado: "+str(int(servicio.getEstado())))
        opcion = self.vista.seleccionarServicio()
        for servicio in self.listaServicios:
            if opcion == servicio.getCodigo():
                servicio.setEstado(self.vista.estadoServicio())
    
    def guardarArchivo(self):
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            for servicio in self.listaServicios:
                archivo.write(str(servicio))
                archivo.write("\n")