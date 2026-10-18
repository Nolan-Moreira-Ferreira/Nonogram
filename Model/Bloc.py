# Model/Bloc.py
#

from Model.CustomTypes import Bloc

# Clé pour stocker le nombre de cellules contigües de même couleur (bloc)
NOMBRE = "nombre"
# Couleur des cellules contigües du bloc
COULEUR = "couleur"
# Booléen permettant de savoir si l'utilisateur a découvert ou non le bloc correspondant
VU = "vu"


def type_bloc(bloc: Bloc) -> bool:
    """
    Détermine si le paramètre peut correspondre ou non à un bloc.

    Un bloc est un dictionnaire contenant 3 clés (NOMBRE, COULEUR, VU) auquelles
    sont associées des valeurs de type (int, int, bool).

    :param bloc: Objet à tester
    :return: True si l'objet correspond à un bloc, False sinon.
    """
    if type(bloc) is not dict:
        return False
    if len(bloc) != 3 or NOMBRE not in bloc or COULEUR not in bloc or VU not in bloc:
        return False
    if type(bloc[NOMBRE]) is not int or bloc[NOMBRE]<=0:
        return False
    if type(bloc[COULEUR]) is not int or bloc[COULEUR]<=0:
        return False
    if type(bloc[VU]) is not bool:
        return False
    return True

def construireBloc(nb_cell: int, couleur: int) -> Bloc:
    """
    Construit un dictionnaire pour en faire un bloc du nonogram
    :param nb_cell: Nombre de cellule du bloc
    :param couleur: Couleur du bloc
    :return: Le bloc
    """
    assert type(nb_cell) is int, "le paramètre n'est pas un entier"
    assert type(couleur) is int, "le paramètre n'est pas un entier"
    assert nb_cell > 0, "le paramètre n'est pas strictement positif"
    assert couleur > 0, "le paramètre n'est pas strictement positif"
    bloc = {NOMBRE : nb_cell, COULEUR : couleur, VU : False}
    return bloc

def getNombreBloc(bloc: Bloc) -> int:
    """
    Renvoi le nombre de bloc dans le dictionnaire Bloc
    :param bloc: Un bloc du nonogram
    :return: le nombre de bloc
    """
    assert type_bloc(bloc), "Le paramètre n'est ps un Bloc"
    return bloc[NOMBRE]

def getCouleurBloc(bloc: Bloc) -> int:
    """
    Renvoi la couleur du bloc dans le dictionnaire Bloc
    :param bloc: Un bloc du nonogram
    :return: la couleur du bloc
    """
    assert type_bloc(bloc), "Le paramètre n'est ps un Bloc"
    return bloc[COULEUR]

def isVuBloc(bloc: Bloc) -> bool:
    """
    Renvoi True si le bloc est deja vu, False sinon
    :param bloc: Un bloc du nonogram
    :return: True si le bloc est deja vu, False sinon
    """
    assert type_bloc(bloc), "Le paramètre n'est pas un Bloc"
    return bloc[VU]

def setVuBloc(bloc: Bloc, vu: bool) -> None:
    """
    Affecte la valeur de vu au dictionnaire bloc à la clé VU
    :param bloc: Un bloc du nonogram
    :param vu: Si le bloc est vu
    :return: Rien
    """
    assert type_bloc(bloc), "Le paramètre n'est pas un Bloc"
    assert type(vu) is bool, "Le paramètre n'est pas un booléen"
    bloc[VU] = vu
    return None
