# Model/Position.py
from Model.debug import *
from Model.CustomTypes import Position


#
# Les positions ne sont pas toujours faciles à gérer !
#
# Sur une image, quand on parle d'un pixel (x, y), x représente la colonne et y la ligne.
# Dans un tableau, quand on cherche la valeur tab[i][j], cette fois, c'est i qui désigne la ligne et j la colonne.
#
# Pour tenter d'éviter d'intervertir ligne/colonne, on va créer un dictionnaire avec deux clés bien explicites
# - la clé LIGNE qui représentera le numéro de ligne
# - la clé COLONNE qui représentera le numéro de colonne
#

LIGNE = "ligne"
COLONNE = "colonne"



def type_position(position: Position) -> bool:
    """
    Fonction permettant de déterminer si le paramètre peut représenter ou non une position.

    Cette fonction ne peut valider la valeur des lignes/colonnes

    :param position: Position à tester
    :return: True si le paramètre correspond à une position, False sinon
    """
    if type(position) is not dict:
        debug(f"Le paramètre {position} n'est pas un dictionnaire")
        return False
    if LIGNE not in position or COLONNE not in position:
        debug(f"Le dictionnaire {position} ne contient pas une des clés {LIGNE} ou {COLONNE}")
        return False
    if type(position[LIGNE]) is not int or type(position[COLONNE]) is not int:
        debug(f"Une des valeurs du dictionnaire {position} n'est pas un entier")
        return False
    return True


#============== DEBUT DU CODE ============================

def construirePosition() -> Position:
    """
    Crée une position à la valeur 0 aux clé COLONNE et LIGNE
    :return: La position crée par la fonction
    """
    Position = {COLONNE : 0, LIGNE : 0}
    return Position

def getLignePosition(pos : Position) -> int:
    """
    Renvoi le numéro de la ligne
    :param pos: La position dans la nonogram
    :return: Le numéro de la ligne
    """
    assert type_position(pos),"Le paramètre n'est pas une Position"
    return pos[LIGNE]

def getColonnePosition(pos : Position) -> int:
    """
    Renvoi le numéro de la colonne
    :param pos: La position dans la nonogram
    :return: Le numéro de la colonne
    """
    assert type_position(pos),"Le paramètre n'est pas une Position"
    return pos[COLONNE]

def setLignePosition(pos : Position, ligne : int) -> None:
    """
    Affecte l'entier ligne a la position en tant que valeur de LIGNE
    :param pos: La position dans la nonogram
    :param int: le numéro à affecter à la position
    :return: Rien
    """
    assert type_position(pos), "Le paramètre n'est pas une Position"
    assert type(ligne) is int, "Le paramètre n'est pas unu entier"
    pos[LIGNE] = ligne
    return None

def setColonnePosition(pos : Position, colonne : int) -> None:
    """
    Affecte l'entier colonne a la position en tant que valeur de COLONNE
    :param pos: La position dans la nonogram
    :param int: le numéro à affecter à la position
    :return: Rien
    """
    assert type_position(pos), "Le paramètre n'est pas une Position"
    assert type(colonne) is int, "Le paramètre n'est pas unu entier"
    pos[COLONNE] = colonne
    return None

def incLignePosition(pos : Position, incrementation : int = 1) -> None:
    """
    Incrémente le ligne avec la valeur passé en paramètre
    :param pos: la position dans la nonnogram
    :param incrementation: la valeur à incrémenter
    :return: Rien
    """
    assert type_position(pos), "Le paramètre n'est pas une Position"
    assert type(incrementation) is int, "Le paramètre n'est pas unu entier"
    pos[LIGNE] += incrementation
    return None

def incColonnePosition(pos : Position, incrementation : int = 1) -> None:
    """
    Incrémente le colonne avec la valeur passé en paramètre
    :param pos: la position dans la nonnogram
    :param incrementation: la valeur à incrémenter
    :return: Rien
    """
    assert type_position(pos), "Le paramètre n'est pas une Position"
    assert type(incrementation) is int, "Le paramètre n'est pas unu entier"
    pos[COLONNE] += incrementation
    return None

def decLignePosition(pos : Position, decrementation : int = 1) -> None:
    """
    Décrémente le ligne avec la valeur passé en paramètre
    :param pos: la position dans la nonnogram
    :param decrementation: la valeur à incrémenter
    :return: Rien
    """
    assert type_position(pos), "Le paramètre n'est pas une Position"
    assert type(decrementation) is int, "Le paramètre n'est pas unu entier"
    pos[LIGNE] -= decrementation
    return None

def decColonnePosition(pos : Position, decrementation : int = 1) -> None:
    """
    Décrémente le colonne avec la valeur passé en paramètre
    :param pos: la position dans la nonnogram
    :param decrementation: la valeur à incrémenter
    :return: Rien
    """
    assert type_position(pos), "Le paramètre n'est pas une Position"
    assert type(decrementation) is int, "Le paramètre n'est pas unu entier"
    pos[COLONNE] -= decrementation
    return None

