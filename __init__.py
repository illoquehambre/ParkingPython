import random

from Models.Cliente import Cliente
from Models.Parking import Parking
from Models.Plaza import Plaza
from Models.Ticket import Ticket
from Models.Tipo import Tipo
from Models.Vehiculo import Vehiculo
from datetime import datetime

from Views.Menu import main_menu, menu_acciones_usuario, menu_ingreso_temporal
from Views.Ticket import ticket_entrada_temporal, ticket_salida_temporal

decision = 0
numPlazas = 40
seguir = True
porcentajeTurismo = 70
porcentajeMoto = 15
porcentajeMovilidadReducidad = 15
listPlazas = []
listVehiculos = []
listClientes = []
listTicket = []
for i in range(numPlazas):
    if i < numPlazas * (porcentajeTurismo / 100):
        listPlazas.append(
            Plaza(precio=0.12, ocupado=False, reservado=False, tipo=Tipo.Turismo, vehiculo=None))
    elif i < (numPlazas * (porcentajeMoto + porcentajeTurismo / 100)):
        listPlazas.append(
            Plaza(tipo=Tipo.Moto, precio=0.8, ocupado=False, reservado=False, vehiculo=None))
    else:
        listPlazas.append(
            Plaza(tipo=Tipo.MovildiadReducida, precio=0.10, ocupado=False, reservado=False, vehiculo=None))
p1 = Parking(listPlaza=listPlazas, listTicket=None)



while seguir:
    main_menu()
    if int(input()) == 1:
        print("Zona Admin")  # Por aqui hay que hacer la parte de admin pero la dejamos pa luego por ahora
    else:
        menu_acciones_usuario()
        decision = int(input())
        if decision == 1:
            print("Generar nuevo abono")
        elif decision == 2:
            menu_ingreso_temporal()
            decision = int(input())
            if decision == 1:
                print("Buscando plazas disponibles para su vehículo")
                x = 0
                while x < len(listPlazas):

                    if listPlazas[x].tipo.value == 1 & (not listPlazas[x].ocupado) & (not listPlazas[x].reservado):
                        print("Plaza encontrada")
                        listPlazas[x].vehiculo = Vehiculo(
                            matricula=input("Introduzca su matricula"),
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
            elif decision == 2:
                print("Buscando plazas disponibles para su vehículo")

                for i in listPlazas:
                    if i.tipo.value == 2 & (not i.ocupado) & (not i.reservado):
                        print("Plaza encontrada")
                        Vehiculo(
                            matricula=input("Introduzca su matricula"),
                            cliente=Cliente(
                                ticket=Ticket(
                                    fecha_alta=datetime.now(), fecha_baja=None, precio=None,
                                    pin=random.randint(100000, 999999)
                                )
                            )
                        )
                        # imprime ticket

            elif decision == 3:
                print("Buscando plazas disponibles para su vehículo")
                for i in listPlazas:
                    if i.tipo.value == 3 & (not i.ocupado) & (not i.reservado):
                        print("Plaza encontrada")
                        Vehiculo(
                            matricula=input("Introduzca su matricula"),
                            cliente=Cliente(
                                ticket=Ticket(
                                    fecha_alta=datetime.now(), fecha_baja=None, precio=None,
                                    pin=random.randint(100000, 999999)
                                )
                            )
                        )

                        # imprime ticket
            else:
                print("Número incorrecto, por favor intente de nuevo")
        elif decision == 3:
            print("Ingresar con un abono activo")
        elif decision == 4:
            print("Retirar vehículo")
            # Pregunta si es abonado a normal
            # Introduce Matricula
            # Busca por Matrícula
            # Introduce pin
            # Comprueba pin
            # Procede con el calculo del total si es normal
            # Marca la plaza como disponible
            # Marca la plaza como vacia

            print("Pulse:")
            print("1 - Salida Abonado")
            print("2 - Salida cliente normal")
            print("Cualquier otro número - Volver atrás")
            decision = int(input())
            if decision == 1:
                print("Salida de Abonados")
            elif decision == 2:
                x = 0
                print("Salida cliente normal")
                matricula = input("Introduzca la matrícula de su coche por favor")

                while x < len(listVehiculos):
                    print(listPlazas[x].vehiculo.matricula)
                    if listPlazas[x].vehiculo.matricula == matricula:
                        pin = input("Introduzca su pin")
                        if pin == listPlazas[x].vehiculo.cliente.ticket.pin:
                            ticket_salida_temporal(listPlazas[x])
                            listClientes.remove(listPlazas[x].vehiculo.cliente)
                            listVehiculos.remove(listPlazas[x].vehiculo)
                            listPlazas[x].ocupado = False

                            print("Vehiculo retirado")
                            x = len(listPlazas)

                    x += 1
            else:
                print("Volver pa atras")

        else:
            print("Numero incorrecto, porfavor intente de nuevo")
