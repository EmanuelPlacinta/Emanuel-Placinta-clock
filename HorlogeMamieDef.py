from datetime import datetime
import time
import os
import sys
import pyfiglet

def check_alarm(tuple_heure, alarm_settings):
    # Vérification de l'alarme par rapport au temps qui passe
    return tuple_heure == alarm_settings

def regler_alarme(format24h):
    print("\n***** RÉGLAGE DE L'ALARME *****\n")
    while True:
        try:
            # Prise en compte du format 24h ou AM/PM pour les heures
            if format24h:
                user_h = int(input("Heure de l'alarme (0-23) : "))
            else:
                choix_suffixe = int(input("Vous êtes dans un format d'affichage AM/PM\nPour régler une alarme le matin, Tapez 1. Pour régler une alarme l'après-midi ? Tapez 2\nVotre choix : "))
                user_h = int(input("Heure de l'alarme (1-12) : "))
                
                # Conversion en 24h pour la logique interne
                if choix_suffixe == 2 and user_h < 12:  
                    user_h += 12
                elif choix_suffixe == 1 and user_h == 12: # 12 AM (Minuit)
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

def regler_heure(format24h):
    # Nettoyage écran pour la lisibilité
    os.system('clear')
    print("\n***** RÉGLAGE DE L'HEURE *****\n")
    while True:
        try:        
            # Prise en compte du format 24h pour les heures
            if format24h:
                h = int(input("Heure (0-23) : "))
            else:
                suffixe=input("C'est le matin ? Tapez 1.\nC'est l'après midi ? Tapez 2.\n\nVotre choix :" )
                h = int(input("Heure (0-12) : "))
                # --- Conversion en mode 24h pour le reste du programme ---
                if suffixe == "2" and h < 12:
                    h += 12
                elif suffixe == "1" and h == 12:
                    h = 0            
            m = int(input("Minutes (0-59) : "))
            s = int(input("Secondes (0-59) : "))
            
            if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
                return (h, m, s)
            else:
                print("Valeurs hors limites. Veuillez recommencer.")
        except:
            print("Erreur : Veuillez entrer des nombres entiers.")

def afficher_heure(tuple_heure, format24h):
    if  format24h:
        heure_texte = f"{tuple_heure[0]:02}:{tuple_heure[1]:02}:{tuple_heure[2]:02}"
    
    else:
        if tuple_heure[0]>=12:
            suffixe="PM"
        else:
            suffixe="AM"

    # Prise en compte du fait que OOH n'xiste pas dans le mode AM/PM
        h_12=tuple_heure[0]%12
        if h_12==0:
            h_12=12

        heure_texte = f"{h_12:02}:{tuple_heure[1]:02}:{tuple_heure[2]:02} {suffixe}"

    # Mise au format pour s'adapter à Pyfliget avec variable contenant la mise en forme pyfiglet :
    heure_geante = pyfiglet.figlet_format(heure_texte, font='script')
    
    # Nettoyage écran pour la lisibilité
    os.system('clear')
    
    # Affichage de l'heure
    print(heure_geante)
    # Accès menu via KeyboardInterrupt

def horloge_creee():
    # Définition des variables alarme et format24h
    alarme=None
    format24h=True

    os.system('clear')

    # Menu de choix de format d'affichage de l'heure 
    print("\n***** Choix d'affichage de l'heure *****\n")
    choix_format=int(input("Veuillez choisir un format d'affichage :\n\n- Pour un format AM/PM, tapez 1\n- Pour un format 24h, tapez 2.\n\nVotre choix : "))
    if choix_format==1:
        format24h=False
    if choix_format==2:
        format24h=True

    # Appel des fonctions pour récupérer les valeurs issues du réglage de l'heure par l'utilisateur
    h_val, m_val, s_val = regler_heure(format24h)    
    maintenant = datetime.now()
    heure_souhaitee = maintenant.replace(hour=h_val, minute=m_val, second=s_val, microsecond=0)

    # Création de la variable de décalage, le coeur du calcul de l'heure utilisateur
    decalage = heure_souhaitee - maintenant
    
    # Boucle de fonctionnement du programme
    while True:
            try:
                while True:
                    heure_virtuelle = datetime.now() + decalage
                    tuple_heure = (heure_virtuelle.hour, heure_virtuelle.minute, heure_virtuelle.second)

                    afficher_heure(tuple_heure, format24h)
                    print("***** Appuyez sur Ctrl+C pour accéder au menu *****")
                    # On vérifie l'alarme seulement si elle existe
                    if alarme is not None and check_alarm(tuple_heure, alarme):
                        alarme_texte=("C'est l'heure")
                        os.system('paplay La_foule.mp3 &')
                        texte_geant = pyfiglet.figlet_format(alarme_texte, font='block')
                        os.system('clear')

                        print(texte_geant)
                        print(input("***** Appuyez sur entrée pour  continuer *****"))
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
                print("6. Mettre l'horloge en pause")
                print("7. Geler l'horloge")
                print("8. Quitter l'horloge")
                
                choix = input("Votre choix : ")

                if choix == "1":
                    # On retourne vers la fonction regler_heure()
                    h_val, m_val, s_val = regler_heure(format24h)
                    
                    # On recalcule le décalage
                    maintenant = datetime.now()
                    heure_souhaitee = maintenant.replace(hour=h_val, minute=m_val, second=s_val)
                    decalage = heure_souhaitee - maintenant
                    print("Heure mise à jour avec succès.")
                
                elif choix == "2":
                    if alarme is not None:
                        os.system('clear')
                        print(f"La précédente alarme était réglée sur {alarme[0]:02}h{alarme[1]:02}m{alarme[2]:02}s")                
                    alarme = regler_alarme(format24h)

                elif choix == "3":
                    if alarme==None:
                        print("Il n' avait pas d'alarme programmée.")
                        alarme=None
                    elif alarme is not None:
                        print("Votre alarme a été annulée.")
                        alarme=None

                elif choix == "4":
                # Reprise de la boucle While :
                    print("Reprise de l'horloge...")
                    continue                

                elif choix == "5":
                    # Permet d'alterner avec la précédent format d'affichage choisi 
                    format24h=not format24h
                    os.system('clear')
                    print("***** Format d'affichage mis à jour *****")
                    time.sleep(2)
                
                elif choix ==  "6":
                    decalage_force=datetime.now()+decalage
                    heure_fixe=(decalage_force.hour, decalage_force.minute, decalage_force.second)
                    afficher_heure(heure_fixe, format24h)
                    print(input("Appuyez sur Entrée pour reprendre "))

                elif choix == "7":
                    # Pour le calcul de la pause (pas affiché)
                    debut_pause=datetime.now()
                    # Pour le temps affiché (du coup on inclu le décalage)
                    temps_arrete=debut_pause+decalage
                    # On transforme en tuple pour l'affichage
                    temps_arrete_tuple=(temps_arrete.hour, temps_arrete.minute, temps_arrete.second)
                    afficher_heure(temps_arrete_tuple, format24h)
                    print(input("Appuyez sur Entrée pour reprendre "))
                    fin_pause=datetime.now()

                    longueur_pause=fin_pause-debut_pause
                    decalage=decalage-longueur_pause

                elif choix == "8":
                    # On quitte proprement le programme
                    au_revoir=("Au revoir !")
                    giant_bye = pyfiglet.figlet_format(au_revoir, font='letter')
                    os.system('clear')
                    print(giant_bye)
                    time.sleep(2)
                    os.system('clear')
                    sys.exit()

                else:
                    print("Mauvaise entrée, retour à l'horloge !")
                    time.sleep(2)
                    continue
horloge_creee()