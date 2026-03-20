# Création de classe pour les différentes pièces

class Piece:
    def __init__(self, couleur):
        self.couleur = couleur
        self.symbole = "?" # À définir par la suite

    def __str__(self):
        return self.symbole

class Pion(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = "\u2659" if couleur == "blanc" else "\u265F" # Unicode du symbole de : Pion

class Fou(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = "\u2657" if couleur == "blanc" else "\u265D" # Unicode du symbole de : Fou

class Cavalier(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = "\u2658" if couleur == "blanc" else "\u265E"  # Unicode du symbole de : Cavalier

class Tour(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = "\u2656" if couleur == "blanc" else "\u265C"  # Unicode du symbole de : Tour

class Roi(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = "\u2654" if couleur == "blanc" else "\u265A"  # Unicode du symbole de : Roi

class Reine(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.symbole = "\u2655" if couleur == "blanc" else "\u265B"  # Unicode du symbole de : Reine