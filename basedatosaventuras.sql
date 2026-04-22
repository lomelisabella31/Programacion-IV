PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS misiones_monstruos;
DROP TABLE IF EXISTS misiones_heroes;
DROP TABLE IF EXISTS monstruos;
DROP TABLE IF EXISTS misiones;
DROP TABLE IF EXISTS heroes;

CREATE TABLE heroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clase TEXT NOT NULL,
    nivel_experiencia INTEGER NOT NULL CHECK (nivel_experiencia >= 1)
);

CREATE TABLE misiones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    dificultad TEXT NOT NULL CHECK (dificultad IN ('facil', 'media', 'dificil', 'epica')),
    localizacion TEXT NOT NULL,
    recompensa INTEGER NOT NULL CHECK (recompensa >= 0)
);

CREATE TABLE monstruos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    nivel_amenaza INTEGER NOT NULL CHECK (nivel_amenaza BETWEEN 1 AND 10)
);

CREATE TABLE misiones_heroes (
    id_heroe INTEGER NOT NULL,
    id_mision INTEGER NOT NULL,
    PRIMARY KEY (id_heroe, id_mision),
    FOREIGN KEY (id_heroe) REFERENCES heroes(id),
    FOREIGN KEY (id_mision) REFERENCES misiones(id)
);

CREATE TABLE misiones_monstruos (
    id_mision INTEGER NOT NULL,
    id_monstruo INTEGER NOT NULL,
    PRIMARY KEY (id_mision, id_monstruo),
    FOREIGN KEY (id_mision) REFERENCES misiones(id),
    FOREIGN KEY (id_monstruo) REFERENCES monstruos(id)
);

INSERT INTO heroes (nombre, clase, nivel_experiencia) VALUES
('Jesus', 'Guerrero', 10),
('Cesar', 'Mago', 12),
('Alberto', 'Arquero', 9);

INSERT INTO misiones (nombre, dificultad, localizacion, recompensa) VALUES
('Rescate en la cueva', 'media', 'Montañas del norte', 500),
('Caza del dragon', 'epica', 'Volcan oscuro', 1500),
('Defensa del reino', 'dificil', 'Ciudad central', 1000);

INSERT INTO monstruos (nombre, tipo, nivel_amenaza) VALUES
('Smaug', 'Dragon', 10),
('Goblin oscuro', 'Goblin', 4),
('Esqueleto guerrero', 'No-muerto', 6);

INSERT INTO misiones_heroes (id_heroe, id_mision) VALUES
(1,1),
(2,1),
(3,2),
(1,2),
(2,3);

INSERT INTO misiones_monstruos (id_mision, id_monstruo) VALUES
(1,2),
(2,1),
(2,2),
(3,3);
