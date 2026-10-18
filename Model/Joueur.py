# Model/Joueur.py

from Model.CustomTypes import *
from Model.Image import *
from Model.Cellule import *
from Model.Bloc import *
from Model.Suggestion import *
from Model.Nonogram import *


def isVuCellJoueur(image_joueur : PlayerImage, position : Position) -> bool:
    """
    Indique si une cellule de l'image du joueur a déjà été découverte.
    :param image_joueur: Image du joueur
    :param position: Position de la cellule
    :return: True si la cellule est découverte, False sinon
    """
    cellule = getCellImage(image_joueur, position)
    return cellule[VALEUR] is not None

def isCouleurCorrecteImage(image: Image, position: Position, couleur: int) -> bool:
    """
    Vérifie si la couleur proposée correspond à celle de l'image du jeu.

    :param image: Image du modèle
    :param position: Position de la cellule
    :param couleur: Couleur proposée
    :return: True si la couleur est correcte, False sinon
    """
    cellule = getCellImage(image, position)
    return cellule[VALEUR] == couleur

def isLigneNonVueImage(image_joueur: PlayerImage, ligne: int) -> bool:
    """
    Indique si une ligne de l'image du joueur ne contient aucune cellule découverte.
    :param image_joueur: image du joueur
    :param ligne: numéro de la ligne (commençant à 0)
    :return: True si la ligne ne possède aucune cellule découverte, False sinon
    """
    non_vue = True
    for cellule in image_joueur[ligne]:
        if getCouleurCellule(cellule) != 0:
            non_vue = False
    return non_vue

def isColonneNonVueImage(image_joueur: PlayerImage, colonne: int) -> bool:
    """
    Indique si une colonne de l'image du joueur ne contient aucune cellule découverte.
    :param image_joueur: image du joueur
    :param colonne: numéro de la colonne (commençant à 0)
    :return: True si la colonne ne possède aucune cellule découverte, False sinon
    """
    non_vue = True
    for ligne in image_joueur:
        if getCouleurCellule(ligne[colonne]) != 0:
            non_vue = False
    return non_vue

def appliquerMonoRecouvrementLigne(image_joueur: PlayerImage,ligne: int,blocs: LstBlocs) -> LstSuggestions:
    """
    La fonction reçoit l'image du joueur, un numéro de ligne et la liste des blocs
    associés à cette ligne. Elle retourne la liste des suggestions déduites à partir
    de la règle de mono-recouvrement. S'il n'y a aucune suggestion possible, la fonction retourne une
    liste vide.
    :param image_joueur: image du joueur
    :param ligne: numéro de la ligne
    :param blocs: liste des blocs de la ligne
    :return: liste des suggestions générées
    """
    suggestions = []
    largeur = len(image_joueur[ligne])
    position_min = 0
    for bloc in blocs:
        taille_bloc = bloc[NOMBRE]
        couleur = bloc[COULEUR]
        position_max = largeur - taille_bloc
        debut_recouvrement = position_max
        fin_recouvrement = position_min + taille_bloc - 1
        if debut_recouvrement <= fin_recouvrement:
            for col in range(debut_recouvrement, fin_recouvrement + 1):
                cellule = image_joueur[ligne][col]
                if not isVuCellule(cellule):
                    suggestions.append(
                        construireSuggestion({"ligne": ligne, "colonne": col},couleur))
        position_min += taille_bloc + 1
    return suggestions

def appliquerMonoRecouvrementColonne(image_joueur: PlayerImage,colonne: int,blocs: LstBlocs) -> LstSuggestions:
    """
    La fonction reçoit l'image du joueur, un numéro de colonne et la liste des blocs
    associés à cette ligne. Elle retourne la liste des suggestions déduites à partir
    de la règle de mono-recouvrement. S'il n'y a aucune suggestion possible, la fonction retourne une
    liste vide.
    :param image_joueur: image du joueur
    :param colonne: numéro de la colonne
    :param blocs: liste des blocs de la colonne
    :return: liste des suggestions
    """
    suggestions = []
    hauteur = len(image_joueur)
    position_min = 0
    for bloc in blocs:
        taille_bloc = bloc[NOMBRE]
        couleur = bloc[COULEUR]
        position_max = hauteur - taille_bloc
        debut_recouvrement = position_max
        fin_recouvrement = position_min + taille_bloc - 1
        if debut_recouvrement <= fin_recouvrement:
            for lig in range(debut_recouvrement, fin_recouvrement + 1):
                cellule = image_joueur[lig][colonne]
                if not isVuCellule(cellule):
                    suggestions.append(
                        construireSuggestion({"ligne": lig, "colonne": colonne},couleur))
        position_min += taille_bloc + 1
    return suggestions

