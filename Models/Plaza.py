
from Models import Vehiculo


class Plaza:
    def __init__(self, idPlaza, tipo, precio, ocupado, reservado, vehiculo=Vehiculo):
        self.__idPlaza = idPlaza
        self.__tipo = tipo
        self.__precio = precio
        self.__ocupado = ocupado
        self.__reservado = reservado
        self.__vehiculo = vehiculo

    @property
    def idPlaza(self):
        return self.__idPlaza

    @idPlaza.setter
    def idPlaza(self, nueva_idPlaza):
        self.__idPlaza = nueva_idPlaza

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nueva_precio):
        self.__precio = nueva_precio

    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, nuevo_ocupado):
        self.__ocupado = nuevo_ocupado

    @property
    def reservado(self):
        return self.__reservado

    @reservado.setter
    def reservado(self, nueva_reservado):
        self.__reservado = nueva_reservado

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, nuevo_vehiculo):
        self.__vehiculo= nuevo_vehiculo
    def __str__(self):
        return '{} {}'.format(self.idPlaza, self.tipo, self.tipo, self.precio, self.ocupado, self.vehiculo)
