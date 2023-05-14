
var para5 = document.getElementsByClassName('para5');
var par = para5[0]
par.style.color = 'green';
let h1 = document.getElementsByClassName("h1");
let h = h1[0];
h.style.color = "orange";
h.innerHTML = 'Welcome to Your Admin Site.'

// Récupération des données JSON

const element = document.getElementsByClassName('selected_user');
let options = document.getElementById('valeur');

fetch('http://127.0.0.1:8000/static/JSONS/leyssaremembres.json')
    .then(response => response.json())
    .then(data => {
        // Utilisez le contenu du fichier JSON ici

        for(let i = 0; i<element.length; i++){
            element[i].addEventListener('click', function(){
                for(let d in data){
                     let prenom = data[d].prenom;
                     let pays = data[d].pays;
                     if(element[i].innerHTML == prenom){
                        let valeur = pays;
                        options.innerHTML = valeur;
                        console.log(prenom+' viens de '+pays);
                     }
            }
        });
            console.log('debut de chargement de function.');

        }
    })
    .catch(error => {
        console.error('Erreur de chargement du fichier JSON:', error);
    });
