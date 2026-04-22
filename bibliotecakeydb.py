import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
PUERTO = int(os.getenv("PUERTO"))
PASSWORD = os.getenv("PASSWORD")

try:
    r = redis.Redis(host=HOST, port=PUERTO, password=PASSWORD, decode_responses=True)
    r.ping()
except:
    print("error de conexion")


def generar_id():
    return r.incr("contador_libros")

def agregar_libro():
    print("\nAgregar libro")
    try:
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        estado = input("Estado: ")

        id_libro = generar_id()

        libro = {
            "id": id_libro,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "estado": estado
        }

        r.set(f"libro:{id_libro}", json.dumps(libro))
        print("Guardado")
    except:
        print("error")

def ver_libros():
    print("\nLista de libros")
    try:
        claves = r.keys("libro:*")
        for c in claves:
            data = json.loads(r.get(c))
            print(data)
    except:
        print("error")

def actualizar_libro():
    print("\nActualizar libro")
    try:
        id_libro = input("ID: ")
        clave = f"libro:{id_libro}"

        if r.exists(clave):
            titulo = input("Nuevo titulo: ")
            autor = input("Nuevo autor: ")
            genero = input("Nuevo genero: ")
            estado = input("Nuevo estado: ")

            libro = {
                "id": id_libro,
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "estado": estado
            }

            r.set(clave, json.dumps(libro))
            print("Actualizado")
        else:
            print("no existe")
    except:
        print("error")

def eliminar_libro():
    print("\nEliminar libro")
    try:
        id_libro = input("ID: ")
        clave = f"libro:{id_libro}"

        if r.exists(clave):
            r.delete(clave)
            print("Eliminado")
        else:
            print("no encontrado")
    except:
        print("error")

def buscar_libro():
    print("\nBuscar libro")
    try:
        dato = input("Buscar: ").lower()
        claves = r.keys("libro:*")

        encontrado = False

        for c in claves:
            libro = json.loads(r.get(c))

            if (dato in libro["titulo"].lower() or
                dato in libro["autor"].lower() or
                dato in libro["genero"].lower()):
                
                print(libro)
                encontrado = True

        if not encontrado:
            print("sin resultados")
    except:
        print("error")


while True:
    print("\n--- biblioteca Bella (KeyDB) ---")
    print("1. Agregar")
    print("2. Ver")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Buscar")
    print("6. Salir")

    op = input("Opcion: ")

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
        print("bye bella")
        break
    else:
        print("no valido")
