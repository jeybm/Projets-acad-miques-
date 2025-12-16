import random
""" 1. Calculer le cout de la fonction somme :
def somme(n):
    somme = 0
    for i in range(n):
        somme += i
    return somme """
#On a 1 affectation somme = 0
# Au niveau de la boucle for on a  1 addition sur i , 1 affection sur i , 1 comparaison (test si i < n)
#Dans la boucle il y 1 opperation (somme +i) et 1 affection somme = (somme +i)
#Donc le cout est égale à = 1+ 3n+ 2n = 5n + 1

""" 2. Reprendre l’exercice 3.1 du TD2 pour l’affichage de la premiere figure,
une solution pourrait etre : """
# def figure(n):
#     for i in range(n+1): # 2 addition , 1 affection et 1 comparaison
#         for j in range(i): #  1 addition , 1 affection et 1 comparaison
#             print("*", end="") # 1 affichage
#         print() # 1 affichage 
# # cout = 1 + 3n+n * (3n+n)= 1 + 16n^2

""" 3 Ordre de grandeur asymptomatique et complexite d’un algorithme
Quand n est relativement grand, c’est difficile de calculer precisement le
cout. Nous allons plutot estimer un ordre de grandeur O.

    On dit qu’une fonction f est :
    — bornee ou constante si f = O(1)
    — logarithmique si f = O(log n)
    — lineaire si f = O(n)
    — quadratique si f = O(n^2)
    — exponentielle s’il existe une constante c > 0 telle que f = O(c^n)

Lorsque f = O(g) on dit que g est un ordre de grandeur de f.
Quel est l’ordre de grandeur de la fonction somme ? Et de la fonction
figure ? """
# Dans la fonction somme i prend les valeurs 0 a n-1 dans la boucle for l'ordre de grandeur est O(n)
#Dans la fonction figure : 

# Vous devez donc écrire :
# — la fonction coord hasard qui renvoie un couple de coordonnées valide
# (par rapport à la zone qui lui est passée en paramètre)
def coord_hasard(zone) :
    #Création de 4 variables coordonnées de départ jusqu'à la fin
    x_min,y_min = zone[0] 
    x_max,y_max = zone[len(zone)-1]
    
    x = random.randint(x_min, x_max)
    y = random.randrange(y_min, y_max)
    return x,y


zone = [[0, 0], [10 - 1, 12 - 1]]
print(coord_hasard(zone))
# — la fonction chercher qui renvoie la direction à suivre pour accéder au
# trésor.
# Son code consiste à regarder où se trouve la case du trésor par rapport
# à la position courante du robot (ces deux informations sont passées
# en paramètres à la fonction). Elle renvoie une chaîne ”H” (haut), ”B”
# (bas), ”G” (gauche), ”D” (droite), ”HG” (haut gauche), ”HD” (haut
# droit), ”BG” (bas gauche), ”BD” (bas droite) en fonction de la position du trésor.
# La réduction de la zone de recherche doit exploiter le principe de la
# dichotomie vu en cours