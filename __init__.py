import random
from typing import List
from Models.Abonado import Abonado
from Models.Cliente import Cliente
from Models.Plaza import Plaza
from Models.Ticket import Ticket
from Models.Tipo import Tipo
from Models.Vehiculo import Vehiculo
from datetime import datetime, timedelta

from Views.Menu import main_menu, menu_acciones_usuario, menu_ingreso_temporal, retirar_vehiculo
from Views.Ticket import ticket_entrada_temporal, ticket_salida_temporal, ticket_alta_abonado

decision = 0
numPlazas = 40
seguir = True
porcentajeTurismo = 70
porcentajeMoto = 15
porcentajeMovilidadReducidad = 15
listPlazas = []
listVehiculos = []
listClientes: List[Cliente] = []
listTicket = []
encontrado = False
for i in range(numPlazas):
    if i < numPlazas * (porcentajeTurismo / 100):
        listPlazas.append(
            Plaza(precio=0.12, ocupado=False, reservado=False, tipo=Tipo.Turismo, vehiculo=None, idPlaza=i))
    elif i < (numPlazas * ((porcentajeMoto + porcentajeTurismo) / 100)):
        listPlazas.append(
            Plaza(tipo=Tipo.Moto, precio=0.8, ocupado=False, reservado=False, vehiculo=None, idPlaza=i))
    else:
        listPlazas.append(
            Plaza(tipo=Tipo.MovildiadReducida, precio=0.10, ocupado=False, reservado=False, vehiculo=None, idPlaza=i))

