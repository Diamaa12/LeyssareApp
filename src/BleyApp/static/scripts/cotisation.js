
let id = document.getElementById('idt');
let nom = document.getElementById('nom');
let prenom = document.getElementById('prenom');

id.style.backgroundColor = '#47846a';
nom.style.backgroundColor = 'rgb(84, 98, 4)';
prenom.style.backgroundColor  = '#0d90e7';
console.log(prenom.innerHTML);


//mise en forme des identifiants
let ids = document.getElementsByClassName('ids');
let noms = document.getElementsByClassName('noms')
let prenoms = document.getElementsByClassName('prenoms')
for( let i = 0; i < ids.length; i++){
ids[i].style.backgroundColor = 'rgba(71, 132, 106, 0.3)';
}
//Mise en forme des noms et prenoms
// Assurez-vous que les deux tableaux ont la même longueur
if (noms.length === prenoms.length) {
  let longueur = noms.length;

  for (let i = 0; i < longueur; i++) {
    let elementNom = noms[i];
    let elementPrenom = prenoms[i];
    elementNom.style.backgroundColor = 'rgba(84, 98, 4, 0.3)';
    elementPrenom.style.backgroundColor = 'rgba(13, 144, 231, 0.3)';
    // Faites ce que vous souhaitez avec les éléments des deux tableaux ici
    console.log(elementNom, elementPrenom);
  }
} else {
  console.log("Les deux tableaux n'ont pas la même longueur.");
}

//On recupere les classes monnaie

let elements = document.getElementsByClassName('monnaie');
for (let i = 0; i < elements.length; i++) {
  //On change la couleur du text, et son poid
  elements[i].style.color = 'green';
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
let ele_fgn = document.getElementById('fgn').style.backgroundColor = '#08a2c1';
let fgn = document.getElementsByClassName('fgn');
for (let i = 0; i < fgn.length; i++) {
  //On change la couleur du text, et son poid
  fgn[i].style.color = 'white';
  fgn[i].style.backgroundColor = 'rgba(8, 162, 193, 0.3)';
  fgn[i].style.fontWeight = 'bold';
  //On recupère la somme en String
  let number = fgn[i].innerHTML;
  //On enléve l'effet float sur la somme exp:1000,0 on enleve le ,0 à la fin
  // La méthode split() permet en meme temps de transformer le string spliter en Array()
  let nmb = number.split(',')
  //On recupére ici l'array numero [0] qui correspond au 1000 on oublie l'array numero [1] qui correspond au ,0 car on en a pas besoin
  //On transforme en INT
  n = parseInt(nmb[0]);
  //Avec la methode toLocaleString, qui permet de trsformer une sommes dans la locale region
  let somme_valide = n.toLocaleString('fr-FR');
  if (isNaN(n)) {
  console.log("La valeur de x est NaN.");
} else {
  // En fin, on remplace le String de départ par le nombre validé
  fgn[i].innerHTML = somme_valide
  console.log("La valeur de x n'est pas NaN.");
}
  console.log(typeof n, somme_valide);

}
let ele_cfa = document.getElementById('cfa').style.backgroundColor = '#ab08c1';
let cfa = document.getElementsByClassName('cfa');
for (let i = 0; i < cfa.length; i++){
  cfa[i].style.backgroundColor = 'rgba(172, 8, 190, 0.3)';
  cfa[i].style.fontWeight = 'bold';
  //On recupère la somme en String
  let number = cfa[i].innerHTML;
  //On enléve l'effet float sur la somme exp:1000,0 on enleve le ,0 à la fin
  // La méthode split() permet en meme temps de transformer le string spliter en Array()
  let nmb = number.split(',')
  //On recupére ici l'array numero [0] qui correspond au 1000 on oublie l'array numero [1] qui correspond au ,0 car on en a pas besoin
  //On transforme en INT
  n = parseInt(nmb[0]);
  //Avec la methode toLocaleString, qui permet de trsformer une sommes dans la locale region
  let somme_valide = n.toLocaleString('fr-FR');
  if (isNaN(n)) {
  console.log("La valeur de x est NaN.");
  } else {
  // En fin, on remplace le String de départ par le nombre validé
  cfa[i].innerHTML = somme_valide
  console.log("La valeur de x n'est pas NaN.");
}
  console.log(typeof n, somme_valide);
}
//Coloration de Colonne Pays
let ele_pays = document.getElementById('pays');
ele_pays.style.backgroundColor = '#c15308';
console.log(ele_pays.innerHTML)

let pays = document.getElementsByClassName('pays_value');
for(let i = 0; i<pays.length; i++){
pays[i].style.backgroundColor = 'rgba(204, 135, 30, 0.3)';
console.log(pays[i].innerHTML)
}