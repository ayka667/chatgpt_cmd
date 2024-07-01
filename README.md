# ___***Chat GPT on the cmd Windows***__

# **Fonctionnalités du script**

***1.*** **Chargement de la clé API :**

- Le script commence par charger la clé API à partir d'un fichier config.json. Cette clé est utilisée pour authentifier les requêtes à l'API OpenAI.
  Création du dossier de l'historique :

***2.*** **Création du dossier de l'historique :**

- Une fonction est définie pour vérifier et créer un dossier appelé historique s'il n'existe pas déjà. Ce dossier est destiné à stocker les fichiers journaux des conversations.

***3.*** **Gestion des fichiers journaux :**

- Une fonction détermine le nom du fichier journal en fonction de la date actuelle (dd mm yyyy) et assure que chaque nouvelle session de conversation est enregistrée dans un fichier distinct.

***4.*** **Conversation avec l'IA :**

- Le cœur du script est une boucle où l'utilisateur entre des messages qu'il veut envoyer à l'IA. L'utilisateur peut taper des messages comme s'il conversait avec une personne réelle.

- Pour chaque message de l'utilisateur :
 -Le script ajoute ce message à l'historique de la conversation.
 -Il envoie l'historique complet à l'API OpenAI pour obtenir une réponse.
 -Il enregistre la réponse de l'IA dans l'historique de la conversation.
 -Il affiche la réponse de l'IA dans la console.
 -Il enregistre chaque échange (message de l'utilisateur et réponse de l'IA) dans le fichier journal correspondant.
  
***5.*** **Fin de la conversation :**

- L'utilisateur peut taper "exit" pour terminer la conversation. À ce moment, le script affiche un message de fin et se termine.


# Installations

You must put your open ai key in the config.json

```
{
    "openai_api_key": "Your open ai key"
}
```
