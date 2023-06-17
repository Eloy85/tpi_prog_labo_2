class VistaCalendario:
    def __init__(self):
        pass
    
    def mostrar_mes(self,ruta):
        archivo=open(str(ruta),"r",encoding="utf-8")
        conten=archivo.read()
        archivo.close()
        print(conten) 

    def ingresar_año(self):
        return int(input("Año a realizar evento: "))

    def ingresar_mes(self):
        return int(input("Mes a realizar evento: "))

    def ingresar_dia(self):
        return int(input("Dia a realizar evento: "))