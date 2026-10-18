# Model/Nonogram.py
from Model.Image import *
from Model.Bloc import *
from Model.CustomTypes import *
from Model.Cellule import *

VALEUR = "value"

def compterBlocsSurLigne(image: ModelImage, num_ligne: int) -> LstBlocs:
    """
    Compte les blocs présents sur une ligne de l'image.

    :param image: Image du modèle
    :param num_ligne: Numéro de la ligne à analyser
    :return: Liste des blocs trouvés sur la ligne
    """
    assert type_image_light(image), "Le paramètre n'est pas une Image"
    assert type(num_ligne) is int, "Le paramètre n'est pas un entier"
    blocs: LstBlocs = []
    couleur_courante = None
    compteur = 0
    for cellule in image[num_ligne]:
        couleur = cellule[VALEUR]
        if couleur == 0:
            if compteur > 0:
                blocs.append(construireBloc(compteur, couleur_courante))
                compteur = 0
                couleur_courante = None
        else:
            if couleur == couleur_courante:
                compteur += 1
            else:
                if compteur > 0:
                    blocs.append(construireBloc(compteur, couleur_courante))
                couleur_courante = couleur
                compteur = 1
    if compteur > 0:
        blocs.append(construireBloc(compteur, couleur_courante))
    return blocs

def getBlocsLignes(image: Image) -> LstLstBlocs:
    """
    Renvoi une liste de liste contenant le nombre de blocs par ligne
    :param image: Image du modèle
    :return: Ine liste de liste contenant le nombre de blocs par ligne
    """
    blocs_lignes: LstLstBlocs = []
    for ligne in range(len(image)):
        blocs_lignes.append(compterBlocsSurLigne(image, ligne))
    return blocs_lignes

def compterBlocsSurColonne(image: Image, num_colonne: int) -> LstBlocs:
    """
    Compte les blocs présents sur une colonne de l'image.
    :param image: Image du modèle
    :param num_colonne: Numéro de la colonne à analyser
    :return: Liste des blocs trouvés sur la colonne
    """
    assert type_image_light(image), "Le paramètre n'est pas une Image"
    assert type(num_colonne) is int, "Le paramètre n'est pas un entier"
    blocs: LstBlocs = []
    couleur_courante = None
    compteur = 0
    for ligne in range(len(image)):
        cellule = image[ligne][num_colonne]
        valeur = cellule[VALEUR]
        if valeur == 0:
            if compteur > 0:
                blocs.append(construireBloc(compteur, couleur_courante))
                compteur = 0
                couleur_courante = None
        else:
            if valeur == couleur_courante:
                compteur += 1
            else:
                if compteur > 0:
                    blocs.append(construireBloc(compteur, couleur_courante))
                couleur_courante = valeur
                compteur = 1
    if compteur > 0:
        blocs.append(construireBloc(compteur, couleur_courante))
    return blocs

def getBlocsColonnes(image: Image) -> LstLstBlocs:
    """
    Retourne la liste des blocs pour chaque colonne de l'image.
    :param image: Image du modèle
    :return: Liste de listes de blocs, un élément par colonne
    """
    blocs_colonnes: LstLstBlocs = []
    for j in range(len(image)):
        blocs_colonnes.append(compterBlocsSurColonne(image, j))
    return blocs_colonnes

def isVuImage(image_joueur: PlayerImage) -> bool:
    """
    Indique si toutes les cellules de l'image du joueur sont découvertes.
    :param image_joueur: Image du joueur
    :return: True si toutes les cellules sont vues, False sinon
    """
    for ligne in image_joueur:
        for cellule in ligne:
            if cellule[VALEUR] is None:
                return False
    return True

def reinitialiserImage(img_joueur: PlayerImage) -> None:
    """
    Fonction réinitialisant l'image du joueur
    :param img_joueur: image du joueur à réinitialiser
    :raise AssertionError: si le paramètre n'est pas une image
    """
    assert type_image_light(img_joueur), "Le paramètre doit être une image"

    for ligne in img_joueur:
        for cell in ligne:
            setNonVuCellule(cell)
    return None

