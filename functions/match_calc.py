import random

def calc_chances(mid_counth, mid_counta):
    print()
    print("Calculating the number of chances for each team.....")
    print()

    home_mid = mid_counth
    away_mid = mid_counta

    home_random = random.randint(-5, 5)
    away_random = random.randint(-5, 5)
    
    home_chances = int((home_mid / (home_mid + away_mid)) * 30) + home_random
    away_chances = int((away_mid / (home_mid + away_mid)) * 30) + away_random

    print()
    print("Team chances calculated")
    print(f"Home chances: ", home_chances, " Away chances: ", away_chances)
    print()

    return home_chances, away_chances

def calc_on_target(home_chances, away_chances, att_counth, def_counth, att_counta, def_counta):
    print()
    print("Calculating the number of on target for each team.....")
    print()

    home_random = random.randint(-1, 3)
    away_random = random.randint(-2, 2)
    
    home_on_target = int(home_random + ((home_chances - 3) * (att_counth / def_counta))) 
    away_on_target = int(away_random + ((away_chances - 2) * (att_counta / def_counth)))
    
    print()
    print("On target calculated")
    print("Home on target: ", home_on_target, " away on target: ", away_on_target)
    print()

    return home_on_target, away_on_target

def calc_possesion(home_chances, away_chances):
    print()
    print("Calculating possesion for each team.....")
    print() 

    home_possesion = 0
    away_possesion = 0

    possesion_random = random.randint(-10, 10)
    home_possesion = (int(home_chances / (away_chances + home_chances) * 100) + possesion_random)

    away_possesion = 100 - home_possesion

    print()
    print("Possesion calculated")
    print("Home possesion: ", home_possesion, " away possesion: ", away_possesion)
    print()

def calc_goals(home_on_target, away_on_target, def_counth, att_counth, def_counta, att_counta):
    print()
    print("Calculating goals scored for each team.....")
    print() 

    home_goals = int(((att_counth / def_counta) * home_on_target)/2)
    away_goals = int(((att_counta / def_counth) * away_on_target)/2)

    print()
    print("Goals scored calculated")
    print("Home goals: ", home_goals, " Away goals: ", away_goals)
    print()