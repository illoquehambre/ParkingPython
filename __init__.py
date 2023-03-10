import random
from typing import List
from Models.Abonado import Abonado
from Models.Cliente import Cliente
from Models.Plaza import Plaza
from Models.Ticket import Ticket
from Models.Tipo import Tipo
from Models.Vehiculo import Vehiculo
from datetime import datetime, timedelta
import pickle
from Services.Finds import find_matricula, find_caducados_por_mes, find_caducados_proximos
from Views.Menu import main_menu, menu_acciones_usuario, menu_ingreso_temporal, menu_acciones_admin, \
    gestiones_abonado, planes_abonos
from Views.Resultados import mostrar_abonados
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

with open('listTicket.pckl', 'rb') as t:
    listTicket = pickle.load(t)
    t.close()

with open('listClientes.pckl', 'rb') as c:
    listClientes = pickle.load(c)
    c.close()

with open('listVehiculos.pckl', 'rb') as v:
    listVehiculos = pickle.load(v)
    v.close()

with open('listPlazas.pckl', 'rb') as p:
    listPlazas = pickle.load(p)
    p.close()

while seguir:

    main_menu()
    if int(input()) == 1:
        menu_acciones_admin()
        decision = int(input())
        if decision == 0:
            seguir = False
        elif decision == 1:
            print("Estado del parking")
            for p in listPlazas:
                print('Id: ' + str(p.idPlaza + 1) + ', ' + 'Ocupado: ' + str(p.ocupado) + ', ' + 'Reservado: ' + str(
                    p.reservado) + ', ')
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
            print("El total recaudado es de " + f"{total:.2f}" + "???")
        elif decision == 3:
            print("Aqui se deberian poder consultar todos los abonados")
            mostrar_abonados(listClientes)
        elif decision == 4:
            gestiones_abonado()
            decision = int(input())

            if decision == 1:
                print("Dar de alta a una abonado")
                print("Introduzca los siguientes datos: ")
                menu_ingreso_temporal(listPlazas)
                decision = int(input())

                print("Buscando plazas disponibles para su veh??culo")
                x = 0

                while x < len(listPlazas):
                    if listPlazas[x].tipo.value == decision and (not listPlazas[x].ocupado) and (
                            not listPlazas[x].reservado):
                        encontrado = True
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
                                tarjeta=input("Tarjeta de cr??dito: "),

                            )

                        )
                        planes_abonos()
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
                            print("Opcion Incorrecta, mensualidad a??adida por defecto")
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=30)
                            listPlazas[x].vehiculo.cliente.ticket.precio = 25

                        listPlazas[x].reservado = True
                        listVehiculos.append(listPlazas[x].vehiculo)
                        listClientes.append(listPlazas[x].vehiculo.cliente)
                        listTicket.append(listPlazas[x].vehiculo.cliente.ticket)

                        ticket_alta_abonado(listPlazas[x])

                    x += 1

            elif decision == 2:
                print("Modificar un abonado")
                dni = input("Introduzca el DNI del abonado por favor: ")
                c = 0
                print("1 - Renovar abono")
                print("2 - Modificar datos personales")
                decision = int(input())

                while c < len(listClientes):
                    encontrado = False
                    if (type(listClientes[c]) == Abonado) and (listClientes[c].dni == dni):
                        encontrado = True
                        if decision == 1:
                            planes_abonos()
                            decision = int(input())
                            if decision == 1:
                                listClientes[c].ticket.fecha_baja = listClientes[c].ticket.fecha_baja + timedelta(
                                    days=30)
                                listClientes[c].ticket.precio += 25
                            elif decision == 2:
                                listClientes[c].ticket.fecha_baja = listClientes[c].ticket.fecha_baja + timedelta(
                                    days=90)
                                listClientes[c].ticket.precio += 70
                            elif decision == 3:
                                listClientes[c].ticket.fecha_baja = listClientes[c].ticket.fecha_baja + timedelta(
                                    days=180)
                                listClientes[c].ticket.precio += 130
                            elif decision == 4:
                                listClientes[c].ticket.fecha_baja = listClientes[c].ticket.fecha_baja + timedelta(
                                    days=365)
                                listClientes[c].ticket.precio += 200
                            else:
                                print("Opcion Incorrecta")
                        elif decision == 2:
                            listClientes[c].nombre = input("Nombre anterior: " + listClientes[c].nombre + " Nuevo: ")
                            listClientes[c].apellidos = input(
                                "Apellidos anterior: " + listClientes[c].apellidos + " Nuevo: ")
                            listClientes[c].dni = input("DNI anterior: " + listClientes[c].dni + " Nuevo: ")
                            listClientes[c].email = input("Email anterior: " + listClientes[c].email + " Nuevo: ")
                            listClientes[c].tarjeta = input(
                                "Tarjeta de cr??dito anterior: " + listClientes[c].tarjeta + " Nuevo: ")
                        c = len(listClientes)
                    c += 1

                if not encontrado:
                    print("Cliente no encontrado")

            elif decision == 3:  # Esto no funciona
                print("Borrar datos de un abonado")
                print("Queda avisadod e antemano que esto peta")
                dni = input("Introduce el dni del cliente")
                for p in listPlazas:
                    if p.reservado and p.vehiculo.cliente.dni == dni:
                        p.vehiculo = None
                        listVehiculos.remove(p.vehiculo)
                        p.reservado = False
                        p.ocupado = False

        elif decision == 5:
            print("Comprobar caducidad de Abonos")
            mostrar_abonados(find_caducados_proximos(listPlazas))
            mes = input("Introduzca el n??mero del mes que desee comprobar")
            mostrar_abonados(find_caducados_por_mes(mes, listPlazas))

    else:
        menu_acciones_usuario()
        decision = int(input())
        if decision == 1:
            print("Para generar un nuevo Bono por favor contacte con el personal del Parking.\n"
                  "Muchas Gracias.")
        elif decision == 2:
            menu_ingreso_temporal(listPlazas)
            decision = int(input())

            print("Buscando plazas disponibles para su veh??culo")
            x = 0
            while x < len(listPlazas):

                if listPlazas[x].tipo.value == decision and (not listPlazas[x].ocupado) and (
                        not listPlazas[x].reservado):
                    print("Plaza encontrada")
                    matricula = input("Introduzca su matricula")

                    if find_matricula(listPlazas, matricula):
                        listPlazas[x].vehiculo = Vehiculo(
                            matricula=matricula,
                            # Falta comprobar que la matricula no exista entre las guardadas
                            cliente=Cliente(
                                ticket=Ticket(
                                    fecha_alta=datetime.now(), fecha_baja=None, precio=None,
                                    pin=random.randint(100000, 999999)
                                )
                            )
                        )
                        # Esto ir?? en uan clase Data y se volcar?? en el pickle cuando se indique
                        listPlazas[x].ocupado = True
                        listVehiculos.append(listPlazas[x].vehiculo)
                        listClientes.append(listPlazas[x].vehiculo.cliente)
                        listTicket.append(listPlazas[x].vehiculo.cliente.ticket)

                        ticket_entrada_temporal(listPlazas[x])
                        x = len(listPlazas)
                    else:
                        print("Esta matricula ya se encuentar registrada")
                x += 1

        elif decision == 3:
            print("Ingresar con un abono activo")
            x = 0
            matricula = input("Por favor indique la matr??cula de su veh??culo")
            while x < len(listPlazas):
                if (listPlazas[x].reservado and listPlazas[x].vehiculo.matricula == matricula) \
                        and (not listPlazas[x].ocupado):
                    encontrado = True
                    dni = input("Por favor indique su DNI")
                    if listPlazas[x].vehiculo.cliente.dni == dni:
                        listPlazas[x].ocupado = True
                        print("Todo correcto.")

                    else:
                        print("Dni incorrecto m??quina.\n"
                              "Introduce el DNI del propietario registrado de la plaza")
                    x = len(listPlazas)
                    encontrado = True
                x += 1

            if not encontrado:
                print("Error, alg??n dato ha sido introducido erroneeamente\nIntentelo de nuevo.\n"
                      "Si el error persoste, por favor pongase en contacto con nuestro personal.")


        elif decision == 4:
            x = 0
            matricula = input("Introduzca la matr??cula de su coche por favor")

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
                            print("Pin incorrecto m??quina.\n"
                                  "??De quien intentas sacar el coche pillin? ;)")
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
                            vehiculo = listPlazas[x].vehiculo
                            listPlazas[x].ocupado = False
                            listPlazas[x].vehiculo = None
                            print("Vehiculo retirado")
                            x = len(listPlazas)
                        else:
                            print("Pin incorrecto m??quina.\n"
                                  "??De quien intentas sacar el coche pillin? ;)")
                x += 1
            if not encontrado:
                print("Vehiculo no encontrado")
                encontrado = False

        else:
            print("Volver pa atras")

    with open('listTicket.pckl', 'wb') as t:
        pickle.dump(listTicket, t)
        t.close()

    with open('listClientes.pckl', 'wb') as c:
        pickle.dump(listClientes, c)
        c.close()

    with open('listVehiculos.pckl', 'wb') as v:
        pickle.dump(listVehiculos, v)
        v.close()

    with open('listPlazas.pckl', 'wb') as p:
        pickle.dump(listPlazas, p)
        p.close()
