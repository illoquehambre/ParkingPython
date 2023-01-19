from enum import Enum

from Models.Cliente import Cliente


class Vehiculo:
    def __init__(self, matricula, cliente=Cliente):
        self.matricula = matricula
        self.cliente = cliente

    def __str__(self):
        return '{} {}'.format(self.matricula, self.cliente)
