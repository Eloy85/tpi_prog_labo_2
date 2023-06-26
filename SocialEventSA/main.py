from Controlador.ControladorEvento import ControladorEvento

if __name__ == "__main__":
    controller = ControladorEvento("Archivos\\eventos.txt", "Archivos\\clientes.txt", "Archivos\\reservas.txt", "Archivos\\servicios.txt", "Archivos\\costo_administrativo.txt")
    controller.ejecutar()
