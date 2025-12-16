package liste

// Exercice 3 : Liste simplement chaînée

// type cellue
type cellule struct {
	valeur  int
	suivant *cellule
}

// type liste

type liste struct {
	head *cellule
}

// méthode Search

func (l *liste) Search(elt int) bool {
	// test liste vide : si la tête de liste est vide toute la liste l'est
	if l.head == nil {
		return false
	}
	// Création d'une variable curseur
	actuel := l.head
	// On parcours la liste en cherchant l'élément
	for actuel != nil && actuel.valeur != elt {
		// j'avance le curseur
		actuel = actuel.suivant
	}
	// cas 1: élement n'a pas été trouvé
	if actuel == nil {
		return false
	}
	// cas 2 =  élément trouvé
	return true

}

// méthode Remove

func (l *liste) Remove(elt int) {
	// test de la liste vide
	if l.head == nil {
		return
	}

	// elt est la tête
	if l.head.valeur == elt {
		l.head = l.head.suivant
		return
	}
	// Création de 2 curseurs qui parcour la liste
	actuel := l.head.suivant
	precedent := l.head
	// Parcours de la liste
	for actuel != nil && actuel.valeur != elt {
		precedent = actuel
		actuel = actuel.suivant
	}
	// elt n'est pas la tête
	if actuel != nil {
		// On pointe la cellule suivante du précédant sur la cellule suivante de actuel
		precedent.suivant = actuel.suivant
		return
	}

}

// Exercice 4 : Liste doublement chaînée
type cellule2 struct {
	valeur    int
	suivant   *cellule2
	précédant *cellule2
}

type listeDouble struct {
	head *cellule2
	tail *cellule2
}

// méthode cons
func (ld *listeDouble) Cons(x int) {
	// Création de la nouvelle cellule
	newcellule := &cellule2{valeur: x, suivant: ld.head, précédant: nil}
	//Si la liste n'était pas vide, mettre à jour le champ 'précédant' de l'ancienne tête
	if ld.head != nil {
		ld.head.précédant = newcellule // Mise à jour du lien arrière
	}
	// Attribution de la postion de tête à la nouvelle cellule
	ld.head = newcellule
}

// méthode Append
func (ld *listeDouble) Append(x int) {
	// Création de la nouvelle cellule
	newcellule := &cellule2{valeur: x, suivant: nil, précédant: ld.tail}
	// Si la liste n'est pas vide
	if ld.head != nil {
		ld.tail.suivant = newcellule // Mise à jour du lien avant
	}
	// Attribution de la position de Queu à la nouvelle cellule
	ld.tail = newcellule
}

// méthode Remove
// func (ld *liste2) Remove2(elt int) {
// 	// Test liste vide
// 	if ld.head == nil && ld.tail == nil {
// 		return
// 	}
// 	// si elt est en tête
// 	if ld.head.valeur == elt {
// 		if ld.head.suivant != nil {
// 			// La liste avait au moins deux éléments
// 			ld.head.suivant.précédant = nil
// 			ld.head = ld.head.suivant
// 		} else {
// 			// La liste avait un seul élément (ld.head = ld.tail = elt)
// 			ld.head = nil
// 			ld.tail = nil
// 		}
// 		return
// 	}

// 	// si elt est en queu de liste
// 	if ld.tail.valeur == elt {
// 		if ld.tail.précédant != nil {
// 			// la liste contient au moins 2 éléments
// 			ld.tail.précédant.suivant = nil // Mise à jours du lien avant
// 			ld.tail = ld.tail.précédant     // Attribution de la position de queu à la cellule précédente
// 		} else {
// 			ld.head = nil
// 			ld.tail = nil
// 		}
// 		return
// 	}
// 	//Si elt n'est ni la tête ni le queu
// 	// On crée 2 curseur pour naviguer dans la liste
// 	actuel := ld.head.suivant
// 	precedent := ld.head
// 	for actuel != nil && actuel.valeur != elt {
// 		// on sort de la liste si elt à été trouvé ou n'a pas été trouvé
// 		precedent = actuel
// 		actuel = actuel.suivant
// 	}
// 	// Cas elt à été trouvé
// 	if actuel != nil {
// 		precedent.suivant = actuel.suivant   // Mise à jour du lien avant
// 		actuel.suivant.précédant = precedent // Mise à jour du lien arrière
// 		return
// 	} else {
// 		return
// 	}
// }
// méthode Print

//méthode remove

func (l *listeDouble) Reemove(x int) {
	// Test liste vide
	if l.head == nil {
		return
	}
	// Cas 1: l'élement recherché est en tête
	if l.head.valeur == x {
		l.head.suivant.précédant = nil
		l.head = l.head.suivant
		return
	}
	// cas 2
	if l.tail.valeur == x {
		l.tail.précédant.suivant = nil
		l.tail = l.head.précédant
		return
	}

	// Parcourir la liste si x n'est pas tete ni queu
	// créé 2 curusur : 1 suivant , un precendent
	actuel := l.head.suivant
	precedent := l.head
	for actuel != nil && actuel.valeur != x {
		precedent = actuel
		actuel = actuel.suivant
	}
	// cas x trouvé
	if actuel != nil {
		precedent.suivant = actuel.suivant // mise a jours du lien avant
		actuel.suivant.précédant = precedent
		return

	} else {
		return
	}

}

func main() {
	cellule1 := cellule2{valeur: 10}
	cellule3 := cellule2{valeur: 20}
	cellule4 := cellule2{valeur: 10}

	cellule1.précédant = nil
	cellule1.suivant = &cellule3
	cellule3.précédant = &cellule1
	cellule3.suivant = &cellule4
	cellule4.précédant = &cellule3
	cellule4.suivant = nil

}
