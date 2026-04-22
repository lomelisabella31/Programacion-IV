from flask import Flask, jsonify

app = Flask(__name__)

VACUNAS = [
    {"anio": 2000, "cobertura": 85.2},
    {"anio": 2001, "cobertura": 86.1},
    {"anio": 2002, "cobertura": 87.0},
    {"anio": 2003, "cobertura": 88.5},
    {"anio": 2004, "cobertura": 89.3},
    {"anio": 2005, "cobertura": 90.0},
    {"anio": 2006, "cobertura": 91.2},
    {"anio": 2007, "cobertura": 92.0},
    {"anio": 2008, "cobertura": 93.1},
    {"anio": 2009, "cobertura": 94.0},
    {"anio": 2010, "cobertura": 95.5}
]

@app.route("/vacunas", methods=["GET"])
def get_all():
    return jsonify(VACUNAS), 200

@app.route("/vacunas/<int:anio>", methods=["GET"])
def get_year(anio):

    for v in VACUNAS:
        if v["anio"] == anio:
            return jsonify(v), 200

    return jsonify({"error": "año no encontrado"}), 404

@app.route("/vacunas/provincia/<nombre>", methods=["GET"])
def get_prov(nombre):

    data = []

    for v in VACUNAS:
        data.append({
            "provincia": nombre,
            "anio": v["anio"],
            "cobertura": v["cobertura"] - 2  # variacion falsa
        })

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True, port=5002)
