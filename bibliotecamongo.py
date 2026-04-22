from pymongo import MongoClient

try:
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["bibliotecaisa"]
    coleccion = db["libros"]
except Exception as e:
    print("error de conexion:", e)


def agregar_libro():
    print("\nagregar libro")
    try:
        titulo = input("titulo: ")
        autor = input("autor: ")
        genero = input("genero: ")
        estado = input("estado (leido/no leido): ")

        libro = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "estado": estado
        }

        coleccion.insert_one(libro)
        print("guardado")
    except:
        print("error al guardar")


def ver_libros():
    print("\nlista de libros")
    try:
        for l in coleccion.find():
            print(l)
    except:
        print("error")


def actualizar_libro():
    print("\nactualizar libro")
    try:
        titulo = input("titulo del libro a cambiar: ")

        nuevo_titulo = input("nuevo titulo: ")
        nuevo_autor = input("nuevo autor: ")
        nuevo_genero = input("nuevo genero: ")
        nuevo_estado = input("nuevo estado: ")

        resultado = coleccion.update_one(
            {"titulo": titulo},
            {"$set": {
                "titulo": nuevo_titulo,
                "autor": nuevo_autor,
                "genero": nuevo_genero,
                "estado": nuevo_estado
            }}
        )

        if resultado.modified_count > 0:
            print("actualizado")
        else:
            print("no encontrado")
    except:
        print("error")


def eliminar_libro():
    print("\neliminar libro")
    try:
        titulo = input("titulo: ")
        resultado = coleccion.delete_one({"titulo": titulo})

        if resultado.deleted_count > 0:
            print("eliminado")
        else:
            print("no existe")
    except:
        print("error")


def buscar_libro():
    print("\nbuscar libro")
    try:
        dato = input("buscar: ")

        resultados = coleccion.find({
            "$or": [
                {"titulo": {"$regex": dato, "$options": "i"}},
                {"autor": {"$regex": dato, "$options": "i"}},
                {"genero": {"$regex": dato, "$options": "i"}}
            ]
        })

        encontrado = False
        for l in resultados:
            print(l)
            encontrado = True

        if not encontrado:
            print("sin resultados")
    except:
        print("error")

while True:
    print("\n--- biblioteca isa (mongo) ---")
    print("1. agregar")
    print("2. ver")
    print("3. actualizar")
    print("4. eliminar")
    print("5. buscar")
    print("6. salir")

    op = input("opcion: ")

    if op == "1":
        agregar_libro()
    elif op == "2":
        ver_libros()
    elif op == "3":
        actualizar_libro()
    elif op == "4":
        eliminar_libro()
    elif op == "5":
        buscar_libro()
    elif op == "6":
        print("bye isa")
        break
    else:
        print("no valido")
