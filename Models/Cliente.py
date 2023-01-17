class Cliente:
    def __init__(self, ticket):
        self.id = id
        self.ticket = ticket

    def __str__(self):
        return '{} {}'.format(self.id, self.ticket)
