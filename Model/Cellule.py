# Model/Cellule.py
#

from Model.debug import debug
from Model.CustomTypes import Cellule

# Clé contenant la valeur d'une cellule
VALEUR = "value"

#
# La Cellule
#
# L'objet cellule va représenter une case de l'image (du nonogram)
#
# La cellule sera représentée par un dictionnaire.
# Une cellule pourra être :
#   - vide (absence de bille) : La valeur sera 0.
#   - non découverte (non connue) : la valeur sera None.
#   - une couleur (ou plutôt l'indice non nul d'une couleur, la palette sera fournie plus tard).
#



def type_cellule(cell: Cellule) -> bool:
    """
    Permet de vérifier si l'argument peut correspondre ou non à une cellule

    :param cell: Objet dont on veut tester le type
    :return: True s'il s'agit d'une cellule, False sinon.
    """
    if type(cell) is not dict:
        debug(f"La cellule {cell} n'est pas un dictionnaire")
        return False
    if VALEUR not in cell:
        debug(f"La clé VALUE ({VALEUR}) n'est pas dans le dictionnaire")
        return False
    if cell[VALEUR] is not None and type(cell[VALEUR]) is not int:
        debug(f"La valeur {cell[VALEUR]} n'est ni entière ni None ")
        return False
    return True


#=============== DEBUT DU CODE ===================================

def construireCellule() -> Cellule:
    """
    Renvoi un dictionnaire contenant la clé VALEUR dont la valeur est None
    :return: Une cellule du nonogram
    """
    cellule = {VALEUR : None}
    return cellule

def isVuCellule(cellule: Cellule) ->  bool:
    """
    Verifie si la cellule passé en paramètre est vue ou pas
    :param cellule: Une cellule du nonogram
    :return: La cellule est vue
    """
    assert type_cellule(cellule),"Le paramètre n'est pas une cellule"
    return cellule[VALEUR] is not None

def isVideCellule(cellule: Cellule) -> bool:
    """
    Verifie si la cellule passé en paramètre est vide ou pas
    :param cellule: Une cellule du nonogram
    :return: La cellule est vide
    """
    assert type_cellule(cellule), "Le paramètre n'est pas une cellule"
    return cellule[VALEUR] == 0

def getCouleurCellule(cellule: Cellule) -> int:
    """
    Renvoi la couleur de la cellule pris en paramètre
    :param cellule: Une cellule du nonogram
    :return: La couleur de la cellule pris en paramètre
    """
    assert type_cellule(cellule), "Le paramètre n'est pas une cellule"
    assert isVuCellule(cellule), "La cellule ne contient pas de couleur"
    return cellule[VALEUR]

def setCouleurCellule(cellule: Cellule, couleur: int) -> None:
    """
    Affecte une couleur à une cellule
    :param cellule: Une cellule du nonogram
    :param couleur: La couleur à affecter a la cellule
    :return: Rien
    """
    assert type_cellule(cellule), "Le paramètre n'est pas une cellule"
    assert type(couleur) == int, "Le paramètre n'est pas une couleur"
    cellule[VALEUR] = couleur
    return None

def setNonVuCellule(cellule: Cellule) -> None:
    """
    Affecte la valeur None a la cellule pris en paramètre
    :param cellule: Une cellule du nonogram
    :return: Rien
    """
    assert type_cellule(cellule), "Le paramètre n'est pas une cellule"
    cellule[VALEUR] = None
    return None
