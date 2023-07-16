import datetime
import os
import shutil

# Importamos las librerias necesarias

dt = datetime.datetime.now()

name = "Copia de seguridad creada el dia {} del año {} y la hora {}".format(dt.day,dt.year,dt.hour)

# Creamos la direccion donde queremos que se guarden las copias de seguridad

shutil.make_archive(name, "zip","ejemploSave")

# Colocamos el nombre, formato y lugar donde se guardara

start = [] # Comienza como un arhivo vacio pero mas adelante en * se completa.

total = os.listdir() # Lo listamos

for a in total:
    if a .startswith("Copia de seguridad creada el dia ") == True:
        start.append(a) # * Aqui se completa el archivo vacio

finishRoute = "User/data/desktop/copy-security" # Aqui se mueve la copia en formato zip.

for i in start:
    shutil.move(i,finishRoute)