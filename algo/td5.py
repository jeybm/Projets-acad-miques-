# 1.1 Recherche d’un élément dans une liste triée 
# 1.  Écrire une fonction qui prend en paramètre une liste triée et un élément. Si cet 
# élément est dans la liste, alors cette fonction retourne l’indice de la première 
# occurrence de cet élément dans la liste. Sinon, cette fonction retourne -1. 

def rechercher(l,elt):
    for i in range(len(l)):
        if l[i] == elt :
            return i
    return -1

# 2.  Écrire un programme principal pour tester les fonctions précédentes avec les 
# exemples suivants : 
# ●  liste = [1,2,3,4,5,5,5], élément = 5 
# ●  liste = [1,2,3,4,5,6], élément = 0 
# ●  liste = [1,2,3,4,5,6], élément = 10 
# ●  liste = [x for x in range(1, 100)], élément = 5 

if __name__ == '__main__' :
    assert rechercher([1,2,3,4,5,5,5],5) == 4
    assert rechercher([1,2,3,4,5,6],0) ==-1
    assert rechercher([1,2,3,4,5,6],10) == -1
    assert rechercher([ x for x in range(1,100)],5) == 4
 
# Quel est le nombre d’opérations effectuées pour chaque exemple ? Que 
# constatez-vous ? 
"""L'algorithme de recherche effectue N comparaisons (il parcourt toute la liste).
Dans le meilleur des cas (si l'élément est au début), le nombre d'opérations est très faible.
 Pour le cas général où l'élément est trouvé à l'index i,le nombre d'opérations est i+1.
 Conclusion pour la recherche ,le nombre d'opérations dépend fortement de la position de l'élément recherché. 
 Si la liste devient très grande (N augmente),le nombre d'opérations peut rester faible, 
ou devenir très grand. 
 """
# 3.  Selon la constatation précédente, proposez un algorithme plus optimisé 
# qui permet d’effectuer un minimum d’opérations possibles.
def recherche_dicho(liste,elt):
    debut = 0
    fin = len(liste) - 1
    # Variable pour stocker le meilleur indice trouvé jusqu'à présent (initialement -1)
    resultat = -1 
    
    while debut <= fin:
        milieu = (debut + fin) // 2
        
        # Cas 1: L'élément est trouvé
        if liste[milieu] == elt:
            # Nous stockons l'indice trouvé (c'est le meilleur résultat actuel)
            resultat = milieu 
            # MAIS nous cherchons maintenant OBLIGATOIREMENT dans la partie gauche 
            # (en ignorant le milieu actuel) pour trouver une occurrence encore PLUS à gauche.
            fin = milieu - 1 
            
        # Cas 2: L'élément cherché est à droite du milieu
        elif liste[milieu] < elt:
            debut = milieu + 1
            
        # Cas 3: L'élément cherché est à gauche du milieu
        else: # liste[milieu] > elt
            fin = milieu - 1
            
    # Si l'élément a été trouvé au moins une fois, 'resultat' contient l'indice le plus à gauche.
    # Sinon, il retourne -1.
    return resultat 

def main() :
    e1 =recherche_dicho([1,2,3,4,5,5,5],5)
    print(e1)
    e2=recherche_dicho([1,2,3,4,5,6],0)
    print(e2)
    e3=recherche_dicho([1,2,3,4,5,6],10)
    print(e3)
    e4=recherche_dicho([ x for x in range(1,100)],5)
    print(e4)


#  Tri 
# 1.  Implémenter l’algorithme du tri par sélection, puis le tester avec des jeux d’essais 
# (voir cours P21). 

def tri_select(l):
    for i in range (len(l)-1):
        # Création d'un variable de suivi du l'indice min actuel
        min_actu = i
        for y in range(i+1,len(l)):
            # Cas ou le min actuel est plus grand que le min trouvé
            if l[min_actu]>l[y]:
                min_actu = y
        if min_actu != i :
            #Création d'un variable de stockage de la valeur a l'indice i
            temp = l[i]
            #Échange des place entre min actuel et de celui trouvé
            l[i]= l[min_actu]
            l[min_actu] = temp
        
# 2.  Implémenter l’algorithme du tri par permutation (tri à bulle), puis le tester avec des 
# jeux d’essai (voir cours P    22). 

def tri_bulle(l):
    # Création d'une variable de vérification
    not_trie = True
    #tant que celle_ci n'est pas vérifier la boucle continue
    while  not_trie :
        # j'initialise un compteur de changement de place cptr
        cptr =0
        # On parcours la liste
        for i in range(len(l)-1):
            # Cas ou ma valeur suivante est plus petit que la précédente
            if l[i]>l[i+1]:
                #variable de stockage temporaire
                temp = l[i]
                l[i]=l[i+1]
                l[i+1] = temp
                cptr+=1
            i+=1
        # Cas ou il n'y a plus de changement donc la liste est triée
        if cptr == 0 :
            not_trie = False
    
            
# 3.  Implémenter l’algorithme du tri par permutation optimisé (tri à bulle), puis le tester 
# avec des jeux d’essai (voir cours P23). 

def tri_select_opti(l):
    dernier_elt =len(l)-1
    while  dernier_elt >0 :
        # On parcours la liste
        for i in range(0,dernier_elt) :
            # Cas ou ma valeur suivante est plus petit que la précédente
            if l[i]>l[i+1]:
                #variable de stockage temporaire
                temp = l[i]
                l[i]=l[i+1]
                l[i+1] = temp
        # Le dernier élément étant à sa place définitive on décrémente dernier_elt de 1
        dernier_elt -=1

