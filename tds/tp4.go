package main

import (
	"fmt"
	"strconv"
)

/*
	Exercice 1 :

Créer une fonction récursive qui calcule le nieme terme de la suite de Fibonacci.
Pour rappel, la suite de Fibonacci est définie de la manière suivante :
F (n) =		0 					si n = 0,

	1 					si n = 1,
	F (n −1) + F (n −2) si n > 1
*/
/* func F(n int) int {
	if n == 0 {
		return 0
	} else if n == 1 {
		return 1
	} else {
		return F(n-1) + F(n-2)
	}
} */

// Exercice 2 :
// Créer une fonction récursive qui calcule a^n

/* func puissance(a, n int) int {
	// Mon cas de bas cest n = 0 et n = 1
	if n == 0 {
		return 1
	} else if n == 1 {
		return a
	} else {
		return a * puissance(a, n-1)
	}
}

*/

/* Exercice 3 :
Créer une fonction récursive qui recherche un entier dans un tableau donné */

/* func recherche(t []int, elt int) bool {
	// Cas ou l'élément cherché est en tête de liste
	if t[0] == elt {
		return true
	} else if len(t) == 0 {
		return false
	} else {
		return recherche(t[1:], elt)
	}
} */

/* Exercice 4 :
Créer une fonction récursive qui détermine si deux tableaux sont équivalents (s’ils contiennent les mêmes élé-
ments, dans le même ordre). */

/* func egaux(t1 []int, t2 []int) bool {
	// 1. VÉRIFICATION PRÉLIMINAIRE (Échec - Longueur)
	// On vérifie la longueur dès le début. Si elles sont différentes, les tranches sont inégales.
	// Cette vérification ne doit se faire qu'une seule fois au premier appel (ici, c'est fait à chaque appel, mais c'est fonctionnel).
	if len(t1) != len(t2) {
		return false
	}

	// 2. CAS DE BASE (Succès/Terminaison)
	// Si la première tranche est vide (et l'autre aussi, grâce au test 1), on a tout vérifié.
	if len(t1) == 0 {
		return true
	}

	// 3. CAS DE BASE (Échec - Différence d'élément)
	// On compare l'élément courant (l'élément à l'indice 0 de la tranche restante).
	if t1[0] != t2[0] {
		return false
	}

	// 4. CAS RÉCURSIF (Progression)
	// On appelle la fonction récursivement sur la queue (tous les éléments sauf le premier) des deux tranches.
	return egaux(t1[1:], t2[1:])
} */

/* Exercice 5 :
Créer une fonction récursive qui fusionne deux tableaux triés */

/* func fusion(t1 []int, t2 []int) []int {
	switch {
	//cas liste vide
	case len(t1) == 0:
		return t2
	case len(t2) == 0:
		return t1
	case t1[0] <= t2[0]:
		return append(t1[0:1], fusion(t1[1:], t2)...)
	default:
		return append(t2[0:1], fusion(t2[1:], t1)...)
	}
} */

/*
	Exercice 6 :

Créer une fonction récursive pour convertir un nombre décimal en binaire.
Remarque : Pour convertir un entier en string, on utilisera strconv.Itoa()
*/
/* func deciBinaire(elt int) string {
	switch {
	case elt%2 == 0 && elt/2 >= 2:
		return deciBinaire(elt/2) + strconv.Itoa(0)
	case elt%2 == 1 && elt/2 >= 2:
		return deciBinaire(elt/2) + strconv.Itoa(1)
	}
	if elt%2 == 0 && elt/2 < 2 {
		return strconv.Itoa(0) + strconv.Itoa(1)
	} else {
		return strconv.Itoa(1) + strconv.Itoa(1)
	}

} */
func deciBinaire(elt int) string {
	if elt <= 1 {
		return strconv.Itoa(elt) // Cas de base : "0" ou "1"
	}
	// Cas récursif
	return deciBinaire(elt/2) + strconv.Itoa(elt%2)
}

func main() {
	fmt.Print(deciBinaire(247))
}
