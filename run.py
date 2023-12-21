import gspread, random
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Load Teams ----------------------------------------------------------------

def get_aw():
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('for_the_win')

    players_worksheet = SHEET.worksheet('players')

    aw = []
    for row in players_worksheet.get_all_records():
        if row.get('id') != '' and row.get('club') == 'LIV':
            player = {
                "id": row.get('id'),
                "name": row.get('name'),
                "pos": row.get('pos'),
                "pa": row.get('pa'),
                "co": row.get('co'),
                "tk": row.get('tk'),
                "ru": row.get('ru'),
                "sh": row.get('sh'),
                "he": row.get('he'),
                "fl": row.get('fl'),
                "st": row.get('st'),
                "cr": row.get('cr'),
                "ts": row.get('ts'),
                "fit": row.get('fit'),
                "perf": row.get('perf'),
                "adj_perf": row.get('adj_perf')
            }
            print(player)
            aw.append(player)

    aw_abbr = "awy"

    return aw, aw_abbr

def get_players():
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('for_the_win')

    players_worksheet = SHEET.worksheet('players')

    player_data = []
    for row in players_worksheet.get_all_records():
        if row.get('id') != '':
            player = {
                "id": row.get('id'),
                "name": row.get('name'),
                "pos": row.get('pos'),
                "pa": row.get('pa'),
                "co": row.get('co'),
                "tk": row.get('tk'),
                "ru": row.get('ru'),
                "sh": row.get('sh'),
                "he": row.get('he'),
                "fl": row.get('fl'),
                "st": row.get('st'),
                "cr": row.get('cr'),
                "ts": row.get('ts'),
                "fit": row.get('fit'),
                "perf": row.get('perf'),
                "adj_perf": row.get('adj_perf')
            }

            player_data.append(player)

    return player_data

def print_gk(player):
    print()
    print("Goalkeepers------------------------------")
    for player in player:
        if player['pos'] == "GK":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} skill")
   
def print_def(player): 
    print()  
    print("Defenders--------------------------------")
    for player in player:
        if player['pos'] == "DEF":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} skill")
    
def print_mid(player):    
    print()
    print("Midfielders-------------------------------")
    for player in player:    
        if player['pos'] == "MID":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} skill")
    
def print_att(player): 
    print()   
    print("Attackers---------------------------------")
    for player in player:    
        if player['pos'] == "ATT":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} skill")
    print("------------------------------------------")
  
def select_team(player_data):
    hm = []
    for i in range(1, 12):
        player_id = int(input(f"{i} Select id of player: "))
        team = player_data[player_id - 1]
        hm.append(team)
        
    print(hm)

    hm_abbr = "usr"

    aw, aw_abbr = get_aw()

    return hm, hm_abbr, aw, aw_abbr

# Perform player adjustments----------------------------------------------------------------

def calc_on_player_fitness(data):
    # Perform calculation on each stat and update the 'perf' field in the original data list
    for record in data:
        pos = record['pos']
        fit = record['fit']
        if pos == "GK":
            perf = int(((record['pa'] + record['co'] + record['sh'] + record['he'] + record['st']) + (record['tk'] + record['ru'] + record['fl'] + record['cr']) / 2) * fit / 100)
        elif pos == "DEF":
            perf = int(((record['co'] + record['tk'] + record['ru'] + record['he'] + record['st']) + (record['pa'] + record['sh'] + record['fl'] + record['cr']) / 2) * fit / 100)
        elif pos == "MID":
            perf = int(((record['pa'] + record['co'] + record['ru'] + record['fl'] + record['cr']) + (record['tk'] + record['sh'] + record['he'] + record['st']) / 2) * fit / 100)
        else:
            perf = int(((record['co'] + record['ru'] + record['sh'] + record['fl'] + record['st']) + (record['pa'] + record['tk'] + record['he'] + record['cr']) / 2) * fit / 100)
        
        record['perf'] = perf

    return data


def calc_on_player_random_perf(data):
    
    for i in data:
        perf = i['perf']
        random_adjustment = random.randint(-20, 20)
        i['adj_perf'] = int(perf + random_adjustment)
    
    return data

def run_player_adj(hm,aw):
    hm_data = calc_on_player_fitness(hm)
    hm_data_1 = calc_on_player_random_perf(hm_data)

    aw_data = calc_on_player_fitness(aw)
    aw_data_1 = calc_on_player_random_perf(aw_data)

    return hm_data_1, aw_data_1

# Calculate team totals----------------------------------------------------------------

