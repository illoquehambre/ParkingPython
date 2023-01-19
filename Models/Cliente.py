from Models.Ticket import Ticket


class Cliente:
    def __init__(self, ticket=Ticket):
        self.id = id
        self.ticket = ticket

    def __str__(self):
        return '{} {}'.format(self.id, self.ticket)
