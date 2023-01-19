from datetime import datetime, timedelta


def ticket_entrada_temporal(plaza):
    print("TICKET")
    print("Matícula: " + plaza.vehiculo.matricula)
    print("Fecha de Entrada: " + str(plaza.vehiculo.cliente.ticket.fecha_alta))
    print("Precio minuto: " + str(plaza.precio) + "€")
    print("PIN: " + str(plaza.vehiculo.cliente.ticket.pin))


def ticket_salida_temporal(plaza):
    print("TICKET")
    print("Matícula: " + plaza.vehiculo.matricula)
    print("Fecha de Entrada: " + str(plaza.vehiculo.cliente.ticket.fecha_alta))
    print("Fecha de Salida: " + str(plaza.vehiculo.cliente.ticket.fecha_baja))
    tiempo_total = (plaza.vehiculo.cliente.ticket.fecha_baja - plaza.vehiculo.cliente.ticket.fecha_alta)
    print("Tiempo total: " + f"{(tiempo_total.total_seconds()/60):.2f}"+'mins')
    print("Precio minuto: " + f"{plaza.precio:.2f}" + "€")
    print("Total: " + f"{((tiempo_total.total_seconds()/60)*plaza.precio):.2f}"+'€')  # Calcular total a pagar
