let id = document.getElementById('id');
let id_number = document.getElementById('id_number');
let nom = document.getElementById('nom');
let prenom = document.getElementById('prenom');
let pays = document.getElementById('pays');

id.style.backgroundColor = '#c5430f';
id_number.style.backgroundColor = '#6b2f46';
nom.style.backgroundColor = '#082c42';
prenom.style.backgroundColor = '#1c81d4';
pays.style.backgroundColor = ''

let ids = document.getElementsByClassName('ids');
let id_numbers = document.getElementsByClassName('id_numbers');
let noms = document.getElementsByClassName('noms');
let prenoms = document.getElementsByClassName('prenoms');
let contry = document.getElementsByClassName('contry');

if(ids.length === prenoms.length){
    let elements_length = ids.length;
    console.log('les element sont egaux et son ' + elements_length);
    for (let i = 0; i < elements_length; i++){
        ids[i].style.backgroundColor = 'rgba(197, 67, 15, 0.3)';
        id_numbers[i].style.backgroundColor = 'rgba(107, 47, 70, 0.3)';
        noms[i].style.backgroundColor = 'rgba(8, 44, 66, 0.3)';
        prenoms[i].style.backgroundColor = 'rgba(28, 129, 212, 0.3)';
        contry[i].style.backgroundColor = 'rgba()';

    }
}

