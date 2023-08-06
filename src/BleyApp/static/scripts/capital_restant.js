//Mise en forme
let cfa = document.getElementById('cfa');
let fgn = document.getElementById('fgn');
cfa.style.backgroundColor = '#08a2c1';
fgn.style.backgroundColor = '#ab08c1';

let cfa_value = document.getElementById('somme_cfa');
let fg_value = document.getElementById('somme_fg');
cfa_value.style.backgroundColor = 'rgba(8, 162, 193, 0.3)';
fg_value.style.backgroundColor = 'rgba(171, 8, 193, 0.3)';


//On recupere les classes monnaie

let elements = document.getElementsByClassName('somme');
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
  console.log(typeof n, somme_valide);
  // En fin, on remplace le String de départ par le nombre validé
  elements[i].innerHTML = somme_valide

}