def calculate_team(data):
    print()
    print()
    print("team_calc")
    print(data)
    # Initialize position counters
    def_count = 0
    mid_count = 0
    att_count = 0

    # Iterate through the player data
    for record in data:
        adj_perf = record['adj_perf']
        pos = record['pos']
     
        # Add the performance to the respective position counter
        if pos == "GK":
            def_count += adj_perf
        elif pos == "DEF":
            def_count += adj_perf       
        elif pos == "MID":
            mid_count += adj_perf
        elif pos == "ATT":
            att_count += adj_perf
    
    print()
    print("Team values calculated")
    print("Defence: ", def_count, " Midfield: ", mid_count, " Attack: ", att_count)

    return def_count, mid_count, att_count

# Run the match----------------------------------------------------------------

def calc_cha(hm_mid_cnt, aw_mid_cnt):

    hm_mid = hm_mid_cnt
    aw_mid = aw_mid_cnt

    hm_random = random.randint(-5, 5)
    aw_random = random.randint(-5, 5)
    
    hm_cha = int((hm_mid / (hm_mid + aw_mid)) * 30) + hm_random
    aw_cha = int((aw_mid / (hm_mid + aw_mid)) * 30) + aw_random

    print()
    print("Team cha calculated")
    print(f"hm cha: ", hm_cha, " aw cha: ", aw_cha)

    return hm_cha, aw_cha

def calc_on_tar(hm_cha, aw_cha, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt):
    
    hm_on_tar = int(hm_cha  * 0.75 * (hm_att_cnt / aw_def_cnt))
    aw_on_tar = int(aw_cha  * 0.75 * (aw_att_cnt / hm_def_cnt))
    
    print()
    print("On tar calculated")
    print("hm on tar: ", hm_on_tar, " aw on tar: ", aw_on_tar)

    return hm_on_tar, aw_on_tar

def calc_poss(hm_cha, aw_cha):

    hm_poss = 0
    aw_poss = 0

    poss_random = random.randint(-10, 10)
    hm_poss = (int(hm_cha / (aw_cha + hm_cha) * 100) + poss_random)

    aw_poss = 100 - hm_poss

    print()
    print("poss calculated")
    print("hm poss: ", hm_poss, " aw poss: ", aw_poss)

    return hm_poss, aw_poss

def calc_gls(hm_on_tar, aw_on_tar, hm_def_cnt, hm_att_cnt, aw_def_cnt, aw_att_cnt):

    hm_gls = int(((hm_att_cnt / aw_def_cnt) * 0.7 * hm_on_tar)/2)
    aw_gls = int(((aw_att_cnt / hm_def_cnt) * 0.7 * aw_on_tar)/2)

    print()
    print("gls scored calculated")
    print("hm gls: ", hm_gls, " aw gls: ", aw_gls)

    return hm_gls, aw_gls

def motm(hm_data_1, aw_data_1):
    
    hm_motm = max(hm_data_1, key=lambda x: x['adj_perf'])
    aw_motm = max(aw_data_1, key=lambda x: x['adj_perf'])

    print()
    print("motm calculated")
    print(f"hm motm: {hm_motm['name']}  - perf {hm_motm['adj_perf']}  aw motm: {aw_motm['name']} - perf {aw_motm['adj_perf']}")

    return hm_motm, aw_motm

def generate_top_5(team_list, mid_adj, att_adj):    
    new_list = []
    for item in team_list:
        if item['pos'] == 'MID':
            item['top_5'] = item['perf'] + mid_adj
            new_list.append(item)
        elif item['pos'] == 'ATT':
            item['top_5'] = item['perf'] + att_adj
            new_list.append(item)
        else:
            item['top_5'] = item['perf']
            new_list.append(item)    

    sort_team_list = sorted(new_list, key=lambda x: x['top_5'], reverse=True)   
    top_5 = [player for player in sort_team_list if player['pos'] != 'GK']
    
    return top_5

    
def generate_goal_info(player_assist, player_score, team_name):
    goal_info = {
        "scored_by": player_score['name'],  # Access the player's name using the key 'name'
        "assisted_by": player_assist['name'],  # Access the player's name using the key 'name'
        "team": team_name
    }
    return goal_info


def generate_goals(team_gls, team_data, team_name):
    goal_list = []
    team_ass = generate_top_5(team_data, 30, 15)
    team_scr = generate_top_5(team_data, 15, 30)

    for i in range(team_gls):
        pl_ass = random.choice(team_ass)
        pl_gls = random.choice(team_scr)

        # Check if the scorer is the same as the assister
        while pl_gls['name'] == pl_ass['name']:  # Access the player's name using the key 'name'
            pl_gls = random.choice(team_scr)

        print(f"{team_name} goal {i + 1} assisted by {pl_ass['name']} and scored by {pl_gls['name']}")
        goal_info = generate_goal_info(pl_ass, pl_gls, team_name)
        goal_list.append(goal_info)

    return goal_list


