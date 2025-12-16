"""traduire l'algorithme suivant :
Début
Afficher("entrer un entier :")
Lire(nbre)
div = 1
cpteur = 0
TQ div < nbre FAIRE
Si nbre modulo div == 0 Alors
cpteur = cpteur + 1
Fin Si
div = div + 1
FTQ
Afficher(cpteur)
fin


def main():
    nbre = int(input("Entrer un entier : "))
    div = 1
    cpteur =0
    while div < nbre :
        if nbre % div == 0 :
            cpteur += 1
        div += 1
    return cpteur

rep = main()
print(rep)

"""


"""On désire réaliser un programme qui permet de simuler le fonctionnement d'une calculatrice.
L'utilisateur saisit en entrée au clavier 2 nombres entiers et choisit un nombre compris entre 1 et 4
pour l'opération :  • 1 pour l'addition
                    • 2 pour la soustraction
                    • 3 pour la multiplication
                    • 4 pour la division

Algorithme:
Début:
Afficher("Entrer un premier nombre entier : ")
Lire(nb1)
Afficher("Entrer un second nombre entier : ")
Lire(nb2)

resultat = 0

Afficher("Entrer un chiffre entre 1 et 4")
Pour x entre 1 et 4 Faire :
    Si x == 1 Alors:
        resultat = nb1 + nb2
    Sinon x== 2 Alors :
        resultat = nb1 - nb2
    Sinon x== 3 Alors :
        resultat = nb1 * nb2
    Sinon :
        Si nb2 not 0 Alors :
            resultat = nb1 / nb2
        Fin de si
    Fin de si
Fin de Pour 

Afficher(resultat)
    
"""



""" def calcul() :
    nb1 = int(input("Entrer un premier entier : "))
    nb2 = int(input("Entrer un second entier : "))
    resultat = 0

    opper = 0
    if opper < 1 or opper > 4:
        opper = int(input("Saisir une opération (1 = +, 2 = -, 3 = * et 4 = /) : "))

    erreur = False
    match opper:
        case 1:
            resultat = nb1 + nb2
        case 2:
            resultat = nb1 - nb2
        case 3:
            resultat = nb1 * nb2
        case _:
            if nb2 != 0:
                resultat = nb1 / nb2
            else:
                erreur = True
    return resultat , erreur

def main() :
    encore = True
    if encore :
        res , err = calcul()
        if not err:
            print(f"le résultat de l'opération est {res}")
        else:
            print("La division par 0 est impossible :")
        rep = input("voulez vous continuer ? Saisir : O pour oui et N pour non : ")
        if rep != "O" or  "N" :
            encore = False

exec = main()
print(exec)  """

""" On part d'un entier n auquel on fait subir une transformation :
• si n est pair, on le divise par deux ;
• si n est impair, on le multiplie par 3, et ajoute 1.
• Puis, on recommence sur le résultat jusqu'à obtenir 1.
Par exemple, en partant de n = 10, on obtient : 10 5 16 8 4 2 1

1. Écrire un programme qui permet de d'afficher cette transformation pour un entier saisi au
clavier ; calculer en même temps sa durée de vol, c'est-à-dire le nombre d'entiers rencontrés
avant de trouver 1 (dans l'exemple, cette durée serait donc 6).

Algorithme
Début
    Afficher("Saisir un nombre entier : ")
    Lire(nbr)

    vol = 0
    Tant que nbr n'est pas égale à 1 Faire :
        Afficher(nbr)
        Si nbr % 2 == 0  Alors :
            nbr = nbr / 2
        Sinon Alors :
            nbr = nbr*3 + 1
        Fin de si
        vol = vol + 1
    Fin de tant que 
    Afficher("On a rencontré {vol} entier avant de trouver 1 ")
    
"""

def duree_vol(nbr):

    vol =0
    entier_conjecture = nbr

    while entier_conjecture != 1 :
        print(entier_conjecture)
        if entier_conjecture % 2 == 0:
            entier_conjecture = entier_conjecture//2
        else :
            entier_conjecture = entier_conjecture*3 + 1 
        vol +=1
    print(entier_conjecture)
    print(f"durée de vol pour {nbr} est {vol}")
    return vol 




"""Généraliser ce programme pour tester tous les entiers dans un intervalle d’entiers. Dans cet
intervalle, repérer l’entier qui a la plus grande durée de vol."""

def main( ):
    borne_min = int(input("Saisir une borne minimum :"))
    borne_max = int(input("Saisir une born_maximum :"))

    duree_volmax = 0
    for x in range(borne_min,borne_max+1) :
        duree_vol1 = duree_vol(x)
        if duree_vol1 >= duree_volmax :
            num_vol = x
            duree_volmax = duree_vol1
    print(f"\n le vol {num_vol} est le plus long et dure {duree_volmax}")

print(main())
