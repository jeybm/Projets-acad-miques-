# 1.1 Recherche dans une liste non triée 
"""     1.  Écrire une fonction qui prend en paramètre une liste quelconque et un élément. Si 
    cet élément est dans la liste, alors cette fonction retourne l’indice (supérieur ou égal 
    à 0) de la première occurrence de cet élément dans la liste. Sinon, cette fonction 
    retourne -1 """
def research(liste,elt):
    for x in range(len(liste)):
        if liste[x] == elt :
            return x
    return -1

""" 2.  Écrire une fonction qui prend en paramètre une liste quelconque et un élément. Si 
cet élément est dans la liste, alors cette fonction retourne une liste contenant les 
indices (supérieurs ou égaux à 0) de toutes ses occurrences dans la liste. Sinon, 
cette fonction retourne une liste vide. """
def research1(liste,elt):
    liste1 =[]
    for x in range(len(liste)):
        if liste[x] == elt :
            liste1.append(x)
    return liste1

""" 3.  Écrire un programme principal pour tester les fonctions précédentes avec les 
exemples suivants : 
●  liste = [3,2,5,1,7,5], élément = 5 
●  liste = [3,2,5,1,7,6], élément = 10 
●  liste = [3,2,5,1,7,6], élément = 6 
●  liste = [3,4,2,5,2,5,4,3,5,3,5,3,5,3,6,2,5], élément = 5 
 
Quel est le nombre d’opérations effectuées pour chaque exemple ? Que 
concluez-vous ? """

if __name__ =='__main__':
    assert research([3,2,5,1,7,5],5) == 2
    assert research([3,2,5,1,7,6],10) == -1
    assert research([3,2,5,1,7,6],6) == 5
    assert research([3,4,2,5,2,5,4,3,5,3,5,3,5,3,6,2,5],5) == 3

    assert research1([3,2,5,1,7,5],5) == [2,5]
    assert research1([3,2,5,1,7,6],10) == []
    assert research1([3,2,5,1,7,6],6) == [5]
    assert research1([3,4,2,5,2,5,4,3,5,3,5,3,5,3,6,2,5],5) == [3,5,8,10,12,16]

   
""" 2 Tuple  """

""" 1.  On peut représenter un rectangle en deux dimensions par deux points : son coin 
inférieur gauche (cig) et son coin supérieur droit (csd). Écrivez une fonction qui 
calcule l’aire d’un rectangle.  """

def air_triangle (x,y):
    cig,csd = (x,y)
    air = (cig*csd,)
    return air

""" 2.  Écrivez la fonction min_max(tuple) qui renvoie les valeurs minimale et maximale de 
tuple. """
def min_max(tuple):
    # Création de deux variable min ,max initialiser à la première valeur du tuple
    min_courant = tuple[0] 
    max_courant = tuple[0]
    # On parcours le tuple
    for x in tuple :
        #pour chaque valeur parcouru on la compare  au min et max courant 
        if min > x :
            min = x
        elif max < x :
            max = x
    return min , max 

""" 3.  Écrivez la fonction enumere(liste) qui produit le même résultat que enumerate() : elle 
retourne une liste de tuples (indice, valeur). Vous ne pouvez évidemment pas utiliser 
enumerate(). """
def enumere (liste):
    #Création d'une liste vide
    ls_enum = []
    #On parcours la liste
    for i in range(len(liste)):
        #on ajoute le tuple (indice, élément) à chaque ittération dans la nouvelle liste
        ls_enum.append((i,liste[i]))
    return ls_enum

""" 4.  Un jeu de 52 cartes est constitué de quatre couleurs (Pique, carreau, Cœur et Trèfle) 
et pour chacune, il y a le 2, 3, 4, 5, 6, 7, 8, 9, 10, valet, dame, roi et as. Écrire une 
fonction qui retourne un jeu de cartes. Celui-ci sera une liste de tuples de la forme 
[(”Pique”, 2, ”Deux”), ......, (”Trèfle”, 14, ”As”)]. Pour cela, vous pouvez commencer `à 
constituer deux listes : 
●  La liste couleurs [”Pique”, ”carreau”, ”Cœur”, ”Trèfle”] 
●  La liste noms [”deux”, ”trois”, ”quatre”...”roi”, ”as”].  """

def cartes() :
    couleur = ["Pique", "carreau", "Cœur", "Trèfle"]
    nom =["deux","trois","quatre","cinq","six","sept","huit","neuf","dix","valet","dame","roi","as"]
    cartes =[]
    for i in range(len(couleur)):
        for y in range(len(nom)):
            cartes.append((couleur[i],y+2,nom[y]))
    return cartes


