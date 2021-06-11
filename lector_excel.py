import openpyxl

class Lector:
    def __init__(self, ruta):
        self.archivo = openpyxl.load_workbook(ruta)
        # selecciona una hoja de trabajo
        self.hoja_activa = self.archivo.active

    def leer_celda(self, celda):
        return self.hoja_activa[celda].value

    def leer_columna(self, columna):
        return [celda.value for celda in self.hoja_activa[columna]]

    def leer_fila(self, fila):
        return [celda.value for celda in self.hoja_activa[fila]]