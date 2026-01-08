#  L’horloge de mamie

Une horloge interactive et élégante développée en Python pour le terminal. Ce projet simule une horloge temps réel avec un affichage en ASCII Art, incluant une gestion d'alarme et une personnalisation complète des formats horaires.

---

##  Fonctionnalités

* **Affichage ASCII Art** : Rendu visuel "old-school" utilisant la bibliothèque `pyfiglet`.
* **Double Format Horaire** : Basculez facilement entre le mode **24 heures** et le mode **12 heures (AM/PM)**.
* **Système d'Alarme** : Programmez une alarme avec une notification visuelle à l'écran.
* **Gestion Dynamique** : Réglage manuel de l'heure avec calcul automatique de l'écart (offset) par rapport à l'heure système.
* **Menu de Contrôle** : Accès à tout moment aux paramètres via l'interruption clavier `Ctrl+C`.
* **Mode Pause** : Possibilité de figer l'heure affichée à l'écran.

---

##  Installation & Lancement

### 1. Prérequis
Assurez-vous d'avoir Python 3 installé sur votre machine.

---

### 2. Installation de la dépendance
Ce projet utilise `pyfiglet` pour générer les polices de caractères ASCII :
```bash
pip install pyfiglet
```

---

### Guide d'utilisation
1. Initialisation : Au lancement, choisissez votre format (1 ou 2) puis réglez l'heure de départ.
2. Accès au Menu : Pendant que l'horloge tourne, appuyez sur Ctrl + C pour ouvrir les options.
3. Options disponibles :
* **1 : Redéfinir l'heure actuelle**

* **2 : Configurer une nouvelle alarme**

* **3 : Annuler l'alarme active**

* **5 : Alterner entre le format 24h et AM/PM**

* **6 : Mettre l'horloge en pause (appui sur Entrée pour reprendre)**

* **7 : Quitter proprement le programme avec un message d'adieu**

---

### Réalisation
Ce projet a été réalisé avec succès par :
* **Mayeul Rouberty**
* **Michel Rostain**
* **Emanuel Placinta-Ioan**
