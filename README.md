# L’horloge de mamie
Une horloge interactive en ligne de commande développée en Python. Ce projet permet d'afficher l'heure en temps réel avec un style artistique ASCII, de gérer des alarmes et de basculer entre les formats d'affichage 24h et AM/PM.


 Fonctionnalités
Affichage ASCII Art : Utilise la bibliothèque pyfiglet pour un rendu visuel élégant dans le terminal.

Format Personnalisable : Basculez instantanément entre le format 24 heures et le format 12 heures (AM/PM).

Système d'Alarme : Programmez une alarme qui vous avertit visuellement lorsqu'elle se déclenche.

Gestion du Temps Réel : Possibilité de régler manuellement l'heure de l'horloge (avec calcul d'offset automatique).

Menu Interactif : Accédez à tout moment aux réglages via un raccourci clavier (Ctrl+C).

Mode Pause : Gelez l'affichage de l'heure pour une lecture fixe.


Installation
Prérequis :
Python 3.x installé sur votre système.

La bibliothèque pyfiglet


Utilisation
Au lancement, l'application vous guidera pour configurer l'affichage initial :

Choisir le format (1 pour AM/PM, 2 pour 24h).

Régler l'heure actuelle.

L'horloge démarre !


Structure du Code
Le script est organisé de manière modulaire :

set_time() / set_alarm() : Fonctions de saisie utilisateur avec gestion d'erreurs.

display_time() : Gère le rendu visuel et la conversion des formats.

run_clock() : La boucle principale gérant la logique temporelle et les interruptions menu.


Technologies Utilisées
Langage : Python 3

Bibliothèques standards : datetime, time, os, sys

Bibliothèque tierce : pyfiglet (pour le rendu des polices ASCII)


Réalisation
Ce projet a été conçu et développé par :

Mayeul Rouberty

Michel Rostain

Emanuel Placinta-Ioan
