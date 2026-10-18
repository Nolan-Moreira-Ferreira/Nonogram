# Model/Image.py

from Model.CustomTypes import Image
from Model.Cellule import *
from Model.Position import *

#
# Gestion simple des nonograms
#
# Accès simple en lecture et en écriture à une "image"
# Création d'une "image"...
#


def type_image_light(img: Image) -> bool:
    """
    Permet de vérifier que le paramètre correspond à une image.
    Renvoie True si c'est le cas, False sinon.

    Version light : Ne vérifie pas le contenu des listes...

    :param img: Objet qu'on veut tester
    :return: True s'il correspond à une image, False sinon
    """
    if type(img) is not list:
        return False
    wrong = "Erreur !"
    if len(img) == 0:
        return False
    if type(img[0]) is not list:
        return False
    n_c = len(img[0])
    if n_c != len(img):
        return False
    if next((wrong for line in img if type(line) is not list or len(line) != n_c), True) == wrong:
        return False
    return True


def type_image_full(img: Image) -> bool:
    """
    Permet de vérifier que le paramètre correspond à une image.
    Renvoie True si c'est le cas, False sinon.

    En plus de la version light, vérifie que le contenu des listes correspond bien à une cellule.

    :param img: Objet qu'on veut tester
    :return: True s'il correspond à une image, False sinon
    """
    if not type_image_light(img):
        return False
    wrong = "Erreur !"
    if next((wrong for line in img for c in line if c is not None and not type_cellule(c)), True) == wrong:
        return False
    return True

def getCellImage(image : Image, pos : Position) -> Cellule:
    """
    Renvoi la cellule dans l'image à la position pos
    :param image: L'image
    :param pos: La position de la cellule
    :return: la cellule de l'image
    """
    assert type_image_light(image), "Le paramètre n'est pas image"
    assert type_position(pos), "Le paramètre n'est pas une Position"
    cell = image[pos[LIGNE]][pos[COLONNE]]
    return cell

def setCellImage(image : Image, pos : Position, entier : int|None) -> None:
    """
    Remplace la couleur de l'image a la position pos par entier
    :param image: L'image
    :param pos: La position dans l'image
    :param entier: Soit un entier représentant une couleur soit None
    :return: Rien
    """
    assert type_image_light(image), "Le paramètre n'est pas image"
    assert type_position(pos), "Le paramètre n'est pas une Position"
    assert type(entier) is int or entier is None, "Le paramètre n'est pas un entier"
    image[pos[LIGNE]][pos[COLONNE]][VALEUR] = entier
    return None

def creerImage(taille : int, liste: list[list[int]]|None = None) -> Image:
    """

    :param taille:
    :param liste:
    :return:
    """
    assert type(taille) is int, "Le paramètre n'est pas un entier"
    assert 5 <= taille <= 20, "La taille n'est pas comprise entre 5 et 20"

    image = []

    if liste is not None:
        assert type_image_light(liste), "Le paramètre n'est pas une liste de liste"
        assert len(liste) == taille, "La taille des liste ne correspondes pas"

        for ligne in liste:
            assert len(ligne) == taille, "La taille des liste ne correspondes pas"

        for ligne in liste:
            nv_ligne = []
            for valeur in ligne:
                cell = construireCellule()
                cell[VALEUR] = valeur
                nv_ligne.append(cell)
            image.append(nv_ligne)
    else:
        image = []
        for li in range(taille):
            ligne = []
            for col in range(taille):
                ligne.append(construireCellule())
            image.append(ligne)
    return image