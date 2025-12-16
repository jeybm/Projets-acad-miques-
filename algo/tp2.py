"""1 Conversion
1. Ecrire un programme qui demande `a l’utilisateur un nombre entier de
secondes. Le programme doit ensuite donner le nombre correspondant
de jours, heures, minutes et secondes. Par exemple, si l’utilisateur
saisit 654321, on affichera quelque chose du type :
Cela donne 7 jours 13 heures 45 minutes 21 secondes"""
#je crée des sous programme qui vont me permettre de convertir mes secondes 
#en minutes,heures,jours
def reste(x,d) :
    seconde = x % d
    return seconde
def minutes(x) :
    minute = x//60
    return minute 
def heures(m ) :
    heure = m//60
    return heure
def jours(x):
    jour = x//24
    return jour

# j'exécute mon script principal dans mon programme  exo1
def exo1():
    entier = int(input("Saisir un nombre entier de secondes :\n"))
    #je convertis les secondes en jours
    jour = jours(heures(minutes(entier)))
    #je récupère le reste des secondes
    res_heure = reste(entier,60*60*24) 
    #je convertis le reste de seconde en heure
    heure = heures(minutes(res_heure))
    #je récupère le reste des secondes
    res_minute = reste(res_heure,60*60)
    #je convertis le reste de seconde en minute
    minute = minutes(res_minute)
    #je récupère le reste de seconde
    seconde = reste(res_minute,60)
    print(f"cela donne {jour} jours, {heure} heures, {minute} minutes,{seconde} secondes \n ")




"""2 Boucles simples
1. Ecrire un programme qui affiche les nombres pairs de 10 `a 1 en utilisant
une boucle for"""

def exo2_1():
    for i in range(10,1,-1) :
        if i %2 == 0 :
            print(i)
    print("\n")
    

"""2. ´Ecrire un programme qui affiche les nombres impairs de 10 `a 1 en
utilisant une boucle while."""

def exo2_2():
    deb = 1
    max = 10
    while deb <= max :
        if deb %2 != 0 :
            print(deb)
        deb+=1
    print("\n")


"""3. Pour afficher les nombres entre n et m (n < m), que doit-on privil´egier
entre for et while ?"""

def exo2_3():
    print("\n Sachant que n>m la boucle for est plus avantageuse car elle incrémente automatique de 1 pas \n")


#Boucles imbriquees

def triangle(max):
    for i in range(1,max+1):
        etoile=""
        #j'ajoute les etoile succéssivement i fois
        for x in range(1,i+1):
            etoile +="*"
            # j'ajoute l'espace après chaque étoile en m'arrétant  avant l'impression de la dernière
            if x !=i+1:
                etoile +=" "
        # j'affiche la ligne que je viens de créer en sautant un ligne avant la prochaine
        print(etoile+"\n")

def triangle_inv(max):
    for i in range(max,0,-1):
        etoile =""
        #j'ajoute les etoile succéssivement i fois
        for x in range(i,0,-1):
            etoile += "*"
            # j'ajoute l'espace après chaque étoile en m'arrétant  avant l'impression de la dernière
            if x !=0 :
                etoile +=" "
        # j'affiche la ligne que je viens de créer en sautant un ligne avant la prochaine
        print(etoile+"\n")

def triangle_droit(max):
   # j'ajoute les espaces présent à gaude de la figure
    for x in range(max,0,-1):
        espace = " "*(2*(max-x))
        etoile =""
        # j'ajoute les étoile à droite des espace créé 
        for i in range(x,0,-1):
            etoile += "*"
            # j'ajoute l'espace après chaque étoile en m'arrétant  avant l'impression de la dernière
            if i !=0 :
                etoile +=" "
        # j'affiche la ligne que je viens de créer en sautant un ligne avant la prochaine
        print(espace+etoile+"\n")
    print("\n")

def z_invers(max):
    # j'ajoute les espaces présent à gaude de la figure
    for i in range(max,0,-1):
        espace =" "*(2*(max-i))
        etoile=""
        if i == max or i ==1:
            # j'ajoute max etoile au début et à la fin de ma figure
            for x in range(max,0,-1):
                etoile +="*"
                if x!=0:
                    etoile +=" "
            print(etoile+"\n")
        #j'ajoute une étoile à droite de l'espace créé jusqu'a i==2
        else :
            etoile ="*"
            print(espace+etoile+"\n")

def exo3_1() :
    triangle(5)
    "\n"
    triangle_inv(5)
    "\n"
    triangle_droit(5)
    "\n"
    z_invers(5)

def exo3_2():
    max = int(input("entrer une heuteur :"))
    triangle(max)
    "\n"
    triangle_inv(max)
    "\n"
    triangle_droit(max)
    "\n"
    z_invers(max)

def main():
    print("j'exécute l'exercice 1 :\n")
    exo1()
    print("fin de l'exercice 1.\n")
    print("j'exécute l'exercice 2 :\n")
    exo2_1()
    exo2_2()
    exo2_3()
    print("fin de l'exercice 2.\n")
    print("j'exécute l'exercice 3 :\n")
    exo3_1()
    exo3_2()
    print("fin de l'exercice 3.\n")


main()