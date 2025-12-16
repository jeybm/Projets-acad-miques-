def recherche_dicho(l,x):
    p_g = l[0:len(l)//2] #je sépare ma liste en 2 en n'integrant pas son milieux
    p_d =[(len(l)//2)+1, len(l)]
    # Je compare x à la moitier
    milieu = l[len(l)//2]
    while x != milieu: 
        if x < l[len(l)//2] :
            l=p_d
            milieu = l[len(l)//2]
        elif x > l


def tri_selection(liste):
    """
    Trie une liste en utilisant l'algorithme de tri par sélection.
    La liste est modifiée sur place.
    """
    n = len(liste) # Obtenir le nombre d'éléments dans la liste 

    # Parcourir tous les éléments de la liste sauf le dernier 
    # n-1 est l'indice maximal à atteindre.
    for i in range(n - 1):
        
        # Initialiser l'indice du minimum trouvé à l'indice courant (i) 
        min_idx = i

        # Trouver l'indice du minimum dans le reste de la sous-liste (de i+1 à la fin)
        for j in range(i + 1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j # Mettre à jour l'indice du plus petit élément

        # Échanger l'élément minimum trouvé avec l'élément à l'indice courant i
        # L'échange se fait si le plus petit élément n'était pas déjà à la position i
        if min_idx != i:
            # Affectation parallèle pour l'échange 
            liste[i], liste[min_idx] = liste[min_idx], liste[i]
            
    return liste