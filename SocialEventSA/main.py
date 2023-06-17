from Controlador.ControladorFecha import ControladorFecha

if __name__ == "__main__":
    controller = ControladorFecha("reservas.txt")
    controller.cargarArchivo()
    controller.ingresarDia()
    controller.ingresarMes()
    controller.ingresarAnio()
    controller.verificarDisponibilidad()