class Moto :

    # Attributs
    prix = 0
    marque = ""
    modele = ""
    puissance = ""
    conso = ""
    reserv = ""
    autonomie = ""
    prix = ""
    notePerso = ""

    # Méthodes
    def __getattribute__(self, item):
        print("getting `{}`".format(str(item)))
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print("setting `{}` to `{}`".format(str(value), str(key)))
        try:
            return object.__setattr__(self, key, value)
        except AttributeError:
            return False
