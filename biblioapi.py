from flask import Flask, jsonify, request

app = Flask(__name__)

LIBROS = []
ID = 1

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(LIBROS), 200


@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    for libro in LIBROS:
        if libro["id"] == id:
            return jsonify(libro), 200
    return jsonify({"error": "no encontrado"}), 404


@app.route("/books", methods=["POST"])
def add_book():
    global ID

    data = request.get_json()

    if not data or "titulo" not in data:
        return jsonify({"error": "datos invalidos"}), 400

    nuevo = {
        "id": ID,
        "titulo": data.get("titulo"),
        "autor": data.get("autor"),
        "genero": data.get("genero")
    }

    LIBROS.append(nuevo)
    ID += 1

    return jsonify(nuevo), 201


@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()

    for libro in LIBROS:
        if libro["id"] == id:
            libro["titulo"] = data.get("titulo", libro["titulo"])
            libro["autor"] = data.get("autor", libro["autor"])
            libro["genero"] = data.get("genero", libro["genero"])
            return jsonify(libro), 200

    return jsonify({"error": "no encontrado"}), 404


@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    for libro in LIBROS:
        if libro["id"] == id:
            LIBROS.remove(libro)
            return jsonify({"msg": "eliminado"}), 200

    return jsonify({"error": "no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5001)
