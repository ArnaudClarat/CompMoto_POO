from com.github.ArnaudClarat.CompMoto.Connexion import *


class MotosManager :
    # Manager de motos, gère la db

    # Attributs DB
    db = "test.db"
    conn = Connexion.new(db)
    cursor = Connexion.get_cursor(conn)
    print(cursor) # Test

    # Attibuts
    motos
