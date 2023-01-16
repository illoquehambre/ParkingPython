class Cliente:
    def __init__(self, vehiculo, ticket):
        self.id = id
        self.vehiculo = vehiculo
        self.ticket = ticket

    def __str__(self):
        return '{} {}'.format(self.id,  self.vehiculo, self.ticket)
