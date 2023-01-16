import null as null

from Models.Plaza import Plaza

numPlazas = 40
porcentajeTurismo = 70
porcentajeMoto = 15
porcentajeMovilidadReducidad = 15
listPlazas = []
for i in range(numPlazas):
    if i < numPlazas * (porcentajeTurismo / 100):
        listPlazas.append(
            Plaza(tipo='Turismo', precio=0.12, vehiculo=None, vacio=True, disponible=True))
    elif i < (numPlazas * (porcentajeMoto + porcentajeTurismo / 100)):
        listPlazas.append(
            Plaza(tipo='Moto', precio=0.8, vehiculo=None, vacio=True, disponible=True))
    else:
        listPlazas.append(
            Plaza(tipo='MovilidadReducida', precio=0.10, vehiculo=None, vacio=True, disponible=True))
