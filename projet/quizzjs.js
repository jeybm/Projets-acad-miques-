const lesQuestions = [
    {
        "id": 1,
        "question": "Quel terme Claude Shannon a-t-il popularisé en 1948 ?",
        "contexte": "Unité fondamentale de l'information.",
        "possibilites": ["Le Pixel", "Le Bit", "Le Watt"]
    },
    {
        "id": 2,
        "question": "Quel lien a-t-il établi dans sa thèse ?",
        "contexte": "Lien entre mathématiques et électricité.",
        "possibilites": ["Algèbre de Boole et circuits", "Relativité et temps", "Chimie et atomes"]
    },
    {
        "id": 3,
        "question": "Quelle était sa passion aux Bell Labs ?",
        "contexte": "Il circulait bizarrement dans les couloirs.",
        "possibilites": ["Le monocycle en jonglant", "Le chant lyrique", "La cuisine"]
    }
];

const bonnesReponses = ["Le Bit", "Algèbre de Boole et circuits", "Le monocycle en jonglant"];


let tempsEcoule = 0;
window.setInterval(function() { 
    tempsEcoule++; 
}, 1000);


const monH1 = document.querySelector("#mod");
if (monH1) {
    monH1.innerHTML += " (" + lesQuestions.length + " questions)";
}


function integrerLesQuestions(questions) {
    let contenuGlobal = "";

    for (const q of questions) {
        let articleHTML = '<div class="col-12 col-md-6 col-lg-4 mb-4">';
        articleHTML +=   '<div class="custom-card h-100">';
        articleHTML +=     '<h3>Question ' + q.id + '</h3>';
        articleHTML +=     '<div class="p-3">';
        articleHTML +=       '<blockquote class="blockquote mb-3">' + q.contexte + '</blockquote>';
        articleHTML +=       '<p class="fw-bold">' + q.question + '</p>';
        
        let listeReponses = '<ul class="list-group list-group-flush">';
        
        if (q.possibilites) {
            for (let i = 0; i < q.possibilites.length; i++) {
                const choix = q.possibilites[i];
                const uniqueID = 'q' + q.id + '-opt' + i;
                const groupName = 'listGroupRadio' + q.id;

                listeReponses += '<li class="list-group-item" style="cursor:pointer;">';
                listeReponses +=   '<input class="form-check-input me-2" type="radio" name="' + groupName + '" id="' + uniqueID + '"> ';
                listeReponses +=   '<label class="form-check-label" style="cursor:pointer; width:80%;" for="' + uniqueID + '">' + choix + '</label>';
                listeReponses += '</li>';
            }
        }
        listeReponses += '</ul>';
        
        articleHTML += listeReponses;
        articleHTML +=     '</div>'; 
        articleHTML +=   '</div>';   
        articleHTML += '</div>';     

        contenuGlobal += articleHTML;
    }

    const section = document.querySelector("#zone-quiz");
    if (section) {
        section.innerHTML = contenuGlobal;
    }
}
integrerLesQuestions(lesQuestions);


 
const items = document.querySelectorAll("li");
for (const item of items) {
    item.addEventListener('click', function(event) {
        const inputRadio = item.querySelector('input');
        if(inputRadio) {
            inputRadio.checked = true;
        }
    });
}



const bouton = document.querySelector(".btn-success");

if (bouton) {
    bouton.addEventListener('click', function() {
        let score = 0;
        const itemsList = document.querySelectorAll("li");

        // ÉTAPE 1 : ON NETTOIE TOUT (RESET)
        // Avant de vérifier les réponses, on enlève toutes les couleurs d'avant
        for (const item of itemsList) {
            item.style.backgroundColor = ""; // On remet le fond à "rien" (transparent/blanc)
            item.style.color = "";           // On remet la couleur du texte par défaut
        }

        // ÉTAPE 2 : ON VÉRIFIE ET ON COLORIE
        for (const item of itemsList) {
            const texteReponse = item.textContent.trim();
            const inputRadio = item.querySelector('input');

            // Vérification si c'est une bonne réponse
            if (bonnesReponses.includes(texteReponse)) {
                // On met en vert pour montrer la solution (correction)
                item.style.backgroundColor = "lightgreen";
                item.style.color = "darkgreen"; // Pour que ce soit lisible
                
                // Si le bouton est coché par l'utilisateur, c'est un point gagné
                if (inputRadio && inputRadio.checked) {
                    score++;
                }
            } 
            // Si c'est faux MAIS que l'utilisateur l'a coché
            else if (inputRadio && inputRadio.checked) {
                item.style.backgroundColor = "lightcoral"; // On met en rouge l'erreur
                item.style.color = "darkred";
            }
        }

        alert("Vous avez trouvé " + score + " bonnes réponses en " + tempsEcoule + " secondes.");
    });
}