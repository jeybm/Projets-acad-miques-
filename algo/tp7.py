
cle_chiffrement= {"A":"Z",
                      "B":"Y",
                      "C":"X",
                      "D":"W",
                      "E":"V",
                      "F":"U",
                      "G":"T",
                      "H":"S",
                      "I":"R",
                      "J":"Q",
                      "K":"P",
                      "L":"O",
                      "M":"N",
                      "N":"M",
                      "O":"L",
                      "P":"K",
                      "Q":"J",
                      "R":"I",
                      "S":"H",
                      "T":"G",
                      "U":"F",
                      "V":"E",
                      "W":"D",
                      "X":"C",
                      "Y":"B",
                      "Z":"A"}
def  chiffrer(mot_a_chiffrer , cle_chiffrement):
    """ Renvoie  la  version  chiffrée de  mot_a_chiffrer  en
        utilisant  le  dictionnaire  cle_chiffrement """
    mot_chiffre =""
    for lettres in mot_a_chiffrer :
        mot_chiffre += cle_chiffrement[lettres.upper()]
    return mot_chiffre
    # code de la  fonction  chiffrer

"""Algotithme (mot_a_chiffrer Chaine de caractère  , cle_chiffrement dictionnaire)
    Debut :
        variable cle_chiff string ="" 
        Pour x dans mot_a_chiffrer Faire
            mot_chiffre += cle_chiffrement[x.Maj]
        Fin Pour
        retourner mot_chiffre 
    FIN
    """

def  dechiffrer (mot_a_dechiffrer , cle_chiffrement):
    """ Renvoie  la  version déchiffrée de  mot_a_dechiffrer  en
        utilisant  le  dictionnaire  cle_chiffrement """
    mot_dechiffre =""
    for lettres in mot_a_dechiffrer :
        l_Maj = lettres.upper()
        mot_dechiffre += cle_chiffrement.keys(l_Maj)
    return mot_dechiffre
    # code de la  fonction  déchiffrer
""" Algorithme (mot_a_dechiffrer , cle_chiffrement)
    Debut :
        variable mot_dechiffre string =""
        Pour lettres dans mot_a_dechiffrer FAIRE :
            mot_dechiffre += cle_chiffrement.keys(letrres.MAJ)
        FIN POUR
        retourner mot_dechiffre


 """

if  __name__ =="__main__":
    




  # demander à l’utilisateur  un mot à chiffrer
    # chiffrer  ce mot
    mot_a_chiffrer = input("Entrer un mot a chiffrer")
    print(chiffrer(mot_a_chiffrer,cle_chiffrement))
    # demander à l’utilisateur  un mot à déchiffrer
    # déchiffrer  ce mot
    mot_a_dechiffrer = input("Entrer un mot a dechiffrer")
    print(chiffrer(mot_a_dechiffrer,cle_chiffrement))




""" Le chiffre de César (clé = 1 lettre)
La  clé  du  chiffrement  de  César  peut  se  résumer  à  une  lettre,  par  exemple  C.  Le  dictionnaire  est
ensuite créé en décalant l’alphabet pour le faire commencer à la lettre clé.
Exemple de clé de chiffrement de César à partir de la lettre C :
2 """
# Travail demandé
# • Écrivez  une  fonction  rotate  qui,  à  partir  d’un  mot  et  d’un  nombre  de  positions,  renvoie  une
# version de ce mot, décalée du nombre de positions indiqué.
# Par exemple, rotate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2) renvoie CDEFGHIJKLMNOPQRSTUVWXYZAB.
#  Utilisez les tranches.
""" Algorithme rotate (mot,nombre_position)--> dictionnaire
    Début :
        variable chiff_de_César string=""
        For x in range(len(mot)) Faire :
            if x < nombre position ALORS :
                Variable temps string =""
                temps += mot[x].MAJ
            else Alors :
                chiff_de_César += mot[x].MAJ
            FIN de si
        Fin du POUR
        chiff_de_César += temps
        retourner chiff_de_César
    FIN
     """
def rotate(mot,nombre_position):
    chiff_de_Cesar ="" #création d'une variable qui renvoie  une version de ce mot, décalée du nombre de positions indiqué
    temps="" #création d'un variable temporaire  qui encapsule les lettres avant le décalage
    for x in range(len(mot)): 
        if x < nombre_position :
            temps += mot[x].upper()
        else :
            chiff_de_Cesar += mot[x].upper()
    chiff_de_Cesar +=temps
    return chiff_de_Cesar
        


# • Écrivez une fonction creer_dico qui, à partir d’une lettre, renvoie le dictionnaire de chiffrement.
# Vous pouvez notamment utiliser la fonction rotate que vous venez d’écrire.
def creer_dico(lettre):
    alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_de_Cesar=""
    for l in range(len(alphabet)) : # recherche de la position de la lettre
        if alphabet[l] == lettre.upper():
            alphabet_de_Cesar = rotate(alphabet,l)
            break
    chiff_de_Cesar ={}
    #Maintenant on assembre le dictionnaire
    for x in range(len(alphabet)) :
        chiff_de_Cesar[alphabet[x]]= alphabet_de_Cesar[x]
    return chiff_de_Cesar





# • Modifiez votre code pour demander une lettre à l’utilisateur et créer le dictionnaire de
# chiffrement à partir de cette lettre

""" if  __name__ =="__main__":
    lettre = input("entrer une lettre : ")
    print(creer_dico(lettre)) """