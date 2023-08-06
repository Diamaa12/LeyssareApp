//Mise en forme
let cfa = document.getElementById('cfa');
let fgn = document.getElementById('fgn');
let depense = document.getElementById('depense');
let date = document.getElementById('date');

cfa.style.backgroundColor = '#08a2c1';
fgn.style.backgroundColor = '#ab08c1';
depense.style.backgroundColor = '#e6750b';
date.style.backgroundColor = '';

let montant_cfa = document.getElementById('montant_cfa');
let montant_fg = document.getElementById('montant_fg');
let montant_depense = document.getElementById('montant_depense');

montant_cfa.style.backgroundColor = 'rgba(8, 162, 193, 0.3)';
montant_fg.style.backgroundColor = 'rgba(171, 8, 193, 0.3)';
montant_depense.style.backgroundColor = 'rgba(230, 110, 10, 0.3)';

function string_designer(identifiant) {
    let split_contenu = identifiant.innerHTML.split(',');
    let tab_contenu = parseInt(split_contenu[0]);
    let contenu_id_spliter = tab_contenu.toLocaleString('fr-FR');
    identifiant.innerHTML = contenu_id_spliter;
    return identifiant.innerHTML;
}

//appel de fonction...
string_designer(montant_fg);
string_designer(montant_cfa);
string_designer(montant_depense);


if( montant_fg.length === montant_cfa.length)
{
    let elements_length = montant_fg.length;
    for (let i = 0; i < elements_length; i++) {
  //On change la couleur du text, et son poid
  montant_fg[i].style.backgroundColor = 'green';
  montant_cfa[i].style.backgroundColor = 'red';
  montant_depense[i].backgroundColor = 'orange';
  elements[i].style.fontWeight = 'bold';
  //On recupère la somme en String
  let number_cfa = montant_cfa[i].innerHTML;
  let number_fg = montant_fg[i].innerHTML;
  let number_depense = montant_depense[i].innerHTML;
  //On enléve l'effet float sur la somme exp:1000,0 on enleve le ,0 à la fin
  // La méthode split() permet en meme temps de transformer le string spliter en Array()
  let nmb_cfa = number_cfa.split(',')
  let nmb_fg = number_fg.split(',')
  let nmb_depense = number_depense.split(',')
  //On recupére ici l'array numero [0] qui correspond au 1000 on oublie l'array numero [1] qui correspond au ,0 car on en a pas besoin
  //On transforme en INT
  a = parseInt(nmb_cfa[0]);
  b = parseInt(nmb_fg[0]);
  c = parseInt(nmb_depense[0]);
  //Avec la methode toLocaleString, qui permet de trsformer une sommes dans la locale region
  let somme_valide_cfa = a.toLocaleString('fr-FR');
  let somme_valide_fg = b.toLocaleString('fr-FR');
  let somme_valide_depense = c.toLocaleString('fr-FR');
  // En fin, on remplace le String de départ par le nombre validé
  montant_cfa[i].innerHTML = somme_valide_cfa;
  montant_fg[i].innerHTML = somme_valide_fg;
  montant_depense[i].innerHTML = somme_valide_depense;
  if (i == 2){montant_depense[i].style.color = 'orange';}

}


}

