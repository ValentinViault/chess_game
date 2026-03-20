from pieces import Pion, Fou, Cavalier, Tour, Reine, Roi

# Création d'un jeu d'échecs en Python

# Commençons par le plateau, vide, de 8*8 cases
plateau = [[None for _ in range(8)] for _ in range(8)]

# Plaçons nos pions sur l'échiquier :
for col in range(8):
    plateau[1][col] = Pion("blanc")
    plateau[6][col] = Pion("noir")

# Maintenant, les pièces principales :
# Pièces Blanches
plateau[0][0] = Tour("blanc")
plateau[0][7] = Tour("blanc")
plateau[0][1] = Cavalier("blanc")
plateau[0][6] = Cavalier("blanc")
plateau[0][2] = Fou("blanc")
plateau[0][5] = Fou("blanc")
plateau[0][3] = Reine("blanc")
plateau[0][4] = Roi("blanc")

# Pièces Noires
plateau[7][0] = Tour("noir")
plateau[7][7] = Tour("noir")
plateau[7][1] = Cavalier("noir")
plateau[7][6] = Cavalier("noir")
plateau[7][2] = Fou("noir")
plateau[7][5] = Fou("noir")
plateau[7][3] = Reine("noir")
plateau[7][4] = Roi("noir")


# Dictionnaire et fonctions de conversion
colonne_dict = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5,
    "G" : 6,
    "H" : 7
}

def position_to_indice(pos):
    lettre = pos[0].upper()
    chiffre = pos[1]
    col = colonne_dict[lettre]
    ligne = 8 - int(chiffre)
    return ligne, col


# Puis affichons le plateau
def afficher_plateau() :
    for ligne in plateau:
        print(" ".join(str(piece)if piece else "." for piece in ligne))

# Fonction pour le déplacement des pièces

def deplacer_piece(dep, arr):
    plateau[arr[0]][arr[1]] = plateau[dep[0]][dep[1]]
    plateau[dep[0]][dep[1]] = None

# Moteur interactif
while True:
    afficher_plateau()

    dep_pos = input("Case de départ (ex: C2, ou 'Q' pour quitter) : ").upper()
    if dep_pos == "Q":
        break

    arr_pos = input("Case d'arrivée (ex: C3) : ").upper()

    try:
        dep = position_to_indice(dep_pos)
        arr = position_to_indice(arr_pos)

        if plateau[dep[0]][dep[1]] is None:
            print("Pas de pièce à cette case, recommence !\n")
            continue

        deplacer_piece(dep, arr)

    except KeyError:
        print("Position invalide, recommence !\n")
    except ValueError:
        print("Format invalide, recommence !\n")