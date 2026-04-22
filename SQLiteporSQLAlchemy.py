from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

usuario = "lomelisa31"
password = "bellitauwu"
host = "localhost"
db = "biblioteca_isabella"

engine = create_engine(f"mysql+pymysql://{usuario}:{password}@{host}/{db}")

Base = declarative_base()

class Libro(Base):
    __tablename__ = "libros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    autor = Column(String(100))
    genero = Column(String(50))
    estado = Column(String(20))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



def agregar_libro():
    print("\nAgregar libro")
    try:
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        estado = input("Estado (leido/no leido): ")

        nuevo = Libro(titulo=titulo, autor=autor, genero=genero, estado=estado)
        session.add(nuevo)
        session.commit()
        print("Libro guardado")
    except Exception as e:
        print("Error al guardar:", e)


def ver_libros():
    print("\nLista de libros")
    libros = session.query(Libro).all()

    for l in libros:
        print(l.id, l.titulo, l.autor, l.genero, l.estado)


def actualizar_libro():
    print("\nActualizar libro")
    try:
        id_libro = input("ID: ")
        libro = session.query(Libro).get(id_libro)

        if libro:
            libro.titulo = input("Nuevo título: ")
            libro.autor = input("Nuevo autor: ")
            libro.genero = input("Nuevo género: ")
            libro.estado = input("Nuevo estado: ")

            session.commit()
            print("Actualizado")
        else:
            print("No existe ese libro")
    except Exception as e:
        print("Error:", e)


def eliminar_libro():
    print("\nEliminar libro")
    try:
        id_libro = input("ID: ")
        libro = session.query(Libro).get(id_libro)

        if libro:
            session.delete(libro)
            session.commit()
            print("Eliminado")
        else:
            print("No encontrado")
    except Exception as e:
        print("Error:", e)


def buscar_libro():
    print("\nBuscar libro")
    dato = input("Buscar: ")

    resultados = session.query(Libro).filter(
        (Libro.titulo.like(f"%{dato}%")) |
        (Libro.autor.like(f"%{dato}%")) |
        (Libro.genero.like(f"%{dato}%"))
    ).all()

    for l in resultados:
        print(l.id, l.titulo, l.autor, l.genero, l.estado)



while True:
    print("\n--- biblioteca de Isa ---")
    print("1. Agregar")
    print("2. Ver")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Buscar")
    print("6. Salir")

    op = input("Opción: ")

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
        print("bye Isa")
        break
    else:
        print("no valido")
