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
from Views.Ticket import ticket_entrada_temporal, ticket_salida_temporal

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
for i in range(numPlazas):
    if i < numPlazas * (porcentajeTurismo / 100):
        listPlazas.append(
            Plaza(precio=0.12, ocupado=False, reservado=False, tipo=Tipo.Turismo, vehiculo=None, idPlaza=i))
    elif i < (numPlazas * (porcentajeMoto + porcentajeTurismo / 100)):
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
        elif decision == 2:
            total = 0
            fecha_inicial = input("Ingresa una fecha inicial en el formato dd/mm/aaaa: ")
            fecha_objeto1 = datetime.strptime(fecha_inicial, "%d/%m/%Y")
            fecha_final = input("Ingresa una fecha inicial en el formato dd/mm/aaaa: ")
            fecha_objeto2 = datetime.strptime(fecha_final, "%d/%m/%Y")

            if fecha_objeto1 < fecha_objeto2:
                for c in listClientes:
                    if (type(c) != Abonado) & (c.ticket.fecha_alta >= fecha_objeto1) \
                            & (c.ticket.fecha_baja <= fecha_objeto2):
                        total += c.ticket.precio  # AQUI PETA
                        # TypeError: unsupported operand type(s) for +=: 'int' and 'NoneType'
            else:
                for c in listClientes:
                    if (type(c) != Abonado) & (c.ticket.fecha_alta >= fecha_objeto2) \
                            & (c.ticket.fecha_baja <= fecha_objeto1):
                        total += c.ticket.precio
            print("El total recaudado es de " + str(total))
        elif decision == 3:
            print("Aqui se deberian poder consultar todos los abonados")
        elif decision == 4:
            print("Indique que gestiones desea realizar: ")
            print("1 - Dar de alta un Abonado")
            print("2 - Modificar un abonado")
            print("3 - Dar de baja un abonado")
            decision = int(input())

            if decision == 1:
                print("Dar de alta a una abonado")
                print("Introduzca los siguientes datos: ")
                menu_ingreso_temporal()
                decision = int(input())

                print("Buscando plazas disponibles para su vehículo")
                x = 0
                while x < len(listPlazas):
                    if listPlazas[x].tipo.value == decision & (not listPlazas[x].ocupado) & (
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
                        elif decision == 2:
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=90)
                        elif decision == 3:
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=180)
                        elif decision == 4:
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=365)
                        else:
                            print("Opcion Incorrecta, mensualidad añadida por defecto")
                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja \
                                = listPlazas[x].vehiculo.cliente.ticket.fecha_alta + timedelta(days=30)

                        listVehiculos.append(listPlazas[x].vehiculo)
                        listClientes.append(listPlazas[x].vehiculo.cliente)
                        listTicket.append(listPlazas[x].vehiculo.cliente.ticket)

                        ticket_entrada_temporal(listPlazas[x])
                        x = len(listPlazas)
                    x += 1
            elif decision == 2:
                print("Modificar un abonado")
                dni = input("Introduzca el DNI del abonado por favor: ")
                for c in listClientes:
                    if (type(c) == Abonado) & (c.dni == dni):
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
                            elif decision == 2:
                                c.ticket.fecha_baja = c.ticket.fecha_baja + timedelta(days=90)
                            elif decision == 3:
                                c.ticket.fecha_baja = c.ticket.fecha_baja + timedelta(days=180)
                            elif decision == 4:
                                c.ticket.fecha_baja = c.ticket.fecha_baja + timedelta(days=365)
                            else:
                                print("Opcion Incorrecta")
                        elif decision == 2:
                            c.nombre = input("Nombre: ")
                            c.apellidos = input("Apellidos: ")
                            c.dni = input("DNI: ")
                            c.email = input("Email: ")
                            c.tarjeta = input("Tarjeta de crédito: ")
            elif decision == 3:
                print("Borrar datos de un abonado")
                

    else:
        menu_acciones_usuario()
        decision = int(input())
        if decision == 1:
            print("Para generar un nuevo Bono por favor contacte con el personal del Parking.\n"
                  "Muchas Gracias.")
        elif decision == 2:
            menu_ingreso_temporal()
            decision = int(input())

            print("Buscando plazas disponibles para su vehículo")
            x = 0
            while x < len(listPlazas):

                if listPlazas[x].tipo.value == decision & (not listPlazas[x].ocupado) & (not listPlazas[x].reservado):
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
                    listVehiculos.append(listPlazas[x].vehiculo)
                    listClientes.append(listPlazas[x].vehiculo.cliente)
                    listTicket.append(listPlazas[x].vehiculo.cliente.ticket)

                    ticket_entrada_temporal(listPlazas[x])
                    x = len(listPlazas)
                x += 1

            else:
                print("Número incorrecto, por favor intente de nuevo")
        elif decision == 3:
            print("Ingresar con un abono activo")
            x = 0
            matricula = input("Por favor indique la matrícula de su vehículo")
            while x < len(listVehiculos):
                print(listPlazas[x].vehiculo.matricula)
                if (listPlazas[x].vehiculo.matricula == matricula) & type(listPlazas[x].vehiculo.cliente) == Abonado:
                    dni = input("Por favor indique su DNI")
                    if listPlazas[x].vehiculo.cliente.dni == dni:
                        listPlazas[x].ocupado = False
                        print("Vehiculo retirado")
                        x = len(listPlazas)
                    else:
                        print("Dni incorrecto máquina.\n"
                              "Introduce el DNI del propietario del vehiculo")
                else:
                    print("Matrícula incorrecta.\n"
                          "No existe nigun bono activo para este vehiculo")
                x += 1

        elif decision == 4:
            retirar_vehiculo()
            decision = int(input())
            if decision == 1:
                print("Salida de Abonados")
                x = 0
                matricula = input("Introduzca la matrícula de su coche por favor")

                while x < len(listVehiculos):
                    print(listPlazas[x].vehiculo.matricula)
                    if listPlazas[x].vehiculo.matricula == matricula:
                        pin = input("Introduzca su pin")
                        if pin == listPlazas[x].vehiculo.cliente.ticket.pin:

                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja = datetime.now()
                            ticket_salida_temporal(listPlazas[x])
                            listClientes.remove(listPlazas[x].vehiculo.cliente)
                            listVehiculos.remove(listPlazas[x].vehiculo)
                            listPlazas[x].ocupado = False
                            print("Vehiculo retirado")
                            x = len(listPlazas)
                        else:
                            print("Pin incorrecto máquina.\n"
                                  "¿De quien intentas sacar el coche pillin? ;)")
                    else:
                        print("Matrícula incorrecta.\n"
                              "¿Ni tu propia matrícula te sabes pringao?")
                    x += 1
            elif decision == 2:
                x = 0
                print("Salida cliente normal")
                matricula = input("Introduzca la matrícula de su coche por favor")

                while x < len(listVehiculos):
                    if listPlazas[x].vehiculo.matricula == matricula:
                        pin = int(input("Introduzca su pin"))
                        if pin == listPlazas[x].vehiculo.cliente.ticket.pin:

                            listPlazas[x].vehiculo.cliente.ticket.fecha_baja = datetime.now()
                            ticket_salida_temporal(listPlazas[x])
                            listPlazas[x].ocupado = False
                            listPlazas[x].vehiculo = None
                            print("Vehiculo retirado")
                            x = len(listPlazas)
                        else:
                            print("Pin incorrecto máquina.\n"
                                  "¿De quien intentas sacar el coche pillin? ;)")
                    else:
                        print("Matrícula incorrecta.\n"
                              "¿Ni tu propia matrícula te sabes pringao?")
                    x += 1
            else:
                print("Volver pa atras")

        else:
            print("Numero incorrecto, porfavor intente de nuevo")
