# Model/Suggestion.py

# Suggestions de coups à jouer modélisés par un dictionnaire à deux clés :
# - POSITION : Position dans l'image
# - COULEUR : Couleur à placer (la couleur transparente, 0, étant acceptée)

# Deux clés associées au dictionnaire représentant une suggestion :
POSITION = "position"
COULEUR = "couleur"


from Model.CustomTypes import *
from Model.Position import *

def type_suggestion(suggestion: Suggestion) -> bool:
    """
    Détermine si le paramètre correspond ou non à une suggestion

    :param suggestion: Objet à tester
    :return: True s'il correspond à une suggestion, False sinon
    """
    if type(suggestion) is not dict:
        return False
    if POSITION not in suggestion or COULEUR not in suggestion:
        return False
    if not type_position(suggestion[POSITION]):
        return False
    if type(suggestion[COULEUR]) is not int:
        return False
    return True

def construireSuggestion(position: Position, couleur: int) -> dict:
    """
    Construit et retourne une suggestion à partir d'une position et d'une couleur.
    :param position: Position dans le nonogram
    :param couleur: Couleur suggérée
    :return:
    """
    assert type(position) == dict
    assert type(couleur) == int
    return {POSITION: position,
            COULEUR: couleur}

def getPositionSuggestion(suggestion: Suggestion) -> Position:
    """
    Retourne la position contenue dans une suggestion.
    :param suggestion: dictionnaire représentant une suggestion contenant au moins la clé POSITION
    :return: Position associée à la suggestion
    """
    assert type_suggestion(suggestion), "Le paramètre n'est pas une suggestion"
    return suggestion[POSITION]

def getCouleurSuggestion(suggestion: Suggestion) -> int:
    """
    Retourne la couleur contenue dans une suggestion.
    :param suggestion: dictionnaire représentant une suggestion contenant les clés POSITION et COULEUR
    :return: couleur associée à la suggestion
    """
    assert type_suggestion(suggestion), "Le paramètre n'est pas une suggestion"
    return suggestion[COULEUR]
