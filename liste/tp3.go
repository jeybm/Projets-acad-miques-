package liste

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
)

/*
	Exercice 1 : Pile

1. Créer une structure Pile basée sur une liste chaînée.
*/
type Pile struct {
	sommet *liste
}

/*2. Implémenter les différentes opérations d’une Pile.*/
//méthode empiler
func (p *Pile) Empiler(elt int) {
	// création d'une nouvelle cellule
	newcellule := &cellule{valeur: elt}
	// on crée une variable qui contiendra l'ancien sommet
	actuel := p.sommet.head
	// Tester si la Pile est vide
	if actuel == nil {
		p.sommet.head = newcellule
		newcellule.suivant = nil
	} else { // La liste n'étant pas vide on fait :
		// le nouveau sommet est newcellule
		p.sommet.head = newcellule
		// On pointe le nouveau sommet vers l'ancien sommet
		newcellule.suivant = actuel // Mise à jour du liens vers l'avant
	}
}

// méthode Depiler
func (p *Pile) Depiler() (int, error) {
	/// on crée 2 curseurs qui contiendront la cellule actuelle, un pour stoquer l'autre pour parcourir la pile
	eltdepile := p.sommet.head
	// On test si la Pile est vide
	if p.sommet.head == nil {
		return -1, errors.New("pile est vide")
	} else {
		p.sommet.head = p.sommet.head.suivant
		return eltdepile.valeur, nil
	}
}

// Fonction créer Pile
func creerPile() Pile {
	pile := Pile{sommet: nil}
	return pile
}

// méthode EstVide
func (p *Pile) EstVide() bool {
	if p.sommet.head == nil {
		return true
	}
	return false
}

// méthode somment
func (p *Pile) Sommet() (int, error) {
	// Vérification de Pile vide
	if p.sommet.head != nil {
		return p.sommet.head.valeur, nil
	} else { // Gestion du cas vide
		return -1, errors.New("Pile Vide")
	}

}

// fonction fromslice

func fromslice(s []int) Pile {
	pile := creerPile()
	for _, elt := range s {
		pile.Empiler(elt)
	}
	return pile
}

// fonction toSlice
func toSlice(p Pile) []int {
	// Création d'une slice vide
	slice := []int{}
	// On parcours la pile
	for !p.EstVide() {
		elt, _ := p.Depiler()
		slice = append(slice, elt)
	}
	return slice
}

/*3. Tester les différentes méthodes implémentées. */

func main() {
	etagere := creerPile() // variable réceptrice de type pile
	rep := true            // On crée une booléenne servant à contenir les limites de la boucle
	for rep {
		fmt.Printf("Veuillez ajouter un nombre")
		// Méthode utilisant NewScanner pour receuillir des informations
		scanner := bufio.NewScanner(os.Stdin)
		scanner.Scan()
		elt, err := strconv.Atoi(scanner.Text()) // Convertisseur du text en entier
		// Gestion d'erreur si elt different d'un entier
		for err != nil {
			fmt.Printf("ERREUR ! Veuillez ajouter un nombre : ")
			scanner := bufio.NewScanner(os.Stdin)
			scanner.Scan()
			elt, err = strconv.Atoi(scanner.Text())
		}
		etagere.Empiler(elt)
		fmt.Printf("Voulez vous ajouter un autre élement")
		scanner.Scan()
		reponse := scanner.Text()
		if reponse == "oui" {
		} else if reponse == "non" {
			rep = false
		}
	}

}

/*
	Exercice 2 : File

1. Créer une structure File basée sur une liste chaînée.
2. Implémenter les différentes opérations d’une File.
3. Tester les différentes méthodes implémentées
*/
type File struct {
	head *liste
	tail *liste
}

// méthode Enfiler
func (f *File) Enfiler(x int) {
	// La liste étant non vide on commence à enfiler
	// On crée une nouvelle cellule
	newCellule := &cellule{valeur: x}
	// cas ou la liste est vide
	// On test si la liste est vide
	if f.head == nil {
		f.head.head.valeur = newCellule.valeur
		f.tail.head.valeur = newCellule.valeur
		f.head.head.suivant = nil
		f.tail.head.suivant = nil
		return
	} else {
		//Cas ou la liste est non vide
		ancien := f.tail.head // variable receptrice de l'ancienne tête
		ancien.suivant = newCellule
		f.tail.head = newCellule
		newCellule.suivant = nil
	}
}
