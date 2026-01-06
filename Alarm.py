import time
import datetime

def check_alarm(tuple_heure, alarm_settings):
    current_h, current_m, current_s = tuple_heure
    alarm_h, alarm_m, alarm_s = alarm_settings
    
    if current_h == alarm_h and current_m == alarm_m and current_s == alarm_s:
        return True
    return False

while True:
    # Set Alarm
    print("\n=== SET YOUR ALARM ===")
    print("(To change alarm anytime, press Ctrl+C)")
    try:
        user_h = int(input("Set hours (0-23): "))
        user_m = int(input("Set minutes (0-59): "))
        user_s = int(input("Set seconds (0-59): "))
    except ValueError:
        print("Please enter numbers only.")
        continue

    my_personal_alarm = (user_h, user_m, user_s)
    print(f"Alarm set for: {user_h:02d}:{user_m:02d}:{user_s:02d}")

    # SIM Clock
    print("\nClock is running... (Press Ctrl+C to reset)")
    try:
        while True:
            now = datetime.datetime.now()
            tuple_heure = (now.hour, now.minute, now.second)
            
            print(f"Current time: {tuple_heure[0]:02d}:{tuple_heure[1]:02d}:{tuple_heure[2]:02d}", end="\r")

            if check_alarm(tuple_heure, my_personal_alarm):
                print("\n" + "!" * 20)
                print("ALARM RINGING!")
                print("!" * 20)
                input("Press 'Enter' to set a new one...")
                break # Back to the menu
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\nResetting... Let's set a new alarm.")
        continue