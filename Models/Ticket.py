class Ticket:
    def __init__(self, fecha_alta, fecha_baja, precio, pin):
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
        self.precio = precio
        self.pin = pin

    def __str__(self):
        return '{} {}'.format(self.fecha_alta, self.fecha_baja, self.precio, self.pin)
