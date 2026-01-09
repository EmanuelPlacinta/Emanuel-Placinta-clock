from datetime import datetime
import time
import os
import sys
import pyfiglet
import platform
import winsound

# La variable SYSTEM est une constante, signalée par le fait qu'elle est écrite en majuscule en début de code
SYSTEM=platform.system()

def check_alarm(time_tuple, alarm_settings):
    # Vérification de l'alarme par rapport au temps qui passe
    return time_tuple == alarm_settings

def set_alarm(is_24h):
    print("\n***** RÉGLAGE DE L'ALARME *****\n")
    while True:
        try:
            # Prise en compte du format 24h ou AM/PM pour les heures
            if is_24h:
                user_h = int(input("Heure de l'alarme (0-23) : "))
            else:
                suffix_choice = int(input("Vous êtes dans un format d'affichage AM/PM\nPour régler une alarme le matin, Tapez 1. Pour régler une alarme l'après-midi ? Tapez 2\nVotre choix : "))
                user_h = int(input("Heure de l'alarme (1-12) : "))
                
                # Conversion en 24h pour la logique interne
                if suffix_choice == 2 and user_h < 12:  
                    user_h += 12
                elif suffix_choice == 1 and user_h == 12: # 12 AM (Minuit)
                    user_h = 0            
            user_m = int(input("Minutes de l'alarme (0-59) : "))
            user_s = int(input("Secondes de l'alarme (0-59) : "))
            
            # Vérif des données utilisateur
            if 0 <= user_h <= 23 and 0 <= user_m <= 59 and 0 <= user_s <= 59:
                return (user_h, user_m, user_s) # On sort et on donne le tuple
            else:
                print("Valeurs hors limites, réessayez.")
        except:
            print("Veuillez entrer des nombres entiers.")


# Le son d'alarme pour windows :
def play_alarm():
    # """Déclenche le son de l'alarme de manière stable sur Windows."""
    if platform.system() == "Windows":
        file_path = "La_foule.mp3"
        if os.path.exists(file_path):
            try:
                # SND_FILENAME : charge le fichier
                # SND_ASYNC : joue en arrière-plan (ne bloque pas le reste du code)
                # SND_LOOP : recommence la musique tant qu'on ne l'arrête pas
                winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            except Exception as e:
                print(f"Erreur lecture : {e}")
                winsound.Beep(1000, 2000)
        else:
            print(f"\n[!] Fichier {file_path} introuvable dans le dossier.")
            winsound.Beep(1000, 2000)
    else:
        # Commande pour Linux
        os.system('paplay La_foule.mp3 &')

def stop_alarm():
    # """Arrête proprement le son de l'alarme."""
    if platform.system() == "Windows":
        # Passer None arrête tout son en cours lancé par PlaySound
        winsound.PlaySound(None, winsound.SND_PURGE)
    else:
        os.system('killall paplay')


def set_time(is_24h):
    # Nettoyage écran pour la lisibilité
    if SYSTEM=="Windows":
        os.system('cls')
    elif SYSTEM=="Darwin":
        sys.stdout.write('\033[H\033[J')
    else:
        os.system('clear')
    print("\n***** RÉGLAGE DE L'HEURE *****\n")
    while True:
        try:        
            # Prise en compte du format 24h pour les heures
            if is_24h:
                h = int(input("Heure (0-23) : "))
            else:
                suffix=input("C'est le matin ? Tapez 1.\nC'est l'après midi ? Tapez 2.\n\nVotre choix :" )
                h = int(input("Heure (0-12) : "))
                # --- Conversion en mode 24h pour le reste du programme ---
                if suffix == "2" and h < 12:
                    h += 12
                elif suffix == "1" and h == 12:
                    h = 0            
            m = int(input("Minutes (0-59) : "))
            s = int(input("Secondes (0-59) : "))
            
            if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
                return (h, m, s)
            else:
                print("Valeurs hors limites. Veuillez recommencer.")
        except:
            print("Erreur : Veuillez entrer des nombres entiers.")

def display_time(time_tuple, is_24h):
    if  is_24h:
        time_text = f"{time_tuple[0]:02}:{time_tuple[1]:02}:{time_tuple[2]:02}"
    
    else:
        if time_tuple[0]>=12:
            suffix="PM"
        else:
            suffix="AM"

    # Prise en compte du fait que OOH n'xiste pas dans le mode AM/PM
        h_12=time_tuple[0]%12
        if h_12==0:
            h_12=12

        time_text = f"{h_12:02}:{time_tuple[1]:02}:{time_tuple[2]:02} {suffix}"

    # Mise au format pour s'adapter à Pyfliget avec variable contenant la mise en forme pyfiglet :
    giant_time = pyfiglet.figlet_format(time_text, font='script')
    
    # Nettoyage écran pour la lisibilité
    if SYSTEM=="Windows":
        os.system('cls')
    elif SYSTEM=="Darwin":
        sys.stdout.write('\033[H\033[J')
    else:
        os.system('clear')
    
    # Affichage de l'heure
    print(giant_time)
    # Accès menu via KeyboardInterrupt

