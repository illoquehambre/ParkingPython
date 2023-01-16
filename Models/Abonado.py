from Models.Cliente import Cliente


class Abonado(Cliente):
    nombre = ""
    apellidos = ""
    dni = ""
    email = ""
    tarjeta = ""

    def __str__(self):
        return '{} {}'.format(self.id, self.nombre, self.apellidos, self.dni, self.email, self.tarjeta)
