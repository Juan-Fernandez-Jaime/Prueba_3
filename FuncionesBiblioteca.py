import json 

def buscar_categoriaJson(idInput:int ):
    with open("biblioteca.json",mode="r") as file:
        lectura = json.load(file)
        for categoria in lectura["Categoria"]:
            if categoria["CategoriaID"] == idInput:
                print(categoria)
           
# buscar_categoriaJso
def agregar_categoria(nombreCategoria:str):
    with open("biblioteca.json",mode="r") as file:
        lectura = json.load(file)
        nueva_categoria = {
            "CategoriaID": len(lectura["Categoria"])+1 ,
            "Nombre":nombreCategoria
        }
        lectura["Categoria"].append(nueva_categoria)
    with open("biblioteca.json",mode="w") as file:
        json.dump(lectura,file, indent=4)

# agregar_categoria("Como estas")

def eliminar_categoria(idInput:int):
    with open("biblioteca.json",mode="r") as file:
        lectura = json.load(file)
        cont = None
        for categoria in lectura["Categoria"]:
            if idInput == categoria["CategoriaID"]:
                cont = categoria
                break
        lectura["Categoria"].remove(cont)

    with open("biblioteca.json",mode="w") as file:
        json.dump(lectura,file, indent=4)
# eliminar_categoria(13)

def editar_categoria(nombreCategoria:str,idInput:int):
    with open("biblioteca.json",mode="r") as file:
        lectura = json.load(file)
        for categoria in lectura["Categoria"]:
            if idInput == categoria["CategoriaID"]:
                categoria["Nombre"]:nombreCategoria


    with open("biblioteca.json",mode="w") as file:
        json.dump(lectura,file,indent=4)
# editar_categoria("HolA",11)