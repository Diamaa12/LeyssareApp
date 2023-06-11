// Sélectionnez l'élément du DOM dans lequel vous souhaitez afficher le message
/*const messageElement = document.getElementById('cgu');

// Définissez le message que vous souhaitez afficher
const message = messageElement.innerHTML;

// Fonction pour afficher le message pendant une durée déterminée
function afficherMessageTemporaire(message, tempsAffichage) {
  // Afficher le message
  messageElement.textContent = message;
  messageElement.style.display = 'block';

  // Masquer le message après la durée spécifiée
  setTimeout(function () {
    messageElement.style.display = 'none';
  }, tempsAffichage);
}

// Appeler la fonction pour afficher le message pendant 5 secondes (par exemple)
afficherMessageTemporaire(message, 5000); // 5000 millisecondes = 5 secondes*/

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('cgu-container').style.display = 'block';

  document.getElementById('close-cgu').addEventListener('click', function() {
    document.getElementById('cgu-container').style.display = 'none';
  });
});