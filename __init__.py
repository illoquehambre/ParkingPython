import random

from Models.Cliente import Cliente
from Models.Plaza import Plaza
from Models.Ticket import Ticket
from Models.Tipo import Tipo
from Models.Vehiculo import Vehiculo
from datetime import datetime

decision = 0
numPlazas = 40
seguir = True
porcentajeTurismo = 70
porcentajeMoto = 15
porcentajeMovilidadReducidad = 15
listPlazas = []
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

while seguir:
    print("Bienvenido al Parking Salesianos San Pedro")
    if int(input("Introduzca 1 si usted es administrador o cualquier otro numero si es Usuario")) == 1:
        print("Zona Admin")  # Por aqui hay que hacer la parte de admin pero la dejamos pa luego por ahora
    else:
        print("Bienvenido usuario elija las siguientes opciones marcando el respectivo número por pantalla")
        print("1 - Generar un nuevo bono para estacionar por largos periodos de tiempo")
        print("2 - Estacionar de forma temporal")
        print("3 - Ingresar con un abono activo")
        print("4 - Retirar vehiculo")
        print("Cualquier otro número - Volver a inicio")
        decision = int(input())
        if decision == 1:
            print("Generar nuevo abono")
        elif decision == 2:
            print("Estacionar de forma temporal")
            print("Indique que tipo de vehiculo tiene")
            print("1 - Turismo")
            print("2 - Moto")
            print("3 - Movilidad Reducida")
            decision = int(input())
            if decision == 1:
                print("Buscando plazas disponibles para su vehículo")
                for i in listPlazas:
                    if i.tipo.value == 1 & (not i.ocupado) & (not i.reservado):
                        print("Plaza encontrada")
                        i.vehiculo = Vehiculo(
                            matricula=input("Introduzca su matricula"),
                            cliente=Cliente(
                                ticket=Ticket(
                                    fecha_alta=datetime.now(), fecha_baja=None, precio=None,
                                    pin=random.randint(100000, 999999)
                                )
                            )
                        )

                        print("TICKET")
                        print("Matícula: "+i.vehiculo.matricula)
                        print("Fecha de Entrada: "+ str(i.vehiculo.cliente.ticket.fecha_alta))
                        print("Precio minuto: "+str(i.precio)+"€")
                        print("PIN: "+str(i.vehiculo.cliente.ticket.pin))
                        i = len(listPlazas)
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
            decision = input()
            if decision == 1:
                print("Salida de Abonados")
            elif decision == 2:
                print("Salida cliente normal")
                matricula = input("Introduzca la matrícula de su coche por favor")
                for i in 
            else:
                print("Volver pa atras")


        else:
            print("Numero incorrecto, porfavor intente de nuevo")
