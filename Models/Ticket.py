class Ticket:
    def __init__(self, fecha_alta, fecha_baja, precio):
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
        self.precio = precio

    def __str__(self):
        return '{} {}'.format(self.matricula, self.tipo)
