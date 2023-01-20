from datetime import datetime, timedelta


def ticket_entrada_temporal(plaza):
    print("TICKET")
    print("Matícula: " + plaza.vehiculo.matricula)
    print("Fecha de Entrada: " + str(plaza.vehiculo.cliente.ticket.fecha_alta))
    print("Precio minuto: " + str(plaza.precio) + "€")
    print("PIN: " + str(plaza.vehiculo.cliente.ticket.pin))


def ticket_salida_temporal(plaza):
    print("TICKET")
    print("Id Plaza: " + str(plaza.idPlaza))
    print("Matrícula: " + plaza.vehiculo.matricula)
    print("Fecha de Entrada: " + str(plaza.vehiculo.cliente.ticket.fecha_alta))
    print("Fecha de Salida: " + str(plaza.vehiculo.cliente.ticket.fecha_baja))
    print("Precio minuto: " + f"{plaza.precio:.2f}" + "€")
    print("Total: " + f"{plaza.vehiculo.cliente.ticket.precio :.2f}" + '€')  # Calcular total a pagar


def ticket_alta_abonado(plaza):
    print("TICKET")
    print("Matrícula: " + str(plaza.vehiculo.matricula))
    print("Nombre: " + plaza.vehiculo.cliente.nombre)
    print("Apelidos: " + str(plaza.vehiculo.cliente.apellidos))
    print("DNI: " + str(plaza.vehiculo.cliente.dni))
    print("Email: " + str(plaza.vehiculo.cliente.email))
    print("Pin: " + str(plaza.vehiculo.cliente.ticket.pin))
    print("Fecha de Entrada: " + str(plaza.vehiculo.cliente.ticket.fecha_alta))
    print("Fecha de Salida: " + str(plaza.vehiculo.cliente.ticket.fecha_baja))
    print("Total: " + f"{plaza.vehiculo.cliente.ticket.precio:.2f}" + "€")  # Calcular total a pagar
