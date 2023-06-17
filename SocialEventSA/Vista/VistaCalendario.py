class VistaCalendario:
    def mostrar_mes(self,ruta):
        archivo=open(str(ruta),"r",encoding="utf-8")
        conten=archivo.read()
        archivo.close()
        print(conten) 
    def ingresar_año(self):
        return input("Año a realizar evento: ")
    def ingresar_mes(self):
        return input("Mes a realizar evento: ")
    def ingresar_dia(self):
        return input("Dia a realizar evento: ")