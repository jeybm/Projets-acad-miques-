package main

import "fmt"

type cellule struct {
	valeur  int
	suivant *cellule
}

type liste struct {
	head *cellule
}

func (l *liste) Search(elt int) bool {
	// test liste vide :
	if l.head == nil {
		return false
	}
	// liste pas vide donc recherche de elt dans la liste
	for l.head != nil {
		if l.head.valeur == elt {
			return true
		}
		l.head = l.head.suivant
	}

	// elt n'a pas été trouvé

	return false
}

func (l *liste) Remove(elt int) {
	// test liste vide
	if l.head == nil {
		return
	}

	// cas 1 : elt est en tête
	if l.head.valeur == elt {
		l.head = l.head.suivant
		return
	}
	// cas 2 : parcours de la liste
	precedent := l.head
	actuel := l.head.suivant

	for actuel != nil {
		if actuel.valeur == elt {
			// ici le pointeur suivant de la variable précédent sauté le noeux actuel
			// et pointer vers le noeux qui suit actuel
			precedent.suivant = actuel.suivant
			return
		}
		// si pas trouvé on avance
		precedent = actuel
		actuel = actuel.suivant

	}

}

type cellules struct {
	valeur    int
	précédent *cellules
	suivant   *cellules
}
type listeDouble struct {
	head *cellules
	tail *cellules
}

func (ld *listeDouble) Removes(elt int) {
	// test liste vide
	if ld.head == nil {
		return
	}
	actuel := ld.head
	// parcours de la liste à la recherche de elt
	for actuel != nil && actuel.valeur != elt {
		actuel = actuel.suivant
	}
	// cas 1 :  l'élément n'est pas trouvé dans la boucle  on sort
	if actuel == nil {
		return
	}

	p := actuel.précédent
	s := actuel.suivant
	// actuel est la valeur à supprimé
	// Mise à jours du chainage avant
	if p != nil {
		// actuel  n'est pas la tête
		p.suivant = s
	} else {
		// actuel est la tête
		ld.head = s
	}

	// Mise à jour du chainage arrière
	if s != nil {
		// actuel n'est pas la queu
		s.précédent = p
	} else {
		// actuel est la queu
		ld.tail = p
	}

}

func (ld *listeDouble) PrintForward() {
	//test liste vide
	if ld.head == nil {
		return
	}
	// parcour de la liste
	actuel := ld.head
	for actuel != nil {
		fmt.Println(actuel.valeur)
		actuel = actuel.suivant
	}
}
func (ld *listeDouble) PrintBackward() {
	//test liste vide
	if ld.head == nil {
		return
	}
	// parcours de la liste à l'envers
	actuel := ld.tail
	for actuel != nil {
		fmt.Println(actuel.valeur)
		actuel = actuel.précédent
	}

}

func (ld *listeDouble) InsertSorted(elt int) {
	//creation d'une nouvelle cellule
	newCell := &cellules{valeur: elt}
	// Cas liste vide
	if ld.head == nil {
		ld.head = newCell
		ld.tail = newCell
		return
	}
	// Cas parcourir liste jusqu'a trouvé un nombre plus petit que elt :
	actuel := ld.head

	for actuel != nil && actuel.valeur < elt {

		actuel = actuel.suivant

		// je passe à la cellule suivante
	}

	// on est sorti de la boucle :
	// cas 1 : actuel est nil et elt est plus grand que chacune des valeurs des cellules.
	if actuel == nil {
		ld.tail.suivant = newCell
		newCell.précédent = ld.tail
		newCell.suivant = nil
		ld.tail = newCell
		return
	}

	// si elt est plus petit que la cellule
	if actuel.valeur > elt {
		// cas ou elt est plus petit que la tête
		if actuel.précédent == nil {
			ld.head.précédent = newCell
			newCell.précédent = nil
			newCell.suivant = actuel
			ld.head = newCell
			return
		} else {
			// cas ou elt n'est pas la tête
			actuel.précédent.suivant = newCell   //elt plus petit que la cellule actuelle donc on va a la cellule qui précède actuel puis on va remplacer son suivant (qui est la cellule actuel) par newcell
			newCell.précédent = actuel.précédent // newcell ayant prit la place de actuel on lui associe son précédent
			newCell.suivant = actuel             // de surcroit la cellule suivant de newcell devient notre cellule actuel
			actuel = newCell                     // pour finir la cellule actuel devient newcelle
			return
		}
	}

}

