
const elements = document.getElementsByClassName('montant');
let options = document.getElementById('valeur');

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
      if (isNaN(n)){

            console.log(elements[i].innerHTML," n'est pas un type valide! ")

        }
      else{
        elements[i].innerHTML = somme_valide
        }

}
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

    items_tab[i].style.color = 'green';
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



