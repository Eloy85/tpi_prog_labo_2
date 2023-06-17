class VistaCalendario:
    def mostrar_mes(self,ruta):
        archivo=open(str(ruta),"r",encoding="utf-8")
        conten=archivo.read()
        archivo.close()
        print(conten) 
        