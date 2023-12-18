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

    print(f"Home chances: ", home_chances, " random: ", home_random)
    print(f"Away chances: ", away_chances, " random: ", away_random)

    return home_chances, away_chances

def calc_goals(home_chances, away_chances):
    home_goals = int(home_chances * random.randint(0, 7) / 20)
    away_goals = int(away_chances * random.randint(0, 7) / 20)

    print(f"Home goals: ", home_goals, " Away goals: ", away_goals)
  