func Merge(l1, l2 *listeDouble) *listeDouble {
	// Création de la nouvelle structure de liste résultante (vide)
	result := &listeDouble{}

	// Curseur pour l1 et l2
	c1 := l1.head
	c2 := l2.head

	// Pointeur vers la dernière cellule ajoutée au résultat.
	var tailResult *cellules

	if c1 == nil {
		// Si l1 est vide, le résultat est l2
		return l2
	}
	if c2 == nil {
		// Si l2 est vide, le résultat est l1
		return l1
	}

	// Déterminer la première cellule de la liste fusionnée (la nouvelle Head)
	if c1.valeur < c2.valeur {
		result.head = c1
		c1 = c1.suivant // Avancer le curseur de l1
	} else {
		// Inclut le cas où les valeurs sont égales
		result.head = c2
		c2 = c2.suivant // Avancer le curseur de l2
	}

	// Initialisation des pointeurs de la nouvelle tête
	result.head.précédent = nil // La tête n'a pas de prédécesseur
	tailResult = result.head    // Le curseur de queue commence à la tête

	// 2. Boucle de Fusion Principale
	for c1 != nil && c2 != nil {
		var temp *cellules // Nœud temporaire, l'élément sélectionné

		if c1.valeur < c2.valeur {
			temp = c1
			c1 = c1.suivant
		} else {
			// Inclut le cas a1.valeur >= a2.valeur
			temp = c2
			c2 = c2.suivant
		}

		// L'ancienne queue (tailResult) pointe en avant vers le nœud sélectionné (temp)
		tailResult.suivant = temp
		// Le nœud sélectionné (temp) pointe en arrière vers l'ancienne queue
		temp.précédent = tailResult

		// Avancer le curseur de queue
		tailResult = temp
	}

	// Déterminer quel reste de liste est le premier élément restant
	var reste *cellules
	if c1 != nil {
		reste = c1 // Reste de l1
		// Le tail du résultat sera le tail de l1
		result.tail = l1.tail
	} else if c2 != nil {
		reste = c2 // Reste de l2
		// Le tail du résultat sera le tail de l2
		result.tail = l2.tail
	} else {
		// Si les deux listes ont terminé exactement en même temps
		result.tail = tailResult
		return result
	}

	// Attacher les restes à la liste fusionnée (dernière liaison bidirectionnelle)
	tailResult.suivant = reste
	reste.précédent = tailResult
	// (Le champ 'suivant' de l'ancienne queue de la liste restante est déjà nil
	// puisqu'elle était la queue de sa liste d'origine, et notre result.tail est déjà pointé correctement)

	return result
}
func main() {
	// liste := &liste{
	// 	head: &cellule{
	// 		valeur: 10,
	// 		suivant: &cellule{
	// 			valeur: 34,
	// 			suivant: &cellule{
	// 				valeur: 43,
	// 			},
	// 		},
	// 	},
	// }
	// Création correcte d'une liste doublement chaînée avec 3 éléments
	node1 := &cellules{valeur: 1}
	node2 := &cellules{valeur: 3}
	node3 := &cellules{valeur: 5}

	node1.suivant = node2
	node2.précédent = node1
	node2.suivant = node3
	node3.précédent = node2

	// liste1 := &listeDouble{
	// 	head: node1,
	// 	tail: node3,
	// }
	node4 := &cellules{valeur: 2}
	node5 := &cellules{valeur: 4}
	node6 := &cellules{valeur: 6}

	node4.suivant = node5
	node5.précédent = node4
	node5.suivant = node6
	node6.précédent = node5
	liste2 := &listeDouble{
		head: node4,
		tail: node6,
	}

	liste2.Reverse()
	liste2.PrintForward()

}

// Exercice 6 : Réversibilité d’une liste doublement chaînée

func (ls *listeDouble) Reverse() {
	//Vérification de liste vide
	if ls.head == nil {
		return
	}
	// lecture de la liste
	actuel := ls.head
	var stockage *cellules // cellule de stockage
	var prev *cellules     // pour stocker le précédent (nouvelle tête)
	for actuel != nil {
		// je stock mon pointeur suivant original dans stockage
		stockage = actuel.suivant
		// j'inverse le pointeur suivant et précédent
		actuel.suivant = actuel.précédent
		actuel.précédent = stockage
		// Je stock ma tete original dans prev
		prev = actuel
		// j'avance à la cellule suivante
		actuel = stockage

	}
	// Après inversion, l'ancienne tête devient la queue et l'ancienne queue devient la tête
	ls.tail, ls.head = ls.head, ls.tail
	ls.head = prev

}
