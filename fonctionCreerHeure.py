from datetime import datetime, timedelta
import time
import sys

def horloge_creee():
    print("Configuration horloge :")
    try:
        # 1. Récupération des paramètres utilisateur
        h = int(input("Heure (0-23) : "))
        m = int(input("Minutes (0-59) : "))
        s = int(input("Secondes (0-59) : "))

        # 2. Calcul du décalage par rapport à l'heure système
        maintenant = datetime.now()
        heure_souhaitee = maintenant.replace(hour=h, minute=m, second=s, microsecond=0)
        decalage = heure_souhaitee - maintenant

        # 3. Boucle d'affichage
        while True:
            # On applique le décalage à l'heure système actuelle
            heure_virtuelle = datetime.now() + decalage
            
            # Affichage dynamique sur une seule ligne
            sys.stdout.write(f"\rIl est : {heure_virtuelle.strftime('%H:%M:%S')}")
            sys.stdout.flush()
            
            # Pause courte pour la fluidité sans consommer trop de CPU
            time.sleep(0.2)

    except ValueError:
        print("Erreur : Veuillez entrer des nombres entiers valides.")
    except KeyboardInterrupt:
        print("\n\nHorloge arrêtée.")

if __name__ == "__main__":
    horloge_creee()