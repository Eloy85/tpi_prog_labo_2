class Cliente:
    def __init__(self, apellido, nombre, dni, domicilio, telefono, email):
        self._apellido = apellido
        self._nombre = nombre
        self._dni = dni
        self._domicilio = domicilio
        self._telefono = telefono
        self._email = email
    
    def get_apellido(self):
        return self._apellido
    
    def set_apellido(self, apellido):
        self._apellido = apellido
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_dni(self):
        return self._dni
    
    def set_dni(self, dni):
        self._dni = dni
    
    def get_domicilio(self):
        return self._domicilio
    
    def set_domicilio(self, domicilio):
        self._domicilio = domicilio
    
    def get_telefono(self):
        return self._telefono
    
    def set_telefono(self, telefono):
        self._telefono = telefono
    
    def get_email(self):
        return self._email
    
    def set_email(self, email):
        self._email = email
    