def verifierBlocsLigneImage(img_joueur: PlayerImage,blocs: LstBlocs,ligne: int) -> bool:
    """
    Vérifie si des blocs d'une ligne sont découverts et met à jour leur état.
    :param img_joueur: image du joueur
    :param blocs: liste des blocs de la ligne
    :param ligne: numéro de la ligne
    :return: True si au moins un bloc a été marqué comme vu, False sinon
    """
    modifie = False
    taille = len(img_joueur)
    col = 0
    idx_bloc = 0
    while (col < taille and idx_bloc < len(blocs) and
           img_joueur[ligne][col][VALEUR] is not None):
        couleur = img_joueur[ligne][col][VALEUR]
        if couleur == 0:
            col += 1
        else:
            longueur = 0
            while (col < taille and
                   img_joueur[ligne][col][VALEUR] is not None and
                   img_joueur[ligne][col][VALEUR] == couleur):
                longueur += 1
                col += 1
            if (getNombreBloc(blocs[idx_bloc]) == longueur and
                    getCouleurBloc(blocs[idx_bloc]) == couleur and
                    not isVuBloc(blocs[idx_bloc])):
                setVuBloc(blocs[idx_bloc], True)
                modifie = True
            idx_bloc += 1
    col = taille - 1
    idx_bloc = len(blocs) - 1
    while (col >= 0 and idx_bloc >= 0 and
           img_joueur[ligne][col][VALEUR] is not None):
        couleur = img_joueur[ligne][col][VALEUR]
        if couleur == 0:
            col -= 1
        else:
            longueur = 0
            while (col >= 0 and
                   img_joueur[ligne][col][VALEUR] is not None and
                   img_joueur[ligne][col][VALEUR] == couleur):
                longueur += 1
                col -= 1
            if (getNombreBloc(blocs[idx_bloc]) == longueur and
                    getCouleurBloc(blocs[idx_bloc]) == couleur and
                    not isVuBloc(blocs[idx_bloc])):
                setVuBloc(blocs[idx_bloc], True)
                modifie = True
            idx_bloc -= 1
    return modifie

def verifierBlocsColonneImage(img_joueur: PlayerImage,blocs: LstBlocs,colonne: int) -> bool:
    """
    Vérifie si des blocs d'une colonne sont découverts et met à jour leur état.
    :param img_joueur: image du joueur
    :param blocs: liste des blocs de la colonne
    :param colonne: numéro de la colonne
    :return: True si au moins un bloc a été marqué comme vu, False sinon
    """
    modifie = False
    taille = len(img_joueur)
    ligne = 0
    idx_bloc = 0
    while (ligne < taille and idx_bloc < len(blocs) and
           img_joueur[ligne][colonne][VALEUR] is not None):
        couleur = img_joueur[ligne][colonne][VALEUR]
        if couleur == 0:
            ligne += 1
        else:
            longueur = 0
            while (ligne < taille and
                   img_joueur[ligne][colonne][VALEUR] is not None and
                   img_joueur[ligne][colonne][VALEUR] == couleur):
                longueur += 1
                ligne += 1
            if (getNombreBloc(blocs[idx_bloc]) == longueur and
                    getCouleurBloc(blocs[idx_bloc]) == couleur and
                    not isVuBloc(blocs[idx_bloc])):
                setVuBloc(blocs[idx_bloc], True)
                modifie = True
            idx_bloc += 1
    ligne = taille - 1
    idx_bloc = len(blocs) - 1
    while (ligne >= 0 and idx_bloc >= 0 and
           img_joueur[ligne][colonne][VALEUR] is not None):
        couleur = img_joueur[ligne][colonne][VALEUR]
        if couleur == 0:
            ligne -= 1
        else:
            longueur = 0
            while (ligne >= 0 and
                   img_joueur[ligne][colonne][VALEUR] is not None and
                   img_joueur[ligne][colonne][VALEUR] == couleur):
                longueur += 1
                ligne -= 1
            if (getNombreBloc(blocs[idx_bloc]) == longueur and
                    getCouleurBloc(blocs[idx_bloc]) == couleur and
                    not isVuBloc(blocs[idx_bloc])):
                setVuBloc(blocs[idx_bloc], True)
                modifie = True
            idx_bloc -= 1
    return modifie

