import sqlite3

class DataBase():
    
    def __init__(self):
        self.database = sqlite3.connect("rolas.db")
        self.cursor = self.database.cursor()
        self.create_types_table()
       # self.insert()
        self.create_performers_table()
        self.create_persons_table()
        self.create_groups_table()
        self.create_albums_table()
        self.create_tracks_table()
        self.create_table_in_groups()

    def create_types_table(self):
        types = [
            """
            CREATE TABLE IF NOT EXISTS types(
                id_type     INTEGER,
                description TEXT
            );
            """
        ]
        for type_ in types:
            self.database.execute(type_)

    def insert(self):
        person = [
            """
            INSERT INTO types VALUES(0,'Person');
            """
            ]
        for p in person:
            self.database.execute(p)
        group = [
            """
            INSERT INTO types VALUES(1,'Group');
            """
            ]
        for g in group:
            self.database.execute(g)
        unknown = [
            """
            INSERT INTO types VALUES(2,'Unknown');
            """
            ]
        for unk in unknown:
            self.database.execute(unk)

    def create_performers_table(self):
        performers = [
            """
            CREATE TABLE IF NOT EXISTS performers(
                id_performer    INTEGER PRIMARY KEY,
                id_type         INTEGER,
                name            TEXT,
                FOREIGN KEY     (id_type) REFERENCES types(id_type)
            );
            """
        ]
        for performer in performers:
            self.database.execute(performer)

    def create_persons_table(self):
        persons = [
            """
            CREATE TABLE IF NOT EXISTS persons(
                id_person   INTEGER PRIMARY KEY,
                stage_name  TEXT,
                real_name   TEXT,
                birth_date  TEXT,
                end_date    TEXT
            );
            """
        ]
        for person in persons:
            self.database.execute(person)

    def create_groups_table(self):
        groups = [
            """
            CREATE TABLE IF NOT EXISTS groups(
                id_group    INTEGER PRIMARY KEY,
                name        TEXT,
                start_date  TEXT,
                end_date    TEXT
            );
            """
        ]
        for group in groups:
            self.database.execute(group)

    def create_albums_table(self):
        albums = [
            """
            CREATE TABLE IF NOT EXISTS albums(
                id_album    INTEGER PRIMARY KEY,
                path        TEXT,
                name        TEXT,
                year        INTEGER
            );
            """
        ]
        for album in albums:
            self.database.execute(album)

    def create_tracks_table(self):
        tracks = [
            """
            CREATE TABLE IF NOT EXISTS tracks(
                id_track        INTEGER PRIMARY KEY,
                id_performer    INTEGER,
                id_album        INTEGER,
                path            TEXT,
                title           TEXT,
                track           INTEGER,
                year            INTEGER,
                genre           TEXT,
                FOREIGN KEY     (id_performer) REFERENCES performers(id_performer),
                FOREIGN KEY     (id_album) REFERENCES albums(id_album)
            );
            """
        ]
        for track in tracks:
            self.database.execute(track)

    def create_table_in_groups(self):
        in_groups = [
            """
            CREATE TABLE IF NOT EXISTS in_group(
                id_person   INTEGER,
                id_group    INTEGER,
                PRIMARY KEY (id_person, id_group),
                FOREIGN KEY (id_person) REFERENCES persons(id_person),
                FOREIGN KEY (id_group) REFERENCES groups(id_group)
            );
            """
        ]
        for in_group in in_groups:
            self.database.execute(in_group)
