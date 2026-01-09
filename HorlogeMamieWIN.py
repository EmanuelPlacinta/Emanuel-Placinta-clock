from datetime import datetime
import time
import os
import sys
import pyfiglet
import platform

# Importation automatique de winsound uniquement si on est sur Windows
if platform.system() == "Windows":
    import winsound

def clear_screen():
    """Nettoie le terminal selon le système d'exploitation."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def play_alarm():
    """Déclenche le son de l'alarme selon l'OS."""
    if platform.system() == "Windows":
        try:
            # Tente de jouer le fichier WAV en boucle et en arrière-plan
            winsound.PlaySound("La_foule.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        except:
            # Si le fichier est introuvable, utilise un BIP système
            print("Fichier audio non trouvé, bip de secours...")
            winsound.Beep(1000, 2000) 
    else:
        # Commande pour Linux
        os.system('paplay La_foule.mp3 &')

def stop_alarm():
    """Arrête le son de l'alarme."""
    if platform.system() == "Windows":
        winsound.PlaySound(None, winsound.SND_PURGE)
    else:
        os.system('killall paplay')

def check_alarm(time_tuple, alarm_settings):
    return time_tuple == alarm_settings

def set_alarm(is_24h):
    print("\n***** RÉGLAGE DE L'ALARME *****\n")
    while True:
        try:
            if is_24h:
                user_h = int(input("Heure de l'alarme (0-23) : "))
            else:
                print("1. Matin (AM)")
                print("2. Après-midi (PM)")
                suffix_choice = int(input("Votre choix : "))
                user_h = int(input("Heure de l'alarme (1-12) : "))
                if suffix_choice == 2 and user_h < 12:  
                    user_h += 12
                elif suffix_choice == 1 and user_h == 12:
                    user_h = 0            
            user_m = int(input("Minutes (0-59) : "))
            user_s = int(input("Secondes (0-59) : "))
            
            if 0 <= user_h <= 23 and 0 <= user_m <= 59 and 0 <= user_s <= 59:
                return (user_h, user_m, user_s)
            else:
                print("Valeurs hors limites, réessayez.")
        except ValueError:
            print("Veuillez entrer des nombres entiers.")

def set_time(is_24h):
    clear_screen()
    print("\n***** RÉGLAGE DE L'HEURE *****\n")
    while True:
        try:        
            if is_24h:
                h = int(input("Heure (0-23) : "))
            else:
                print("1. Matin")
                print("2. Après-midi")
                suffix = input("Votre choix : ")
                h = int(input("Heure (0-12) : "))
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
        except ValueError:
            print("Erreur : Veuillez entrer des nombres entiers.")

def display_time(time_tuple, is_24h):
    if is_24h:
        time_text = f"{time_tuple[0]:02}:{time_tuple[1]:02}:{time_tuple[2]:02}"
    else:
        suffix = "PM" if time_tuple[0] >= 12 else "AM"
        h_12 = time_tuple[0] % 12
        if h_12 == 0: h_12 = 12
        time_text = f"{h_12:02}:{time_tuple[1]:02}:{time_tuple[2]:02} {suffix}"

    giant_time = pyfiglet.figlet_format(time_text, font='script')
    clear_screen()
    print(giant_time)

def run_clock():
    alarm = None
    is_24h = True
    clear_screen()

    print("\n***** Choix d'affichage de l'heure *****\n")
    try:
        format_choice = int(input("- Pour un format AM/PM, tapez 1\n- Pour un format 24h, tapez 2\nVotre choix : "))
        is_24h = (format_choice == 2)
    except:
        is_24h = True

    # Réglage initial
    h_val, m_val, s_val = set_time(is_24h)    
    now = datetime.now()
    target_time = now.replace(hour=h_val, minute=m_val, second=s_val, microsecond=0)
    offset = target_time - now
    
    while True:
        try:
            while True:
                virtual_time = datetime.now() + offset
                time_tuple = (virtual_time.hour, virtual_time.minute, virtual_time.second)

                display_time(time_tuple, is_24h)
                print("***** Appuyez sur Ctrl+C pour accéder au menu *****")
                
                # Vérification de l'alarme
                if alarm is not None and check_alarm(time_tuple, alarm):
                    play_alarm()
                    
                    alarm_text = "C'est l'heure"
                    giant_text = pyfiglet.figlet_format(alarm_text, font='block')
                    clear_screen()
                    print(giant_text)
                    
                    input("\n>>> ALARME ACTIVE ! Appuyez sur ENTREE pour arrêter <<<")
                    stop_alarm()
                    alarm = None # Désactivation après déclenchement

                time.sleep(1)

        except KeyboardInterrupt:
            clear_screen()
            print("\n***** Menu *****\n")
            print("1. Régler l'heure")
            print("2. Régler l'alarme")
            print("3. Annuler alarme")
            print("4. Reprendre l'horloge")
            print("5. Changer format (24h / AM-PM)")
            print("8. Quitter l'horloge")
            
            choice = input("\nVotre choix : ")

            if choice == "1":
                h_val, m_val, s_val = set_time(is_24h)
                now = datetime.now()
                target_time = now.replace(hour=h_val, minute=m_val, second=s_val)
                offset = target_time - now
            elif choice == "2":
                alarm = set_alarm(is_24h)
            elif choice == "3":
                alarm = None
                print("Alarme annulée.")
                time.sleep(1)
            elif choice == "5":
                is_24h = not is_24h
            elif choice == "8":
                clear_screen()
                print(pyfiglet.figlet_format("Au revoir !", font='small'))
                sys.exit()
            else:
                continue

if __name__ == "__main__":
    run_clock()