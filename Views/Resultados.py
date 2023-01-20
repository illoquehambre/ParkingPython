from Models.Abonado import Abonado
from Models.Plaza import Plaza


def mostrar_abonados(listado):
    for a in listado:
        if type(a) == Abonado:
            print("Nombre: " + str(a.nombre) + ', ' + "Apellidos: " + str(a.apellidos)
                  + ', ' + "DNI: " + str(a.dni)
                  + ', '"Email: " + str(a.email) + ', ' + "Tarjeta: " + str(a.tarjeta) + ',\n'
                  + ', '"Fecha_entrada: " + str(a.ticket.fecha_alta) + ', '
                  + "Fecha baja: " + str(a.ticket.fecha_baja) + ',\n'
                  + "Total: " + str(a.ticket.precio) + '€')
