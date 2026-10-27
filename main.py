from datetime import datetime
from journal import *

# Hola, voy a hacer cositas :)
rutaDiario = "diario.txt"
papaya = datetime.today()

with open(rutaDiario, "a", encoding="utf-8") as newVer: 	# se abre el archivo en modo "append"
    if lockFile(rutaDiario, papaya) == True:					# si el diario está marcado para no escribir nuevas entradas
        blockNotif(papaya)
    else:													# si está permitido escribir nuevas entradas
        newEntry(newVer, papaya)
                
# Como estamos usando open con with, no es necesario hacer .close(), ya que se cierra
# automáticamente una vez que ejecuta todas las líneas de codigo que están dentro de
# su estructura
