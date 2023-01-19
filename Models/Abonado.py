from Models.Cliente import Cliente


class Abonado(Cliente):
    def __init__(self, ticket, nombre, apellidos, dni, email, tarjeta):
        super().__init__(ticket)
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.email = email
        self.tarjeta = tarjeta

    def __str__(self):
        return '{} {}'.format(self.id, self.nombre, self.apellidos, self.dni, self.email, self.tarjeta)
