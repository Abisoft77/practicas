# importar la clase para leer
from lector_excel import Lector
import os
 
# funcion con parametro de entrada
def leer_archivo(nombre_archivo, col):
    # crear un objeto para leer a partir de la clase
    archivo_excel = Lector(nombre_archivo)
    # leer columna
    columna = archivo_excel.leer_columna(col)
 
    # eliminar primer elemento porque es un string
    columna.pop(0)
    
    # sumar los valores de la columna
    valsColumna = [celda for celda in columna]

    return valsColumna
 
carpeta_entrada = "archivos"
# listar todos los archivos de una carpeta
lista_archivos = os.listdir(carpeta_entrada)

noEstudiante = 0
promedios = 0
NOTES = []
# recorriendo la lista de archivos
for nombre_archivo in lista_archivos:
    
    semestre = leer_archivo((f'archivos//{nombre_archivo}'), 'B')
    punteo = leer_archivo((f'archivos//{nombre_archivo}'), 'C')
    
    promedio = sum(punteo) / len(punteo)
    semestreMayor = max(semestre)
    
    for x in punteo:
        NOTES.append(x)

    promedios += promedio
    noEstudiante = noEstudiante + 1
 
    print("=== Estudiante ===", noEstudiante)
    print(nombre_archivo)
    print("Promedio: ", promedio )
    print("Semestre más alto: ", semestreMayor)
    print("Nota más alta: ", max(NOTES))
    print()

print("====================")
print("Promedio total: ", promedios / noEstudiante)
print("Cantidad de estudiantes: ", noEstudiante)
print("Nota más alta: ", max(NOTES))
print("Nota más baja: " , min(NOTES))