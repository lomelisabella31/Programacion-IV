import sqlite3

conexion = sqlite3.connect("biblioteca_isa.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    genero TEXT,
    estado TEXT
)
""")

conexion.commit()


def agregar_libro():
    print("\nAgregar libro")
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado = input("Estado (leido/no leido): ")

    cursor.execute("INSERT INTO libros (titulo, autor, genero, estado) VALUES (?, ?, ?, ?)",
                   (titulo, autor, genero, estado))
    conexion.commit()
    print("Libro agregado")


def ver_libros():
    print("\nLista de libros")
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()

    for libro in libros:
        print(libro)


def actualizar_libro():
    print("\nActualizar libro")
    id_libro = input("ID del libro: ")

    nuevo_titulo = input("Nuevo título: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_genero = input("Nuevo género: ")
    nuevo_estado = input("Nuevo estado: ")

    cursor.execute("""
    UPDATE libros
    SET titulo = ?, autor = ?, genero = ?, estado = ?
    WHERE id = ?
    """, (nuevo_titulo, nuevo_autor, nuevo_genero, nuevo_estado, id_libro))

    conexion.commit()
    print("Libro actualizado")


def eliminar_libro():
    print("\nEliminar libro")
    id_libro = input("ID del libro: ")

    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conexion.commit()
    print("Libro eliminado")


def buscar_libro():
    print("\nBuscar libro")
    dato = input("Buscar por título, autor o género: ")

    cursor.execute("""
    SELECT * FROM libros
    WHERE titulo LIKE ? OR autor LIKE ? OR genero LIKE ?
    """, (f"%{dato}%", f"%{dato}%", f"%{dato}%"))

    resultados = cursor.fetchall()

    for libro in resultados:
        print(libro)

cursor.execute("INSERT INTO libros (titulo, autor, genero, estado) VALUES ('Orgullo y prejuicio', 'Austen', 'Romance', 'leido')")
cursor.execute("INSERT INTO libros (titulo, autor, genero, estado) VALUES ('La metamorfosis', 'Kafka', 'Ficcion', 'no leido')")
cursor.execute("INSERT INTO libros (titulo, autor, genero, estado) VALUES ('El niño con el pijama de rayas', 'Boyne', 'Drama', 'leido')")
conexion.commit()


while True:
    print("\n--- Biblioteca de Isa ---")
    print("1. Agregar libro")
    print("2. Ver libros")
    print("3. Actualizar libro")
    print("4. Eliminar libro")
    print("5. Buscar libro")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        ver_libros()
    elif opcion == "3":
        actualizar_libro()
    elif opcion == "4":
        eliminar_libro()
    elif opcion == "5":
        buscar_libro()
    elif opcion == "6":
        print("Chao Isa")
        break
    else:
        print("Opción no válida")

conexion.close()
