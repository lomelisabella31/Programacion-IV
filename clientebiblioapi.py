from flask import Flask, render_template, request, redirect
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_URL = os.getenv("API_URL")


@app.route("/")
def index():
    try:
        res = requests.get(API_URL + "/books")
        libros = res.json()
    except:
        libros = []
    return render_template("index.html", libros=libros)


@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    msg = ""

    if request.method == "POST":
        data = {
            "titulo": request.form["titulo"],
            "autor": request.form["autor"],
            "genero": request.form["genero"]
        }

        try:
            r = requests.post(API_URL + "/books", json=data)
            if r.status_code == 201:
                msg = "Libro agregado"
            else:
                msg = "Error al agregar"
        except:
            msg = "Error de conexion"

    return render_template("agregar.html", msg=msg)


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    msg = ""

    try:
        r = requests.get(API_URL + f"/books/{id}")
        libro = r.json()
    except:
        libro = {}

    if request.method == "POST":
        data = {
            "titulo": request.form["titulo"],
            "autor": request.form["autor"],
            "genero": request.form["genero"]
        }

        try:
            r = requests.put(API_URL + f"/books/{id}", json=data)
            if r.status_code == 200:
                return redirect("/")
            else:
                msg = "error al editar"
        except:
            msg = "error conexion"

    return render_template("editar.html", libro=libro, msg=msg)


@app.route("/eliminar/<int:id>")
def eliminar(id):
    try:
        requests.delete(API_URL + f"/books/{id}")
    except:
        pass
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
