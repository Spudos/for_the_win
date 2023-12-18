import random

def calc_chances(data):
    print()
    print("Calculating the number of chances for each team.....")
    print()

    home_mid = data
    away_mid = 150

    home_random = random.randint(-5, 5)
    away_random = random.randint(-5, 5)
    
    home_chances = int((home_mid / (home_mid + away_mid)) * 30) + home_random
    away_chances = int((away_mid / (home_mid + away_mid)) * 30) + away_random

    print()
    print("Team chances calculated")
    print(f"Home chances: ", home_chances, " random: ", home_random)
    print(f"Away chances: ", away_chances, " random: ", away_random)

    return home_chances, away_chances

def calc_on_target(home_chances, away_chances, att_count, def_count):
    
    home_random = random.randint(-1, 3)
    away_random = random.randint(-2, 2)
    
    home_on_target = int(home_random + ((home_chances - 3) * (att_count / def_count))) 
    away_on_target = int(away_random + ((away_chances - 2) * 0.5))

    print("Home on target: ", home_on_target, " away on target: ", away_on_target)

def calc_possesion(home_chances, away_chances):
    
    home_possesion = 0
    away_possesion = 0

    possesion_random = random.randint(-20, 20)
    home_possesion = (int(home_chances / (away_chances + home_chances) * 100) + possesion_random)

    away_possesion = 100 - home_possesion

    print("Home possesion: ", home_possesion, " away possesion: ", away_possesion)
