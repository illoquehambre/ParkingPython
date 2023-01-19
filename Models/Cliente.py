from Models.Ticket import Ticket


class Cliente:
    def __init__(self, ticket=Ticket):
        self.__ticket = ticket

    @property
    def ticket(self):
        return self.__ticket

    @ticket.setter
    def ticket(self, nuevo_ticket):
        self.__ticket = nuevo_ticket

    def __str__(self):
        return '{} {}'.format(self.ticket)

