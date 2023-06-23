from Controlador.ControladorEvento import ControladorEvento

if __name__ == "__main__":
    controller = ControladorEvento("eventos.txt", "clientes.txt", "reservas.txt", "servicios.txt")
    controller.ejecutar()
