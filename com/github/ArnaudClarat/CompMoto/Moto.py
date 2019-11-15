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
    @property
    def _prix(self):
        return self.prix

    @_prix.setter
    def _prix(self, v):
        self.prix = v