while seguir:
    main_menu()
    if int(input()) == 1:
        print("Zona Admin")
        print("Bienvenido esclavo, hora de trabajar")
        print("Indique que gestiones desea realizar: ")
        print("0 - Cerrar programa")
        print("1 - Consultar estado del parking")
        print("2 - Consultar Facturación")
        print("3 - Consultar Abonados")
        print("4 - Gestionar abonos")
        print("5 - Comprobar caducidad Abonos")
        decision = int(input())
        if decision == 0:
            seguir = False
        elif decision == 1:
            print("Estado del parking")
            for p in listPlazas:
                print('Id: '+str(p.idPlaza+1)+', '+'Ocupado: '+str(p.ocupado)+', '+'Reservado: '+str(p.reservado)+', ')
        elif decision == 2:
            total = 0
            fecha_inicial = input("Ingresa una fecha inicial en el formato dd/mm/aaaa: ")
            fecha_objeto1 = datetime.strptime(fecha_inicial, "%d/%m/%Y")
            fecha_final = input("Ingresa una fecha inicial en el formato dd/mm/aaaa: ")
            fecha_objeto2 = datetime.strptime(fecha_final, "%d/%m/%Y")

            if fecha_objeto1 < fecha_objeto2:
                for c in listClientes:
                    if (type(c) != Abonado) and (c.ticket.fecha_baja is not None) and \
                            (c.ticket.fecha_alta >= fecha_objeto1) and (c.ticket.fecha_baja <= fecha_objeto2):
                        total += c.ticket.precio
            else:
                for c in listClientes:
                    if (type(c) != Abonado) and (c.ticket.fecha_alta >= fecha_objeto2) \
                            and (c.ticket.fecha_baja <= fecha_objeto1):
                        total += c.ticket.precio
            print("El total recaudado es de " + f"{total:.2f}" + "€")
        elif decision == 3:
            print("Aqui se deberian poder consultar todos los abonados")
            for a in listClientes:
                if isinstance(a, Abonado):
                    print("Nombre: "+str(a.nombre)+', '+"Apellidos: "+str(a.apellidos)+', '+"DNI: "+str(a.dni)
                          +', '"Email: "+str(a.email)+', '+"Tarjeta: "+str(a.tarjeta)+',\n'+
                          "Total: "+str(a.ticket.precio)+'€')
        elif decision == 4:
            print("Indique que gestiones desea realizar: ")
            print("1 - Dar de alta un Abonado")
            print("2 - Modificar un abonado")
            print("3 - Dar de baja un abonado")
            decision = int(input())

            if decision == 1:
                print("Dar de alta a una abonado")
                print("Introduzca los siguientes datos: ")
                menu_ingreso_temporal(listPlazas)
                decision = int(input())

                print("Buscando plazas disponibles para su vehículo")
                x = 0

                while x < len(listPlazas):
                    if listPlazas[x].tipo.value == decision and (not listPlazas[x].ocupado) and (
                            not listPlazas[x].reservado):
                        print("Plaza encontrada")
                        print("Introduzca los siguientes datos conforme se le indiquen")
                        listPlazas[x].vehiculo = Vehiculo(
                            matricula=input("Introduzca su matricula"),
                            # Falta comprobar que la matricula no exista entre las guardadas

                            cliente=Abonado(
                                ticket=Ticket(
                                    fecha_alta=datetime.now(), fecha_baja=None, precio=None,
                                    pin=random.randint(100000, 999999)
                                ),
                                nombre=input("Nombre: "),
                                apellidos=input("Apellidos: "),
                                dni=input("DNI: "),
                                email=input("Email: "),
                                tarjeta=input("Tarjeta de crédito: "),

                            )

                        )

                        print("Elija entre las siguientes opciones la duracion de su bono")
                        print("1 - Mensual - 25€")
                        print("2 - Trimestral - 70€")
                        print("3 - Semestral - 130€")
                        print("4 - Anual - 200€")
                        decision = int(input())
                        if decision == 1:
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=30)
                            listPlazas[x].vehiculo.cliente.ticket.precio = 25
                        elif decision == 2:
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=90)
                            listPlazas[x].vehiculo.cliente.ticket.precio = 70
                        elif decision == 3:
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=180)
                            listPlazas[x].vehiculo.cliente.ticket.precio = 130
                        elif decision == 4:
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=365)
                            listPlazas[x].vehiculo.cliente.ticket.precio = 200
                        else:
                            print("Opcion Incorrecta, mensualidad añadida por defecto")
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=30)
                            listPlazas[x].vehiculo.cliente.ticket.precio = 25

                        listPlazas[x].reservado = True
                        listVehiculos.append(listPlazas[x].vehiculo)
                        listClientes.append(listPlazas[x].vehiculo.cliente)
                        listTicket.append(listPlazas[x].vehiculo.cliente.ticket)

                        ticket_alta_abonado(listPlazas[x])
                        x = len(listPlazas)
                    x += 1
            elif decision == 2:
                print("Modificar un abonado")
                dni = input("Introduzca el DNI del abonado por favor: ")
                for c in listClientes:
                    if (type(c) == Abonado) and (c.dni == dni):
                        print("1 - Renovar abono")
                        print("2 - Modificar datos personales")
                        decision = int(input())
                        if decision == 1:
                            print("Elija entre las siguientes opciones la duracion de su bono")
                            print("1 - Mensual - 25€")
                            print("2 - Trimestral - 70€")
                            print("3 - Semestral - 130€")
                            print("4 - Anual - 200€")
                            decision = int(input())
                            if decision == 1:
                                c.ticket.fecha_baja = c.ticket.fecha_baja + timedelta(days=30)
                                c.ticket.precio += 25
                            elif decision == 2:
                                c.ticket.fecha_baja = c.ticket.fecha_baja + timedelta(days=90)
                                c.ticket.precio += 70
                            elif decision == 3:
                                c.ticket.fecha_baja = c.ticket.fecha_baja + timedelta(days=180)
                                c.ticket.precio += 130
                            elif decision == 4:
                                c.ticket.fecha_baja = c.ticket.fecha_baja + timedelta(days=365)
                                c.ticket.precio += 200
                            else:
                                print("Opcion Incorrecta")
                        elif decision == 2:
                            c.nombre = input("Nombre anterior: "+c.nombre+" Nuevo: ")
                            c.apellidos = input("Apellidos anterior: "+c.apellidos+" Nuevo: ")
                            c.dni = input("DNI anterior: "+c.dni+" Nuevo: ")
                            c.email = input("Email anterior: "+c.email+" Nuevo: ")
                            c.tarjeta = input("Tarjeta de crédito anterior: "+c.tarjeta+" Nuevo: ")
                    else:
                        print("Cliente no encontrado")
            elif decision == 3:
                print("Borrar datos de un abonado")

    else:
        menu_acciones_usuario()
        decision = int(input())
        if decision == 1:
            print("Para generar un nuevo Bono por favor contacte con el personal del Parking.\n"
                  "Muchas Gracias.")
        elif decision == 2:
            menu_ingreso_temporal(listPlazas)
            decision = int(input())

            print("Buscando plazas disponibles para su vehículo")
            x = 0
            while x < len(listPlazas):

                if listPlazas[x].tipo.value == decision and (not listPlazas[x].ocupado) and (not listPlazas[x].reservado):
                    print("Plaza encontrada")
                    listPlazas[x].vehiculo = Vehiculo(
                        matricula=input("Introduzca su matricula"),
                        # Falta comprobar que la matricula no exista entre las guardadas
                        cliente=Cliente(
                            ticket=Ticket(
                                fecha_alta=datetime.now(), fecha_baja=None, precio=None,
                                pin=random.randint(100000, 999999)
                            )
                        )
                    )
                    # Esto irá en uan clase Data y se volcará en el pickle cuando se indique
                    listPlazas[x].ocupado = True
                    listVehiculos.append(listPlazas[x].vehiculo)
                    listClientes.append(listPlazas[x].vehiculo.cliente)
                    listTicket.append(listPlazas[x].vehiculo.cliente.ticket)

                    ticket_entrada_temporal(listPlazas[x])
                    x = len(listPlazas)

                x += 1

        elif decision == 3:
            print("Ingresar con un abono activo")
            x = 0
            matricula = input("Por favor indique la matrícula de su vehículo")
            while x < len(listPlazas):
                if (listPlazas[x].vehiculo.matricula == matricula) and (not listPlazas[x].ocupado) \
                        and type(listPlazas[x].vehiculo.cliente) == Abonado:
                    encontrado = True
                    dni = input("Por favor indique su DNI")
                    if listPlazas[x].vehiculo.cliente.dni == dni:
                        listPlazas[x].ocupado = True
                        print("Tdoo correcto.")

                    else:
                        print("Dni incorrecto máquina.\n"
                              "Introduce el DNI del propietario registrado de la plaza")
                    x = len(listPlazas)
                if not encontrado:
                    print("Error., algún dato ha sido introducido erroneeamente\nIntentelo de nuevo.\n"
                          "Si el error persoste, por favor pongase en contacto con nuestro personal.")
                x += 1
                encontrado = False

        elif decision == 4:
            x = 0
            matricula = input("Introduzca la matrícula de su coche por favor")

            while x < len(listPlazas):

                if listPlazas[x].ocupado and listPlazas[x].vehiculo.matricula == matricula:
                    encontrado = True
                    if type(listPlazas[x].vehiculo.cliente) == Abonado:
                        pin = int(input("Introduzca su pin"))
                        if pin == listPlazas[x].vehiculo.cliente.ticket.pin:
                            ticket_salida_temporal(listPlazas[x])
                            listPlazas[x].ocupado = False
                            print("Vehiculo retirado")

                        else:
                            print("Pin incorrecto máquina.\n"
                                  "¿De quien intentas sacar el coche pillin? ;)")
                        x = len(listPlazas)
                    else:
                        pin = int(input("Introduzca su pin"))
                        if pin == listPlazas[x].vehiculo.cliente.ticket.pin:

                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja = datetime.now()
                            tiempo_total = (
                                    listPlazas[x].vehiculo.cliente.ticket.fecha_baja
                                    - listPlazas[x].vehiculo.cliente.ticket.fecha_alta)
                            listPlazas[x].vehiculo.cliente.ticket.precio = (tiempo_total.total_seconds() / 60) * \
                                                                           listPlazas[x].precio
                            ticket_salida_temporal(listPlazas[x])
                            listVehiculos.remove(listPlazas[x].vehiculo)
                            listPlazas[x].ocupado = False
                            listPlazas[x].vehiculo = None
                            print("Vehiculo retirado")
                            x = len(listPlazas)
                        else:
                            print("Pin incorrecto máquina.\n"
                                  "¿De quien intentas sacar el coche pillin? ;)")
                x += 1
            if not encontrado:
                print("Vehiculo no encontrado")
                encontrado = False

        else:
            print("Volver pa atras")


