def main_menu():
    print("Bienvenido al Parking Salesianos San Pedro")
    print("Introduzca 1 si usted es administrador o cualquier otro numero si es Usuario")


def menu_acciones_usuario():
    print("Bienvenido usuario elija las siguientes opciones marcando el respectivo número por pantalla")
    print("1 - Generar un nuevo bono para estacionar por largos periodos de tiempo")
    print("2 - Estacionar de forma temporal")
    print("3 - Ingresar con un abono activo")
    print("4 - Retirar vehiculo")
    print("Cualquier otro número - Volver a inicio")


def menu_acciones_admin():
    print("Zona Admin")
    print("Bienvenido esclavo, hora de trabajar")
    print("Indique que gestiones desea realizar: ")
    print("0 - Cerrar programa")
    print("1 - Consultar estado del parking")
    print("2 - Consultar Facturación")
    print("3 - Consultar Abonados")
    print("4 - Gestionar abonos")
    print("5 - Comprobar caducidad Abonos")


def menu_ingreso_temporal(lista):
    turismo = 0
    moto = 0
    movilidad_reducida = 0
    print("Estacionar de forma temporal")
    for i in lista:
        if i.tipo.value == 1 and not (i.ocupado or i.reservado):
            turismo += 1
        elif i.tipo.value == 2 and not (i.ocupado or i.reservado):
            moto += 1
        elif i.tipo.value == 3 and not (i.ocupado or i.reservado):
            movilidad_reducida += 1
    print("Indique que tipo de vehiculo tiene")
    print("1 - Turismo - Plazas disponibles: " + str(turismo))
    print("2 - Moto - Plazas disponibles: " + str(moto))
    print("3 - Movilidad Reducida - Plazas disponibles: " + str(movilidad_reducida))


def retirar_vehiculo():
    print("Retirar vehículo")
    print("Pulse:")
    print("1 - Salida Abonado")
    print("2 - Salida cliente normal")
    print("Cualquier otro número - Volver atrás")


def gestiones_abonado():
    print("Indique que gestiones desea realizar: ")
    print("1 - Dar de alta un Abonado")
    print("2 - Modificar un abonado")
    print("3 - Dar de baja un abonado")
