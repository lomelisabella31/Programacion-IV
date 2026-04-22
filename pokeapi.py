import requests
import time

BASE = "https://pokeapi.co/api/v2/"

def getData(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            print("Error en la API :", res.status_code)
            return None
    except:
        print("Error de conexion")
        return None

def getAll(url):
    data = []
    while url:
        info = getData(url)
        if info:
            data.extend(info["results"])
            url = info["next"]
        else:
            break
        time.sleep(0.2)
    return data

def fuego_kanto():
    print("\nBuscando pokemones fuego en kanto...\n")
    tipo = getData(BASE + "type/fire")

    count = 0
    for p in tipo["pokemon"]:
        nombre = p["pokemon"]["name"]
        data = getData(p["pokemon"]["url"])

        if data and data["id"] <= 151:
            count += 1

    print("Total tipo fuego en KANTO:", count)

def agua_altos():
    print("\nPokemones tipo agua con altura > 10\n")
    tipo = getData(BASE + "type/water")

    lista = []
    for p in tipo["pokemon"]:
        data = getData(p["pokemon"]["url"])
        if data and data["height"] > 10:
            lista.append(data["name"])

    print("Resultado:")
    for x in lista[:20]:  # no spamear tanto
        print("-", x)

def evoluciones():
    nombre = input("Dime un pokemon inicial: ").lower()

    poke = getData(BASE + "pokemon/" + nombre)

    if not poke:
        print("No existe ese pokemon")
        return

    especie = getData(poke["species"]["url"])
    evo = getData(especie["evolution_chain"]["url"])

    print("\nCadena evolutiva:")

    cadena = evo["chain"]

    while cadena:
        print("-", cadena["species"]["name"])
        if cadena["evolves_to"]:
            cadena = cadena["evolves_to"][0]
        else:
            break

def electricos_sin_evo():
    print("\nElectricos sin evolucion\n")
    tipo = getData(BASE + "type/electric")

    lista = []

    for p in tipo["pokemon"]:
        data = getData(p["pokemon"]["url"])
        if not data:
            continue

        especie = getData(data["species"]["url"])
        evo = getData(especie["evolution_chain"]["url"])

        if evo["chain"]["species"]["name"] == data["name"] and not evo["chain"]["evolves_to"]:
            lista.append(data["name"])

    for x in lista:
        print("-", x)

def ataque_johto():
    print("\nBuscando mayor ataque en JOHTO...\n")

    mayor = 0
    nombre_top = ""

    for i in range(152, 252):  # johto
        data = getData(BASE + "pokemon/" + str(i))

        if not data:
            continue

        for stat in data["stats"]:
            if stat["stat"]["name"] == "attack":
                if stat["base_stat"] > mayor:
                    mayor = stat["base_stat"]
                    nombre_top = data["name"]

    print("Mayor ataque:", nombre_top, "-", mayor)

def velocidad_no_legendario():
    print("\nBuscando velocidad mas alta (no legendario)\n")

    mayor = 0
    nombre_top = ""

    lista = getAll(BASE + "pokemon?limit=200")

    for p in lista:
        data = getData(p["url"])
        if not data:
            continue

        especie = getData(data["species"]["url"])

        if especie["is_legendary"]:
            continue

        for stat in data["stats"]:
            if stat["stat"]["name"] == "speed":
                if stat["base_stat"] > mayor:
                    mayor = stat["base_stat"]
                    nombre_top = data["name"]

    print("Mas rapido:", nombre_top, "-", mayor)

def habitat_planta():
    print("\nHabitat mas comun tipo planta\n")

    tipo = getData(BASE + "type/grass")

    cont = {}

    for p in tipo["pokemon"]:
        data = getData(p["pokemon"]["url"])
        if not data:
            continue

        especie = getData(data["species"]["url"])

        if especie["habitat"]:
            h = especie["habitat"]["name"]
            cont[h] = cont.get(h, 0) + 1

    mayor = max(cont, key=cont.get)
    print("Habitat mas comun:", mayor)


def menor_peso():
    print("\nBuscando pokemon con menor peso...\n")

    menor = 999999
    nombre = ""

    lista = getAll(BASE + "pokemon?limit=200")

    for p in lista:
        data = getData(p["url"])
        if not data:
            continue

        if data["weight"] < menor:
            menor = data["weight"]
            nombre = data["name"]

    print("Menor peso:", nombre, "-", menor)


def menu():
    while True:
        print("\n===== MENU POKEMON ISA =====")
        print("1. Fuego en Kanto")
        print("2. Agua altura >10")
        print("3. Evoluciones")
        print("4. Electricos sin evo")
        print("5. Ataque Johto")
        print("6. Velocidad no legendario")
        print("7. Habitat planta")
        print("8. Menor peso")
        print("0. salir")

        op = input("elige: ")

        if op == "1":
            fuego_kanto()
        elif op == "2":
            agua_altos()
        elif op == "3":
            evoluciones()
        elif op == "4":
            electricos_sin_evo()
        elif op == "5":
            ataque_johto()
        elif op == "6":
            velocidad_no_legendario()
        elif op == "7":
            habitat_planta()
        elif op == "8":
            menor_peso()
        elif op == "0":
            print("bye")
            break
        else:
            print("opcion no valida")


if __name__ == "__main__":
    menu()
