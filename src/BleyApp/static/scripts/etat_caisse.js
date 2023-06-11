let elements = document.getElementsByClassName('montant');
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
  if (i == 2){elements[i].style.color = 'orange';}

}
