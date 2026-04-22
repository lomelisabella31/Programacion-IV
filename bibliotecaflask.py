from flask import Flask, render_template, request, redirect
import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("HOST"),
    port=int(os.getenv("PUERTO")),
    password=os.getenv("PASSWORD"),
    decode_responses=True
)

def generar_id():
    return r.incr("contador_libros")

@app.route("/")
def inicio():
    claves = r.keys("libro:*")
    libros = []

    for c in claves:
        libros.append(json.loads(r.get(c)))

    return render_template("index.html", libros=libros)

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        genero = request.form["genero"]
        estado = request.form["estado"]

        id_libro = generar_id()

        libro = {
            "id": id_libro,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "estado": estado
        }

        r.set(f"libro:{id_libro}", json.dumps(libro))
        return redirect("/")

    return render_template("agregar.html")

@app.route("/eliminar/<id>")
def eliminar(id):
    r.delete(f"libro:{id}")
    return redirect("/")

@app.route("/editar/<id>", methods=["GET", "POST"])
def editar(id):
    clave = f"libro:{id}"
    libro = json.loads(r.get(clave))

    if request.method == "POST":
        libro["titulo"] = request.form["titulo"]
        libro["autor"] = request.form["autor"]
        libro["genero"] = request.form["genero"]
        libro["estado"] = request.form["estado"]

        r.set(clave, json.dumps(libro))
        return redirect("/")

    return render_template("editar.html", libro=libro)

@app.route("/buscar", methods=["POST"])
def buscar():
    dato = request.form["dato"].lower()
    claves = r.keys("libro:*")
    resultados = []

    for c in claves:
        libro = json.loads(r.get(c))

        if (dato in libro["titulo"].lower() or
            dato in libro["autor"].lower() or
            dato in libro["genero"].lower()):
            resultados.append(libro)

    return render_template("index.html", libros=resultados)

if __name__ == "__main__":
    app.run(debug=True)
