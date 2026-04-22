import json
import os

ARCHIVO = "articulos.json"

def cargar():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)

def guardar(data):
    with open(ARCHIVO, "w") as f:
        json.dump(data, f, indent=4)

def registrar():
    print("\nREGISTRAR ARTICULO")

    nombre = input("nombre: ")
    categoria = input("categoria: ")
    cantidad = input("cantidad: ")
    precio = input("precio unitario: ")
    desc = input("descripcion: ")

    if nombre == "" or categoria == "":
        print("datos invalidos")
        return

    data = cargar()

    nuevo = {
        "id": len(data) + 1,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
        "descripcion": desc
    }

    data.append(nuevo)
    guardar(data)

    print("articulo guardado")

def listar():
    print("\nLISTA DE ARTICULOS")

    data = cargar()

    if len(data) == 0:
        print("no hay datos")
        return

    for a in data:
        print(a["id"], a["nombre"], "-", a["categoria"], "-", a["precio"])

def buscar():
    print("\nBUSCAR ARTICULOS")

    op = input("buscar por (nombre/categoria): ")

    data = cargar()

    encontrado = False

    for a in data:
        if op.lower() in a["nombre"].lower() or op.lower() in a["categoria"].lower():
            print(a)
            encontrado = True

    if not encontrado:
        print("no encontrado")

def editar():
    print("\nEDITAR ARTICULO")

    id = input("id del articulo: ")

    data = cargar()

    for a in data:
        if str(a["id"]) == id:
            a["nombre"] = input("nuevo nombre: ") or a["nombre"]
            a["categoria"] = input("nueva categoria: ") or a["categoria"]
            a["cantidad"] = input("nueva cantidad: ") or a["cantidad"]
            a["precio"] = input("nuevo precio: ") or a["precio"]

            guardar(data)
            print("actualizado")
            return

    print("no encontrado")

def eliminar():
    print("\nELIMINAR ARTICULO")

    id = input("id: ")

    data = cargar()

    nueva = []

    for a in data:
        if str(a["id"]) != id:
            nueva.append(a)

    guardar(nueva)
    print("eliminado si existia")

def menu():
    while True:
        print("\n===== PRESUPUESTO ISA =====")
        print("1. registrar")
        print("2. listar")
        print("3. buscar")
        print("4. editar")
        print("5. eliminar")
        print("0. salir")

        op = input("elige: ")

        if op == "1":
            registrar()
        elif op == "2":
            listar()
        elif op == "3":
            buscar()
        elif op == "4":
            editar()
        elif op == "5":
            eliminar()
        elif op == "0":
            print("adios")
            break
        else:
            print("opcion invalida")


if __name__ == "__main__":
    menu()
