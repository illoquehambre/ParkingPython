class Plaza:
    def __init__(self, tipo, precio, vehiculo, vacio, disponible):
        self.id = id
        self.tipo = tipo
        self.precio = precio
        self.vehiculo = vehiculo
        self.vacio = vacio
        self.disponible = disponible

    def __str__(self):
        return '{} {}'.format(self.id, self.tipo, self.precio, self.vehiculo, self.vacio, self.disponible)