def run_clock():
    # Définition des variables alarm et is_24h
    alarm=None
    is_24h=True

    # Nettoyage écran suivant système d'exploitation
    if SYSTEM=="Windows":
        os.system('cls')
    elif SYSTEM=="Darwin":
        sys.stdout.write('\033[H\033[J')
    else:
        os.system('clear')

    # Menu de choix de format d'affichage de l'heure 
    print("\n***** Choix d'affichage de l'heure *****\n")
    format_choice=int(input("Veuillez choisir un format d'affichage :\n\n- Pour un format AM/PM, tapez 1\n- Pour un format 24h, tapez 2.\n\nVotre choix : "))
    if format_choice==1:
        is_24h=False
    if format_choice==2:
        is_24h=True

    # Appel des fonctions pour récupérer les valeurs issues du réglage de l'heure par l'utilisateur
    h_val, m_val, s_val = set_time(is_24h)    
    now = datetime.now()
    target_time = now.replace(hour=h_val, minute=m_val, second=s_val, microsecond=0)

    # Création de la variable de décalage (offset), le coeur du calcul de l'heure utilisateur
    offset = target_time - now
    
    # Boucle de fonctionnement du programme
    while True:
            try:
                while True:
                    virtual_time = datetime.now() + offset
                    time_tuple = (virtual_time.hour, virtual_time.minute, virtual_time.second)

                    display_time(time_tuple, is_24h)
                    print("***** Appuyez sur Ctrl+C pour accéder au menu *****")
                    
                    # On vérifie l'alarme seulement si elle existe
                    if alarm is not None and check_alarm(time_tuple, alarm):
                        alarm_text=("C'est l'heure")
                        
                        if SYSTEM=="Windows":
                            play_alarm()
                        elif SYSTEM=="Darwin":
                            os.system('afplay La_foule.mp3 &')
                        else:
                            os.system('paplay La_foule.mp3 &')
                        
                        giant_text = pyfiglet.figlet_format(alarm_text, font='block')
                        
                        # Nettoyage écran suivant système d'exploitation
                        if SYSTEM=="Windows":
                            os.system('cls')
                        elif SYSTEM=="Darwin":
                            sys.stdout.write('\033[H\033[J')
                        else:
                            os.system('clear')

                        print(giant_text)
                        print(input("***** Appuyez sur entrée pour  continuer *****"))

                        # Fin du  precssus de lecture pour chaque système d'exploitation
                        if SYSTEM == "Windows":
                            stop_alarm()
                        elif SYSTEM == "Darwin":
                            os.system('killall afplay')
                        else:
                            os.system('killall paplay')
                    time.sleep(1)

            # Accès au menu et affichage de celui-ci
            except KeyboardInterrupt:
                os.system('clear')
                print("\n***** Menu *****\n")
                print("1. Régler l'heure")
                print("2. Régler l'alarme")
                print("3. Annuler alarme")
                print("4. Quitter le menu et Reprendre")
                print("5. Changer de mode d'affichage (24h ou AM/PM)")
                print("6. Mettre l'horloge affichée en pause")
                print("7. Geler l'horloge")
                print("8. Quitter l'horloge")
                
                choice = input("Votre choix : ")

                if choice == "1":
                    # On retourne vers la fonction set_time()
                    h_val, m_val, s_val = set_time(is_24h)
                    
                    # On recalcule le offset
                    now = datetime.now()
                    target_time = now.replace(hour=h_val, minute=m_val, second=s_val)
                    offset = target_time - now
                    print("Heure mise à jour avec succès.")
                
                elif choice == "2":
                    if alarm is not None:
                        if SYSTEM=="Windows":
                            os.system('cls')
                        elif SYSTEM=="Darwin":
                            sys.stdout.write('\033[H\033[J')
                        else:
                            os.system('clear')
                        print(f"La précédente alarme était réglée sur {alarm[0]:02}h{alarm[1]:02}m{alarm[2]:02}s")                
                    alarm = set_alarm(is_24h)

                elif choice == "3":
                    if alarm==None:
                        print("Il n' avait pas d'alarme programmée.")
                        alarm=None
                    elif alarm is not None:
                        print("Votre alarme a été annulée.")
                        alarm=None

                elif choice == "4":
                # Reprise de la boucle While :
                    print("Reprise de l'horloge...")
                    continue                

                elif choice == "5":
                    # Permet d'alterner avec la précédent format d'affichage choisi 
                    is_24h=not is_24h
                    if SYSTEM=="Windows":
                        os.system('cls')
                    elif SYSTEM=="Darwin":
                        sys.stdout.write('\033[H\033[J')
                    else:
                        os.system('clear')
                    print("***** Format d'affichage mis à jour *****")
                    time.sleep(2)
                
                elif choice ==  "6":
                    forced_offset=datetime.now()+offset
                    fixed_time=(forced_offset.hour, forced_offset.minute, forced_offset.second)
                    display_time(fixed_time, is_24h)
                    print(input("Appuyez sur Entrée pour reprendre "))

                elif choice == "7":
                    # Pour le calcul de la pause (pas affiché)
                    debut_pause=datetime.now()
                    # Pour le temps affiché (du coup on inclu le décalage)
                    time_stopped=debut_pause+offset
                    # On transforme en tuple pour l'affichage
                    time_stopped_tuple=(time_stopped.hour, time_stopped.minute, time_stopped.second)
                    display_time(time_stopped_tuple, is_24h)
                    print(input("Appuyez sur Entrée pour reprendre "))
                    end_pause=datetime.now()

                    lenght_pause=end_pause-debut_pause
                    offset=offset-lenght_pause

                elif choice == "8":
                    # On quitte proprement le programme
                    bye_text=("Au revoir !")
                    giant_bye = pyfiglet.figlet_format(bye_text, font='letter')
                    if SYSTEM=="Windows":
                        os.system('cls')
                    elif SYSTEM=="Darwin":
                        sys.stdout.write('\033[H\033[J')
                    else:
                        os.system('clear')

                    print(giant_bye)
                    time.sleep(2)

                    if SYSTEM=="Windows":
                        os.system('cls')
                    elif SYSTEM=="Darwin":
                        sys.stdout.write('\033[H\033[J')
                    else:
                        os.system('clear')
                    sys.exit()

                else:
                    print("Mauvaise entrée, retour à l'horloge !")
                    time.sleep(2)
                    continue
run_clock()