import sqlite3


class Connexion:

    # Attributs
    cursor = ""


    # Méthodes
    @classmethod
    def new(cls, db):
        return sqlite3.connect(db)

    @classmethod
    def get_cursor(cls, conn):
        return conn.cursor()
