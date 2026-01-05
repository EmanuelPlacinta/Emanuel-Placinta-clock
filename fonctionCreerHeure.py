from datetime import datetime, timedelta
import time
import sys

def fonction_alarme(tuple_heure):
    if tuple_heure[0] == 12:
        sys.stdout.write(" C'est Midi !")
        sys.stdout.flush()

def horloge_creee():
    print("Configuration horloge :")

    def heures():
        while True:
            try:
                h = int(input("Heure (0-23) : "))
                if 0 <= h <= 23:
                    return h  # On sort de la boucle et on renvoie la valeur
                else:
                    print("Mauvaise entrée (doit être entre 0 et 23), réessayez.")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre entier.")

    def minutes():
        while True:
            try:
                m = int(input("Minutes (0-59) : "))
                if 0 <= m <= 59:
                    return m
                else:
                    print("Mauvaise entrée (0-59), réessayez.")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre entier.")

    def secondes():
        while True:
            try:
                s = int(input("Secondes (0-59) : "))
                if 0 <= s <= 59:
                    return s
                else:
                    print("Mauvaise entrée (0-59), réessayez.")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre entier.")


    # Appel des fonctions pour récupérer les valeurs
    h_val = heures()
    m_val = minutes()
    s_val = secondes()
    
    maintenant = datetime.now()
    heure_souhaitee = maintenant.replace(hour=h_val, minute=m_val, second=s_val, microsecond=0)
    decalage = heure_souhaitee - maintenant



    # AFFICHAGE DE L'HEURE EN DIRECT :
    while True:
         # On applique le décalage à l'heure système actuelle
        heure_virtuelle = datetime.now() + decalage
        
        # CREATION DU TUPLE ET AFFICHAGE :
        tuple_heure = (heure_virtuelle.hour, heure_virtuelle.minute, heure_virtuelle.second)
        sys.stdout.write(f"\rHeure : {tuple_heure[0]:02}:{tuple_heure[1]:02}:{tuple_heure[2]:02}")
        sys.stdout.flush()
        time.sleep(1)
        fonction_alarme(tuple_heure)

horloge_creee()