def appliquerMonoRecouvrement(image_joueur: PlayerImage,blocs_lignes: LstLstBlocs,blocs_colonnes: LstLstBlocs) -> LstSuggestions:
    """
    Applique la règle de mono-recouvrement sur l'ensemble de l'image du joueur,
    pour toutes les lignes et toutes les colonnes.
    :param image_joueur: image du joueur
    :param blocs_lignes: listes des blocs des lignes
    :param blocs_colonnes: listes des blocs des colonnes
    :return: liste de toutes les suggestions possibles
    """
    suggestions = []
    for ligne in range(len(blocs_lignes)):
        suggestions_ligne = appliquerMonoRecouvrementLigne(image_joueur, ligne, blocs_lignes[ligne])
        suggestions += suggestions_ligne
    for col in range(len(blocs_colonnes)):
        suggestions_colonne = appliquerMonoRecouvrementColonne(image_joueur, col, blocs_colonnes[col])
        suggestions += suggestions_colonne
    return suggestions

def appliquerMonoGlueBordRangee(rangee: list, blocs: LstBlocs) -> LstIndexCouleurs:
    """
    Applique la règle de mono-glue bord sur une rangée.

    :param rangee: rangée de l'image du joueur
    :param blocs: liste des blocs de la rangée
    :return: liste des suggestions possibles pour cette rangée
    """
    suggestions = []
    if blocs:
        taille_rangee = len(rangee)
        bloc = blocs[0]
        taille_bloc = bloc[NOMBRE]
        couleur_bloc = bloc[COULEUR]
        idx = 0
        while idx < taille_rangee and rangee[idx] is None:
            idx += 1
        if idx < taille_rangee:
            if rangee[idx] == 0:
                for i in range(min(taille_bloc, idx)):
                    suggestions.append((i, 0))
            else:
                debut_bloc = idx
                fin_bloc = debut_bloc + taille_bloc
                for i in range(debut_bloc, min(fin_bloc, taille_rangee)):
                    if rangee[i] is None:
                        suggestions.append((i, couleur_bloc))
                if fin_bloc < taille_rangee and rangee[fin_bloc] is None:
                    suggestions.append((fin_bloc, 0))
    return suggestions

def indexCouleursToSuggestions(lst_index_couleurs: LstIndexCouleurs,num: int,est_ligne: bool) -> LstSuggestions:
    """
    Construit une liste de suggestions à partir d'une liste d'index et de couleurs.
    :param lst_index_couleurs: liste de couples (index, couleur)
    :param num: numéro de la ligne ou de la colonne
    :param est_ligne: True si ligne, False si colonne
    :return: liste des suggestions correspondantes
    """
    suggestions = []
    for index, couleur in lst_index_couleurs:
        if est_ligne:
            position = {"ligne": num, "colonne": index}
        else:
            position = {"ligne": index, "colonne": num}
        suggestions.append(construireSuggestion(position, couleur))
    return suggestions

def getLigneImage(image: PlayerImage, li: int) -> list:
    """
    Retourne la ligne li de l'image du joueur.
    :param image: image du joueur
    :param li: indice de la ligne
    :return: la ligne li de l'image
    """
    return image[li]

def getLigneInverseImage(image: PlayerImage, li: int) -> list:
    """
    Retourne la ligne li inversée de l'image du joueur.
    :param image: image du joueur
    :param li: indice de la ligne
    :return: la ligne li inversée
    """
    return list(reversed(image[li]))

def getLstBlocsInverse(blocs: LstBlocs) -> LstBlocs:
    """
    Retourne la liste des blocs inversée.
    :param blocs: liste des blocs
    :return: liste des blocs inversée
    """
    return list(reversed(blocs))

def getColonneImage(image: PlayerImage, co: int) -> list:
    """
    Retourne la colonne co de l'image du joueur.
    :param image: image du joueur
    :param co: indice de la colonne
    :return: la colonne co de l'image
    """
    colonne = []
    for ligne in image:
        colonne.append(ligne[co])
    return colonne