def goals(hm_gls, aw_gls, hm_data_1, aw_data_1):
    hm_goals = generate_goals(hm_gls, hm_data_1, "hm")
    aw_goals = generate_goals(aw_gls, aw_data_1, "aw")
    return hm_goals + aw_goals


def run_match(hm_mid_cnt, aw_mid_cnt, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt, hm_data_1, aw_data_1):
    hm_cha, aw_cha = calc_cha(hm_mid_cnt, aw_mid_cnt)

    # claculate how many cha are on tar
    hm_on_tar, aw_on_tar = calc_on_tar(hm_cha, aw_cha, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt)

    # calculate the possesion stats
    hm_poss, aw_poss = calc_poss(hm_cha, aw_cha)

    # calculate how many gls are scored
    hm_gls, aw_gls = calc_gls(hm_on_tar, aw_on_tar, hm_def_cnt, hm_att_cnt, aw_att_cnt, aw_def_cnt)
    
    # calculate who made and scored goals
    goal_list = goals(hm_gls, aw_gls, hm_data_1, aw_data_1)

    # calculate motm for each team
    hm_motm, aw_motm = motm(hm_data_1, aw_data_1)

    return hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list 

# Produce match output----------------------------------------------------------------

def text_file_match_output(hm_abbr, aw_abbr, hm_data_1, aw_data_1, hm_def_cnt, hm_mid_cnt, hm_att_cnt, aw_def_cnt, aw_mid_cnt, aw_att_cnt, hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list):
    
    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M")

    # Construct the file name with the current date and time
    file_name = f"match_reports/match_output_{hm_abbr}_v_{aw_abbr}_{current_datetime}.txt"
    
    with open(file_name, "w") as file:
        file.write(f"hm team abbr: {hm_abbr}\n")
        for item in hm_data_1:
            file.write(f"Pos: {item['pos']} - Player: {item['name']} - TS: {item['ts']} - Perf: {item['adj_perf']}\n")
        file.write(f" \n")
        file.write(f"aw team abbr: {aw_abbr}\n")
        for item in aw_data_1:
            file.write(f"Pos: {item['pos']} - Player: {item['name']} - TS: {item['ts']} - Perf: {item['adj_perf']}\n")
        file.write(f" \n")        
        file.write(f"Defense - hm: {hm_def_cnt} aw: {aw_def_cnt}\n")
        file.write(f"Midfield - hm: {hm_mid_cnt} aw: {aw_mid_cnt}\n") 
        file.write(f"Attack - hm: {hm_att_cnt} aw: {aw_att_cnt}\n")       
        file.write(f" \n")
        file.write(f"poss - hm: {hm_poss} aw: {aw_poss}\n")        
        file.write(f"cha - hm: {hm_cha} aw: {aw_cha}\n")
        file.write(f"On tar - hm: {hm_on_tar} - aw: {aw_on_tar}\n")  
        file.write(f"gls - hm: {hm_gls} - aw: {aw_gls}\n") 
        for i in goal_list:
            file.write(f"{i}\n") 
        file.write(f" \n")
        file.write(f"motm - hm: {hm_motm['name']} perf {hm_motm['adj_perf']} - aw: {aw_motm['name']} perf {aw_motm['adj_perf']}\n")

# Run all functions----------------------------------------------------------------

def main():
    # get player data from gsheet
    player_data = get_players()
    
    print_gk(player_data)
    print_def(player_data)
    print_mid(player_data)
    print_att(player_data)

    hm, hm_abbr,aw ,aw_abbr = select_team(player_data)
    
    # make player adj and calculate team values for the hm team
    hm_data_1, aw_data_1 = run_player_adj(hm, aw)

    # calculate team values for the teams
    hm_def_cnt, hm_mid_cnt, hm_att_cnt = calculate_team(hm_data_1)
    aw_def_cnt, aw_mid_cnt, aw_att_cnt = calculate_team(aw_data_1)

    # run the match
    hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list = run_match(hm_mid_cnt, aw_mid_cnt, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt, hm_data_1, aw_data_1)

    # output match data to a text file
    text_file_match_output(hm_abbr, aw_abbr, hm_data_1, aw_data_1, hm_def_cnt, hm_mid_cnt, hm_att_cnt, aw_def_cnt, aw_mid_cnt, aw_att_cnt, hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list)

main()