def isLigneDecouverteImage(img_joueur: PlayerImage,
                           blocs: LstBlocs,
                           ligne: int) -> bool:
    """
    Indique si une ligne est complètement découverte.
    :param img_joueur: image du joueur
    :param blocs: liste des blocs de la ligne
    :param ligne: numéro de la ligne
    :return: True si la ligne est découverte, False sinon
    """
    somme_blocs = 0
    for bloc in blocs:
        somme_blocs += getNombreBloc(bloc)
    nb_cellules = 0
    for col in range(len(img_joueur)):
        valeur = img_joueur[ligne][col][VALEUR]
        if valeur is not None and valeur != 0:
            nb_cellules += 1
    return somme_blocs == nb_cellules

def getCellsNonVuesLigneImage(img_joueur: PlayerImage,ligne: int) -> list[int]:
    """
    Retourne les indices de colonnes des cellules non découvertes d'une ligne.
    :param img_joueur: image du joueur
    :param ligne: numéro de la ligne
    :return: liste des numéros de colonnes non découvertes
    """
    cellules = []
    for col in range(len(img_joueur)):
        if img_joueur[ligne][col][VALEUR] is None:
            cellules.append(col)
    return cellules

def isColonneDecouverteImage(img_joueur: PlayerImage,blocs: LstBlocs,colonne: int) -> bool:
    """
    Indique si une colonne est complètement découverte.
    :param img_joueur: image du joueur
    :param blocs: liste des blocs de la colonne
    :param colonne: numéro de la colonne
    :return: True si la colonne est découverte, False sinon
    """
    somme_blocs = 0
    for bloc in blocs:
        somme_blocs += getNombreBloc(bloc)
    nb_cellules = 0
    for ligne in range(len(img_joueur)):
        valeur = img_joueur[ligne][colonne][VALEUR]
        if valeur is not None and valeur != 0:
            nb_cellules += 1
    return somme_blocs == nb_cellules

def getCellsNonVuesColonneImage(img_joueur: PlayerImage,colonne: int) -> list[int]:
    """
    Retourne les indices des lignes des cellules non découvertes d'une colonne.
    :param img_joueur: image du joueur
    :param colonne: numéro de la colonne
    :return: liste des indices de lignes non découvertes
    """
    cellules = []
    for ligne in range(len(img_joueur)):
        if img_joueur[ligne][colonne][VALEUR] is None:
            cellules.append(ligne)
    return cellules

def getNbParCouleur(taille: int,blocs: LstBlocs) -> dict[int, int]:
    """
    Retourne le nombre de cellules par couleur pour une ligne ou une colonne.
    :param taille: taille de la ligne ou colonne
    :param blocs: liste des blocs
    :return: dictionnaire {couleur: nombre de cellules}
    """
    nb_par_couleur = {}
    total = 0
    for ligne in blocs:
        for bloc in ligne:
            couleur = bloc[COULEUR]
            nombre = bloc[NOMBRE]
            if couleur not in nb_par_couleur:
                nb_par_couleur[couleur] = 0
            nb_par_couleur[couleur] += nombre
            total += nombre
    total_cell = taille ** 2
    nb_par_couleur[0] = total_cell - total
    return nb_par_couleur

def getCouleursVuImage(image_joueur: PlayerImage, nb_par_couleur: NbParCouleur) -> LstCouleurs:
    """
    Retourne la liste des couleurs pour lesquelles toutes les cellules
    ont été découvertes dans l'image du joueur.
    :param image_joueur: Image du joueur
    :param nb_par_couleur: nombre de cellule par couleur
    :return:
    """
    couleurs_vues = {}
    for ligne in image_joueur:
        for cell in ligne:
            val = cell[VALEUR]
            if val is not None:
                if val not in couleurs_vues:
                    couleurs_vues[val] = 0
                couleurs_vues[val] += 1
    resu = []
    for couleur, total in nb_par_couleur.items():
        if couleur in couleurs_vues and couleurs_vues[couleur] == total:
            resu.append(couleur)
    return resu