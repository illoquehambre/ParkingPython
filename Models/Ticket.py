class Ticket:
    def __init__(self, fecha_alta, fecha_baja, pin, precio=float):
        self.__fecha_alta = fecha_alta
        self.__fecha_baja = fecha_baja
        self.__precio = precio
        self.__pin = pin

    @property
    def fecha_alta(self):
        return self.__fecha_alta

    @fecha_alta.setter
    def fecha_alta(self, nuevo_fecha_alta):
        self.__fecha_alta = nuevo_fecha_alta

    @property
    def fecha_baja(self):
        return self.__fecha_baja
    @fecha_baja.setter
    def fecha_baja(self, nuevo_fecha_baja):
        self.__fecha_baja = nuevo_fecha_baja

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, nuevo_pinl):
        self.__pin = nuevo_pinl

    def __str__(self):
        return '{} {}'.format(self.fecha_alta, self.fecha_baja, self.precio, self.pin)