def getColonneInverseImage(image: PlayerImage, co: int):
    """
    Retourne la colonne co inversée de l'image du joueur.
    :param image: image du joueur
    :param co: indice de la colonne
    :return: la colonne co inversée
    """
    colonne = getColonneImage(image, co)
    return list(reversed(colonne))

def getIndexInverseDeIndexCouleurs(idx_color: LstIndexCouleurs,dim: int) -> LstIndexCouleurs:
    """
    Calcule les indices inversés d'une liste d'index et couleurs.
    :param idx_color: liste de couples (index, couleur)
    :param dim: dimension de l'image
    :return: nouvelle liste avec indices inversés
    """
    res = []
    for index, couleur in idx_color:
        res.append((dim - 1 - index, couleur))
    return res

def appliquerMonoGlueBord(image_joueur: PlayerImage,blocs_lignes: LstLstBlocs,blocs_colonnes: LstLstBlocs) -> LstSuggestions:
    """
    Applique la règle de mono-glue bord sur l'ensemble de l'image du joueur.
    :param image_joueur: image du joueur
    :param blocs_lignes: listes des blocs des lignes
    :param blocs_colonnes: listes des blocs des colonnes
    :return: liste de toutes les suggestions possibles
    """
    suggestions = []
    hauteur = len(image_joueur)
    largeur = len(image_joueur[0])
    for li1 in range(hauteur):
        rangee = getLigneImage(image_joueur, li1)
        idx_colors = appliquerMonoGlueBordRangee(rangee, blocs_lignes[li1])
        suggestions += indexCouleursToSuggestions(idx_colors, li1, True)
    for li2 in range(hauteur):
        rangee_inv = getLigneInverseImage(image_joueur, li2)
        idx_colors_inv = appliquerMonoGlueBordRangee(rangee_inv, blocs_lignes[li2])
        idx_colors = getIndexInverseDeIndexCouleurs(idx_colors_inv, largeur)
        suggestions += indexCouleursToSuggestions(idx_colors, li2, True)
    for co1 in range(largeur):
        rangee = getColonneImage(image_joueur, co1)
        idx_colors = appliquerMonoGlueBordRangee(rangee, blocs_colonnes[co1])
        suggestions += indexCouleursToSuggestions(idx_colors, co1, False)
    for co2 in range(largeur):
        rangee_inv = getColonneInverseImage(image_joueur, co2)
        idx_colors_inv = appliquerMonoGlueBordRangee(rangee_inv, blocs_colonnes[co2])
        idx_colors = getIndexInverseDeIndexCouleurs(idx_colors_inv, hauteur)
        suggestions += indexCouleursToSuggestions(idx_colors, co2, False)
    return suggestions

def appliquerBoucheTrouRangee(rangee: Rangee, blocs: LstBlocs) -> LstIndexCouleurs:
    """
    Applique la règle du bouche-trou sur une rangée.
    :param rangee: rangée de l'image du joueur
    :param blocs: liste des blocs de la rangée
    :return: liste des suggestions (index, couleur=0)
    """
    suggestions = []
    taille_rangee = len(rangee)
    if blocs:
        longueur_blocs = 0
        for bloc in blocs:
            longueur_blocs += bloc[NOMBRE]
        longueur_blocs += len(blocs) - 1
        if longueur_blocs < taille_rangee:
            debut = 0
            fin = longueur_blocs
            for i in range(taille_rangee):
                if i >= fin and rangee[i] is None:
                    suggestions.append((i, 0))
    return suggestions

def appliquerBoucheTrou(image_joueur: PlayerImage,blocs_lignes: LstLstBlocs,blocs_colonnes: LstLstBlocs) -> LstSuggestions:
    """
    Applique la règle du bouche-trou sur l'ensemble de l'image du joueur.
    :param image_joueur: image du joueur
    :param blocs_lignes: listes des blocs des lignes
    :param blocs_colonnes: listes des blocs des colonnes
    :return: liste des suggestions possibles
    """
    suggestions = []
    hauteur = len(image_joueur)
    largeur = len(image_joueur[0])
    for li in range(hauteur):
        rangee = getLigneImage(image_joueur, li)
        idx_colors = appliquerBoucheTrouRangee(rangee, blocs_lignes[li])
        suggestions += indexCouleursToSuggestions(idx_colors, li, True)
    for co in range(largeur):
        rangee = getColonneImage(image_joueur, co)
        idx_colors = appliquerBoucheTrouRangee(rangee, blocs_colonnes[co])
        suggestions += indexCouleursToSuggestions(idx_colors, co, False)
    return suggestions
