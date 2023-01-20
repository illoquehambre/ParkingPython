from datetime import datetime, timedelta

from Models.Abonado import Abonado


def find_matricula(plazas, matricula):
    for p in plazas:
        if p.vehiculo.matricula == matricula:
            return False
    return True


def find_caducados_por_mes(mes, plazas):
    listadoAbonados = []
    if int(mes) < 10:
        mes = 0+mes
    for p in plazas:
        if type(p.vehiculo.cliente) == Abonado and p.vehiculo.cliente.ticket.fecha_baja.strftime('%m') == mes:
            listadoAbonados.append(p)
    return listadoAbonados

def find_caducados_proximos(plazas):
    listadoAbonados = []
    for p in plazas:
        if type(p.vehiculo.cliente) == Abonado \
                and datetime.now() < p.vehiculo.cliente.ticket.fecha_baja > (datetime.now() + timedelta(days=10)):
            listadoAbonados.append(p)
    return listadoAbonados