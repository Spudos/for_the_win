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
    
    home_on_target = int(home_chances  * 0.75 * (att_counth / def_counta))
    away_on_target = int(away_chances  * 0.75 * (att_counta / def_counth))
    
    print()
    print("On target calculated")
    print("Home on target: ", home_on_target, " away on target: ", away_on_target)
    print()

    return home_on_target, away_on_target

def calc_possession(home_chances, away_chances):
    print()
    print("Calculating possession for each team.....")
    print() 

    home_possession = 0
    away_possession = 0

    possession_random = random.randint(-10, 10)
    home_possession = (int(home_chances / (away_chances + home_chances) * 100) + possession_random)

    away_possession = 100 - home_possession

    print()
    print("Possession calculated")
    print("Home possession: ", home_possession, " away possession: ", away_possession)
    print()

    return home_possession, away_possession

def calc_goals(home_on_target, away_on_target, def_counth, att_counth, def_counta, att_counta):
    print()
    print("Calculating goals scored for each team.....")
    print() 

    home_goals = int(((att_counth / def_counta) * 0.7 * home_on_target)/2)
    away_goals = int(((att_counta / def_counth) * 0.7 * away_on_target)/2)

    print()
    print("Goals scored calculated")
    print("Home goals: ", home_goals, " Away goals: ", away_goals)
    print()

    return home_goals, away_goals