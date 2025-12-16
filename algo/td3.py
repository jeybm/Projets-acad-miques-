# Algo-Prog TD3

# 1) Fonctions simples sur les listes

# 1.

def create_liste ():
    liste = [] #on crée une liste vide résecptacle
    stop = True 
    while stop : # boucle qui continue tant que stop est true
        
        liste.append(int(input("entrer une valeur : \n"))) # ajoute l'élément entré
        rep = input("Voulez vous continuez ? s (pour stopper)/ c(pour continuer) :\n")
        if rep == "s": # Controle la sorti de la boucle
            stop = False
    return liste
#2.
def take(n,liste_entier):
    liste =[]
    for x in range(n):
        liste.append(liste_entier[x]) # ajoute les n premier entier a liste
    return liste
#3.
def drop(n,liste_entier):
    liste =[]
    for x in range(n,len(liste_entier)): # commence à compter à partir de l'indice des nombre à récupérer
        liste.append(liste_entier[x])
    return liste

#4.
def somme(liste):
    somme =0
    for x in range(len(liste)):
        somme += liste[x] # additionne les éléments de la liste à chaque itération 
    return somme

#5.
def pairs_impairs(liste_entier):
    # On commence à créer 2 liste réceptrice
    l_pairs =[]
    l_impairs=[]
    for x in range(len(liste_entier)):
        if liste_entier[x]%2 ==0 : # cas ou le nombre est pair
            l_pairs.append(liste_entier[x])
        else: #cas ou il est impair
            l_impairs.append(liste_entier[x])
    return l_pairs,l_impairs

#6.
def split_at(n,liste):
    # On commence à créer 2 liste réceptrice
    part1 =[]
    part2=[]
    for x in range(len(liste)):
        if x < n : # ajout des n premier entier dans une liste
            part1.append(liste[x])
        else : # ajout du reste dans l'autre
            part2.append(liste[x])
    return part1,part2

#7
def to_str(liste) :
    # Création d'une variable de type string réceptrice
    string =""
    for i in range(len(liste)):
        string += str(liste[i]) # On converti chaque élément de la liste en chaine de caractère puis on ajoute à chaque ittération dans "string"
        if i < len(liste)-1:
            string+="," #après chaque élément on ajoute une virgule. On s'arrête à l'avant dernière variable 
    return string

# Création d'une fonction main dans laquelle chaque exercice est exécuté

# def main (): # fonction dans laquelle toute les exercice vont être exécuter
#     liste = [10, 29, 56, 75]
#     liste_premier = take(2,liste)
#     liste_dernier = drop(2,liste)
#     pair , impair = pairs_impairs(liste)
#     part1,part2 = split_at(2,liste)
#     string = to_str(liste)
#     print(f"liste : {liste},n premier éléments : {liste_premier}, n dernier éléments : {liste_dernier},\n liste pair :{pair},liste impair :{impair},\n partie 1 : {part1},partie 2 : {part2},\n chaine de liste : {string}")

# main()
if __name__ == '__main__':
    # Testez si la fonction take prend correctement les n premiers éléments
    assert take(5, list(range(1, 11))) == [1, 2, 3, 4, 5]
    
    # Testez si la fonction drop retire correctement les n premiers éléments
    assert drop(5, list(range(1, 11))) == [6, 7, 8, 9, 10]
    
    # Testez la somme (cas de la liste vide et d'une liste simple)
    assert somme([]) == 0
    assert somme([1, 2, 3]) == 6
    
    # Testez la séparation des pairs et impairs
    assert pairs_impairs(list(range(1, 5))) == ([2, 4], [1, 3])
    
    # Testez la division de la séquence (cas normal et cas de division à l'index 0)
    assert split_at(3, list(range(1, 5))) == ([1, 2, 3], [4])
    assert split_at(0, list(range(1, 5))) == ([], [1, 2, 3, 4])
    
    # Testez la conversion en chaîne de caractères
    assert to_str([1,2,3]) == "1,2,3"


# 2 Compteur de mots

def words_count(x):
    nombre =0
    for i in range(len(x)):
        if x[i] == " ":
            nombre +=1
    # Ajout du dernier mot 
    nombre +=1
    return nombre

# fonction qui compte en comptant les virgules
def count_words(x):
    nombre =0
    for i in range(len(x)):
        if x[i] ==","  :
            nombre +=1
        elif x[i] == " ":
            nombre +=1
        
    # Ajout du dernier mot 
    nombre +=1
    return nombre



def main2() :
    sentence = input("Écrivez une phrase: ")
    count1 = words_count(sentence)
    count2 = count_words(sentence)
    print(f"sans ponctuation {count1}, avec ponctuation {count2}")
    


main2()


    

