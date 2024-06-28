import FuncionesBiblioteca as fun
import reportes as repo
import os
import time 
repo.crear_json
while True:
    print("**********************************")
    print("*           Mundo libro          *") 
    print("********************************** ")
    print("[1]- Mantenedor de categorias ")
    print("[2]- Reportes")
    print("[3]- Salir")

    opc = int(input("ingrese la opcion que desea :"))
    if opc == 1:
        print("[1]- Agregar categorias ")
        print("[2]- Editar categoria")
        print("[3]- Eliminar categoria")
        print("[4]- Buscar categoria")
        print("[5]- Volver")
        time.sleep(0.5)
        opc = int(input("ingrese la opcion que desea :"))
        if opc == 1:
            nombre = input("ingrese el nombre de la categoria ")
            fun.agregar_categoria(nombreCategoria = nombre)
        elif opc == 2:
            nombre = input("ingrese el nombre de la categoria ")            
            id = int(input("ingrese la id de la categoria "))
            fun.editar_categoria(nombreCategoria=nombre, idInput= id)
        elif opc == 3:
            nombre = input("ingrese el nombre de la categoria ")
            id = int(input("ingrese la id de la categoria "))
            fun.eliminar_categoria(nombreCategoria=nombre, idInput= id)
        elif opc == 4:
            id = int(input("ingrese la id de la categoria "))
            fun.buscar_categoriaJson( idInput= id)
        elif opc == 5:
            continue


    elif opc == 2:
        print("[1]- Crear reporte ")
        print("[2]- Volver")
        time.sleep(0.5)
        opc = int(input("ingrese la opcion que desea :"))
        if opc ==1:
            idInput = int(input("ingrese la id del libro que desea el reporte "))
            repo.crear_reporteJson(id=idInput)
            print("*************************************************")
            print("     libro            cantidad de veces prestados")
            print("*************************************************")
        elif opc == 2:
            continue
    elif opc == 3:
        print("Muchas gracias por visitarnos")
        time.sleep(1.5)
        break
    os.system("cls")
