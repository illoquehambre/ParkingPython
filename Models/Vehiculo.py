from enum import Enum

from Models.Cliente import Cliente


class Vehiculo:
    def __init__(self, matricula, cliente=Cliente):
        self.__matricula = matricula
        self.__cliente = cliente

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, nueva_matricula):
        self.__matricula = nueva_matricula

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, nuevo_cliente):
        self.__cliente = nuevo_cliente
    def __str__(self):
        return '{} {}'.format(self.matricula, self.cliente)
