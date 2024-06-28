import json 
import os
import time 
def crear_json():
    with open("Reportes_biblioteca_mundo_libro.json",mode="w") as file:
        lectura = json.dump(lectura,file)
        print(lectura)
# crear_json()

def crear_reporteJson(id:int):
    with open("biblioteca.json",mode="r") as file:
        lectura1 = json.load(file)
        for Libro in lectura["Libro"]:
            if Libro["LibroID"] == id:
                with open("Reportes_biblioteca_mundo_libro.json",mode="r") as file:
                    lectura = json.load(file)
                    nuevo_reporte = {
                        "Titulo": Libro["Libro"],
                        "Prestamos":Libro["Prestamo"],
                        
                }
                    lectura.append(nuevo_reporte)

    with open("Reportes_biblioteca_mundo_libro.json",mode="a") as file:
        json.load(lectura,file,indend= 4)
        

crear_reporteJson(1)
