from Controlador.ControladorFecha import ControladorFecha
from Controlador.ControladorServicio import ControladorServicio
from Controlador.ControladorEvento import ControladorEvento

if __name__ == "__main__":
#    controller = ControladorFecha("reservas.txt")
#    controller.cargarArchivo()
#    controller.ingresarDia()
#    controller.ingresarMes()
#    controller.ingresarAnio()
#    controller.verificarDisponibilidad()
#    controller.guardarArchivo()
#    controller = ControladorServicio("servicios.txt")
#    controller.inicializarServicios()
    controller = ControladorEvento("")
    opcion = controller.vista.menuPrincipal()