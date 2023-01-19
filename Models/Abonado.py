from Models.Cliente import Cliente


class Abonado(Cliente):
    def __init__(self, ticket, nombre, apellidos, dni, email, tarjeta):
        super().__init__(ticket)
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__email = email
        self.__tarjeta = tarjeta

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, nuevo_apellido):
        self.__apellidos = nuevo_apellido

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo_dni):
        self.__dni = nuevo_dni

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email

    @property
    def tarjeta(self):
        return self.__tarjeta

    @tarjeta.setter
    def tarjeta(self, nuevo_tarjeta):
        self.__tarjeta = nuevo_tarjeta
    def __str__(self):
        return '{} {}'.format(self.id, self.nombre, self.apellidos, self.dni, self.email, self.tarjeta)
