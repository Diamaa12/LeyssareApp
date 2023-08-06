
//Mise en forme
let cfa = document.getElementById('cfa');
let fgn = document.getElementById('fgn');
let depense = document.getElementById('depense');

cfa.style.backgroundColor = '#08a2c1';
fgn.style.backgroundColor = '#ab08c1';
depense.style.backgroundColor = '#e6750b';

let montant_cfa = document.getElementById('montant_cfa');
let montant_fg = document.getElementById('montant_fg');
let montant_depense = document.getElementById('montant_depense');

montant_cfa.style.backgroundColor = 'rgba(8, 162, 193, 0.3)';
montant_fg.style.backgroundColor = 'rgba(171, 8, 193, 0.3)';
montant_depense.style.backgroundColor = 'rgba(230, 110, 10, 0.3)';


let cfa_value = document.getElementById('cfa_value');
let fg_value = document.getElementById('fg_value');
cfa_value.style.backgroundColor = '#08a2c1';
fg_value.style.backgroundColor = '#ab08c1';

let class_cfa = document.getElementsByClassName('cfa');
let class_fgn = document.getElementsByClassName('fgn');
let class_date = document.getElementsByClassName('date');

function string_trimer(elements){
    for (let i = 0; i < elements.length; i++) {
          //On change la couleur du text, et son poid
          elements[i].style.color = 'white';
          elements[i].style.fontWeight = 'bold';
          //On recupère la somme en String
          let number = elements[i].innerHTML;
          //On enléve l'effet float sur la somme exp:1000,0 on enleve le ,0 à la fin
          // La méthode split() permet en meme temps de transformer le string spliter en Array()
          let nmb = number.split(',')
          //On recupére ici l'array numero [0] qui correspond au 1000 on oublie l'array numero [1] qui correspond au ,0 car on en a pas besoin
          //On transforme en INT
           n = parseInt(nmb[0]);
          //Avec la methode toLocaleString, qui permet de trsformer une sommes dans la locale region
          let somme_valide = n.toLocaleString('fr-FR');
              // En fin, on remplace le String de départ par le nombre validé
           if (isNaN(n)){

              console.log(elements[i].innerHTML," n'est pas un type valide! ");

             }
            else{
              elements[i].innerHTML = somme_valide;
             }
           //mise en forme des classes html
           if(elements[i].classList == 'cfa'){elements[i].style.backgroundColor = 'rgba(8, 162, 193, 0.3)'; }
           else if (elements[i].classList == 'fgn'){elements[i].style.backgroundColor = 'rgba(171, 8, 193, 0.3)';}
           else{console.log(elements[i].classList = 'date');}

        }

}

//Appel de fonction.
string_trimer(class_cfa);
string_trimer(class_fgn);


let ele_li = document.getElementsByClassName('inline-li');
for(let i=0; i<ele_li.length; i++){
    ele_li[i].style.color = 'red';
    ele_li[i].style.display = 'inline';
}
let items_tab = document.getElementsByClassName('fg-success');
for(let i=0; i<items_tab.length; i++){
    //suppression du .0
    let number = items_tab[i].innerHTML;
    let nmb = number.split(',')
    n = parseInt(nmb[0]);
    let somme_valide = n.toLocaleString('fr-FR');
    items_tab[i].innerHTML = somme_valide

    items_tab[i].style.color = 'white';
    if(i==2){items_tab[i].style.color = 'orange';}
    items_tab[i].style.display = '';
    items_tab[i].style.fontWeight = 'bold';
    items_tab[i].style.fontStyle = 'normal';
    items_tab[i].style.fontFamily = 'Sans-serif Arial';
    items_tab[i].style.fontSize = '1.3em';
}
//Remplissage de lignes dans la colone depense du fichier depence.html

/*
fetch('http://127.0.0.1:8000/static/JSONS/depenses.json')
    .then(response => response.json())
    .then(data => {
        // Utilisez le contenu du fichier JSON ici

        const valeurs = Object.values(data);
        console.log(valeurs)
        const numeros = valeurs.filter(element => typeof element === 'number');
        console.log(numeros)

        let element_depensee = document.getElementById('depensees');
        console.log(element_depensee.innerHTML)

        element_depensee.innerHTML = ''; // Clear the innerHTML before adding new values

        for (let i = 0; i < numeros.length; i++) {
          element_depensee.innerHTML = numeros[i] + ' ';
        }
        console.log(element_depensee.innerHTML)
    })
    .catch(error => {
        console.error('Erreur de chargement du fichier JSON:', error);
    });
*/



