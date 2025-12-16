package main

/*Exercice 1 :
Un Etudiant est défini par son nom, son prénom, son numéro étudiant et sa moyenne.

4. Écrire une fonction qui prend en entrée deux Etudiant et qui renvoie le numéro de celui qui a la meilleure
moyenne.
5. Écrire une fonction permettant de saisir plusieurs Etudiant (demander ce nb à l’utilisateur) et de les stocker
dans une slice.
6. Écrire une fonction qui recherche un Etudiant dans une slice en fonction de son numéro et qui renvoie son
nom et prénom (ou un message d’erreur s’il n’existe pas dans la liste).
7. Écrire une fonction qui prend une slice d’Etudiant et une note seuil et renvoie les numéros des Etudiant
ayant une moyenne supérieure ou égale à ce seuil.*/

// 1. Créer une structure Etudiant.
/* type etudiant struct {
	nom, prenom, idEtu string
	moyenne            float64
}
*/
// 2. Écrire une méthode qui permet d’afficher correctement les informations d’un Etudiant.
/*
func (e etudiant) infoEtu() string {
	return fmt.Sprintf("l'étudiant %s %s d'id : %s à une moyenne de %.2f", e.nom, e.prenom, e.idEtu, e.moyenne)
}
*/
/* func exo1() {
	etudiants := []etudiant{
		{
			nom:     "boudinemervillon",
			prenom:  "jey",
			idEtu:   "22411194",
			moyenne: 14.36,
		},
	}
	fmt.Println(etudiants[0].infoEtu())
}
*/
// 3. Écrire une fonction permettant de saisir un nouvel Etudiant.

/* func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Quel est le nom de l'étudiant ?")
	scanner.Scan()
	nomEtu := scanner.Text()

	fmt.Println("Quel est sont prénom ?")
	scanner.Scan()
	prenomEtu := scanner.Text()

	fmt.Println("Quel sont numéro d'étudiant")
	scanner.Scan()
	idEtud := scanner.Text()

	fmt.Println("Quelle est sa moyenne ?")
	scanner.Scan()
	mean, _ := strconv.ParseFloat(scanner.Text(), 64)

	etudiants := []etudiant{
		{nom: nomEtu,
			prenom:  prenomEtu,
			idEtu:   idEtud,
			moyenne: mean},
	}
	fmt.Println(etudiants[0].infoEtu())

} */

// func modify(arr *[3]int) {
// 	arr[0] = 100
// }
// func main() {
// 	array := [3]int{1, 2, 3}
// 	modify(&array)
// 	fmt.Println(array)
// }
