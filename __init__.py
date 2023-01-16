from Models.Cliente import Cliente
from Models.Plaza import Plaza
from Models.Ticket import Ticket
from Models.Tipo import Tipo
from Models.Vehiculo import Vehiculo
from datetime import datetime

decision = 0
numPlazas = 40
seguir =True
porcentajeTurismo = 70
porcentajeMoto = 15
porcentajeMovilidadReducidad = 15
listPlazas = []
for i in range(numPlazas):
    if i < numPlazas * (porcentajeTurismo / 100):
        listPlazas.append(
            Plaza(precio=0.12, vacio=True, disponible=True, tipo=Tipo.Turismo))
    elif i < (numPlazas * (porcentajeMoto + porcentajeTurismo / 100)):
        listPlazas.append(
            Plaza(tipo=Tipo.Moto, precio=0.8, vacio=True, disponible=True))
    else:
        listPlazas.append(
            Plaza(tipo=Tipo.MovildiadReducida, precio=0.10, vacio=True, disponible=True))

while seguir:
    print("Bienvenido al Parking Salesianos San Pedro")
    if input("Introduzca 1 si usted es administrador o cualquier otro numero si es Usuario") == 1:
        print("Zona Admin")  # Por aqui hay que hacer la parte de admin pero la dejamos pa luego por ahora
    else:
        print("Bienvenido usuario elija las siguientes opciones marcando el respectivo número por pantalla")
        print("1 - Generar un nuevo bono para estacionar por largos periodos de tiempo")
        print("2 - Estacionar de forma temporal")
        print("3 - Ingresar con un abono activo")
        print("4 - Retirar vehiculo")
        print("Cualquier otro número - Volver a inicio")
        decision = input()
        if decision == 1:
            print("Generar nuevo abono")
        elif decision == 2:
            print("Estacionar de forma temporal")
            print("Indique que tipo de vehiculo tiene")
            print("1 - Turismo")
            print("2 - Moto")
            print("3 - Movilidad Reducida")
            decision = input()
            if decision == 1:
                print("Buscando plazas disponibles para su vehículo")
            elif decision == 2:
                print("Buscando plazas disponibles para su vehículo")
                for i in listPlazas:
                    if i.tipo.__eq__(Tipo.Turismo) & i.disponible:
                        print("Plaza encontrada")
                        Cliente(
                            vehiculo=Vehiculo(
                                matricula=input("Introduzca su matricula"), tipo=Tipo.Turismo, plaza=i),
                            ticket=Ticket(
                                fecha_alta=datetime.now(), fecha_baja=None, precio=None,
                                pin=input("Aqui se deberia autogenerar un numero")
                            )
                        )
                        #imprime ticket

            elif decision == 3:
                print("Buscando plazas disponibles para su vehículo")

            else:
                print("Número incorrecto, por favor intente de nuevo")
        elif decision == 3:
            print("Ingresar con un abono activo")
        elif decision == 4:
            print("Retirar vehículo")
            #Introduce pin
            #Busca por pin
            #Comprueba si es abonado o normal
                #Procede con el calculo del total si es normal
                #Marca la plaza como disponible
            #Marca la plaza como vacia
        else:
            print("Numero incorrecto, porfavor intente de nuevo")


