import gspread, random, os
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# General functions ----------------------------------------------------------

def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def press_any_key_to_continue():
    input(Fore.BLUE + "Press any key to continue...\n" + Style.RESET_ALL)

def press_any_key_for_outcome():
    input(Fore.BLUE + "Press any key to see the match result...\n" + Style.RESET_ALL)

def print_centered(text):
    terminal_width = 80
    centered_text = text.center(terminal_width)
    print(centered_text)

# Header and instructions print ------------------------------------------------

def print_for_the_win():
    block_letters = {
        'A': ['  **  ', ' *  * ', ' *****', '*    *', '*    *'],
        'B': ['****  ', '*   * ', '***** ', '*    *', '****  '],
        'C': [' **** ', '*    *', '*     ', '*    *', ' **** '],
        'D': ['****  ', '*   * ', '*    *', '*   * ', '****  '],
        'E': ['***** ', '*     ', '****  ', '*     ', '***** '],
        'F': ['***** ', '*     ', '****  ', '*     ', '*     '],
        'G': [' **** ', '*     ', '*  ***', '*    *', ' **** '],
        'H': ['*    *', '*    *', '******', '*    *', '*    *'],
        'I': ['***** ', '  *   ', '  *   ', '  *   ', '***** '],
        'J': [' *****', '    * ', '    * ', '*   * ', ' ***  '],
        'K': ['*   * ', '*  *  ', '***   ', '*  *  ', '*   * '],
        'L': ['*     ', '*     ', '*     ', '*     ', '***** '],
        'M': ['*    *', '**  **', '* ** *', '*    *', '*    *'],
        'N': ['*    *', '**   *', '* *  *', '*  * *', '*   **'],
        'O': [' **** ', '*    *', '*    *', '*    *', ' **** '],
        'P': ['***** ', '*    *', '***** ', '*     ', '*     '],
        'Q': [' **** ', '*    *', '*  * *', '*   **', ' **** '],
        'R': ['***** ', '*    *', '****  ', '*   * ', '*    *'],
        'S': [' **** ', '*     ', ' ***  ', '    * ', '****  '],
        'T': ['***** ', '  *   ', '  *   ', '  *   ', '  *   '],
        'U': ['*    *', '*    *', '*    *', '*    *', ' **** '],
        'V': ['*    *', '*    *', ' *  * ', ' *  * ', '  **  '],
        'W': ['*    *', '*    *', '* ** *', '**  **', '*    *'],
        'X': ['*    *', ' *  * ', '  **  ', ' *  * ', '*    *'],
        'Y': ['*    *', ' *  * ', '  **  ', '  *   ', '  *   '],
        'Z': ['***** ', '   *  ', '  *   ', ' *    ', '***** '],
        ' ': ['      ', '      ', '      ', '      ', '      '],
    }

    print()

    lines = ['', '', '', '', '']
    text = 'for the win'
    for char in text.upper():
        if char in block_letters:
            letter = block_letters[char]
            for i in range(len(lines)):
                lines[i] += f"{Fore.YELLOW}{letter[i]}{Style.RESET_ALL}" + ' ' * 1  # Add 1 spaces between letters
        else:
            for i in range(len(lines)):
                lines[i] += ' ' * 7  # Add 7 spaces for unknown characters

    for line in lines:
        print_centered(line)
    
    print()
    print_centered(Fore.RED + '============================================================================' + Style.RESET_ALL)
    print_centered(Fore.GREEN + 'The football management game where you pick the team to take on the mighty')
    print_centered('Liverpool FC.')
    print()
    print_centered('In the team selection screen, you will be able to select 11 players from a')
    print_centered('list of those that are available.  Simply input the id for each player when')
    print_centered('and the match engine will calculate the outcome by using the comlex hidden')
    print_centered('stats for each player.')
    print_centered('The only rules are that you cannot pick a player twice and you must pick')
    print_centered('11 players.  The formation will be determined based on what players you pick.')
    print_centered('You will then be able to see the match stats and finally, the outcome of the')
    print_centered('game.')
    print_centered('Good luck, I hope you enjoy "For the Win!"' + Style.RESET_ALL)
    print()
    press_any_key_to_continue()

    clear_terminal()

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
            aw.append(player)

    aw_abbr = "Liverpool FC"

    return aw, aw_abbr

def get_players():
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('for_the_win')

    players_worksheet = SHEET.worksheet('players')

    player_data = []
    for row in players_worksheet.get_all_records():
        if row.get('id') != '' and row.get('club') != 'LIV':
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
    print(Fore.RED + "=========== AVAILABLE PLAYERS ===========" + Style.RESET_ALL)
    print(Fore.RED + "Goalkeepers------------------------------" + Style.RESET_ALL)
    for player in player:
        if player['pos'] == "GK":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} skill")
   
def print_def(player): 
    print(Fore.RED + "Defenders--------------------------------" + Style.RESET_ALL)
    for player in player:
        if player['pos'] == "DEF":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} skill")
    
def print_mid(player):    
    print(Fore.RED + "Midfielders-------------------------------" + Style.RESET_ALL)
    for player in player:    
        if player['pos'] == "MID":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} skill")
    
def print_att(player):    
    print(Fore.RED + "Attackers---------------------------------" + Style.RESET_ALL)
    for player in player:    
        if player['pos'] == "ATT":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} skill")
  
def select_team(player_data): 
    print(Fore.RED + "============= TEAM SELECTION =============" + Style.RESET_ALL)
    
    hm = []
    selected_ids = set()
    for i in range(1, 12):
        while True:
            try:
                player_id = int(input(f"Player {i}: Select the ID of a player:\n"))
                if player_id < 1 or player_id > len(player_data):
                    print("Invalid player ID. Please enter a valid ID.")
                elif player_id in selected_ids:
                    print("Player already selected. Please choose a different player.")
                else:
                    selected_ids.add(player_id)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid ID.")
        
        team = player_data[player_id - 1]
        hm.append(team)

        clear_terminal()
        
        print_gk(player_data)
        print_def(player_data)
        print_mid(player_data)
        print_att(player_data)
        print(Fore.RED + "============= TEAM SELECTION =============" + Style.RESET_ALL)

    hm_abbr = "Your team"

    return hm, hm_abbr


def print_team_selected(hm):
    print() 
    print(Fore.YELLOW + "This is the team you selected ------------" )
    for player in hm:
        name = player['name']
        formatted_name = f"{name:<20}"
        print(f"{formatted_name} : {player['pos']} : {player['ts']}")
    print("------------------------------------------" + Style.RESET_ALL)

def print_away_team():
    aw, aw_abbr = get_aw()

    print() 
    print(Fore.RED + "This is the Liverpool team you are playing" )
    for player in aw:
        name = player['name']
        formatted_name = f"{name:<20}"
        print(f"{formatted_name} : {player['pos']} : {player['ts']}")
    print("------------------------------------------" + Style.RESET_ALL)

    return aw, aw_abbr


# Perform player adjustments----------------------------------------------------------------

def calc_on_player_fitness(data):
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

def calculate_team(data, name):
    print(Fore.BLUE + "============== MATCH PLAYED =============="  + Style.RESET_ALL)
    print()
    print(Fore.RED + f"{name}"  + Style.RESET_ALL)
    print(Fore.RED + "Performance ratings ----------------------"  + Style.RESET_ALL)
    
    for i in data:
        name = i['name']
        formatted_name = f"{name:<20}"
        print(f"{formatted_name} {i['pos']} {i['adj_perf']}")

    def_count = 0
    mid_count = 0
    att_count = 0

    for record in data:
        adj_perf = record['adj_perf']
        pos = record['pos']
     
        if pos == "GK":
            def_count += adj_perf
        elif pos == "DEF":
            def_count += adj_perf       
        elif pos == "MID":
            mid_count += adj_perf
        elif pos == "ATT":
            att_count += adj_perf
    
    print()
    print(Fore.RED + "------------------------------------------" + Style.RESET_ALL)
    print("Team values calculated")
    print("Defence: ", def_count, " Midfield: ", mid_count, " Attack: ", att_count)
    print(Fore.RED + "==========================================" + Style.RESET_ALL)
    
    press_any_key_to_continue()
    clear_terminal()

    return def_count, mid_count, att_count

# Run the match----------------------------------------------------------------

def calc_cha(hm_mid_cnt, aw_mid_cnt):
    print()
    print(Fore.BLUE + "============== MATCH STATS ==============="  + Style.RESET_ALL)
    hm_mid = hm_mid_cnt
    aw_mid = aw_mid_cnt

    hm_random = random.randint(-5, 5)
    aw_random = random.randint(-5, 5)
    
    hm_cha = int((hm_mid / (hm_mid + aw_mid)) * 30) + hm_random
    aw_cha = int((aw_mid / (hm_mid + aw_mid)) * 30) + aw_random

    print()
    print(Fore.GREEN + "Chances created----------" + Style.RESET_ALL)
    print(f"Home: ", hm_cha, " Away: ", aw_cha)

    return hm_cha, aw_cha

def calc_on_tar(hm_cha, aw_cha, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt):
    
    hm_on_tar = int(hm_cha  * 0.75 * (hm_att_cnt / aw_def_cnt))
    aw_on_tar = int(aw_cha  * 0.75 * (aw_att_cnt / hm_def_cnt))
    
    print()
    print(Fore.GREEN + "Chances on target--------------------------" + Style.RESET_ALL)
    print("Home: ", hm_on_tar, " Away: ", aw_on_tar)

    return hm_on_tar, aw_on_tar

def calc_poss(hm_cha, aw_cha):

    hm_poss = 0
    aw_poss = 0

    poss_random = random.randint(-10, 10)
    hm_poss = (int(hm_cha / (aw_cha + hm_cha) * 100) + poss_random)

    aw_poss = 100 - hm_poss

    print()
    print(Fore.GREEN + "Possession--------------------------------" + Style.RESET_ALL)
    print("Home: ", hm_poss, " Away: ", aw_poss)

    return hm_poss, aw_poss

def calc_gls(hm_on_tar, aw_on_tar, hm_def_cnt, hm_att_cnt, aw_def_cnt, aw_att_cnt):
    press_any_key_for_outcome()
    hm_gls = int(((hm_att_cnt / aw_def_cnt) * 0.7 * hm_on_tar)/2)
    aw_gls = int(((aw_att_cnt / hm_def_cnt) * 0.7 * aw_on_tar)/2)

    print()
    print(Fore.GREEN + "Goals scored------------------------------" + Style.RESET_ALL)
    print("Home: ", hm_gls, " Away: ", aw_gls)

    return hm_gls, aw_gls

def motm(hm_data_1, aw_data_1):
    
    hm_motm = max(hm_data_1, key=lambda x: x['adj_perf'])
    aw_motm = max(aw_data_1, key=lambda x: x['adj_perf'])

    print()
    print(Fore.GREEN + "Man of the Match---------------------------" + Style.RESET_ALL)
    print(f"Home: {hm_motm['name']}  - perf {hm_motm['adj_perf']}  Away: {aw_motm['name']} - perf {aw_motm['adj_perf']}")
    print()

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
        "team": team_name,
        "scored_by": player_score['name'],
        "assisted_by": player_assist['name']
    }
    return goal_info


def generate_goals(team_gls, team_data, team_name):
    goal_list = []
    team_ass = generate_top_5(team_data, 30, 15)
    team_scr = generate_top_5(team_data, 15, 30)

    for i in range(team_gls):
        pl_ass = random.choice(team_ass)
        pl_gls = random.choice(team_scr)

        while pl_gls['name'] == pl_ass['name']:
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
    calc_poss(hm_cha, aw_cha)

    # calculate how many gls are scored
    hm_gls, aw_gls = calc_gls(hm_on_tar, aw_on_tar, hm_def_cnt, hm_att_cnt, aw_att_cnt, aw_def_cnt)
    
    # calculate who made and scored goals
    goals(hm_gls, aw_gls, hm_data_1, aw_data_1)

    # calculate motm for each team
    motm(hm_data_1, aw_data_1)

# Run all functions================================================================

def main():
    clear_terminal()

    print_for_the_win()


    # get player data from gsheet and print them to screen
    player_data = get_players()
    print_gk(player_data)
    print_def(player_data)
    print_mid(player_data)
    print_att(player_data)

    hm, hm_abbr = select_team(player_data)

    # team selection
    clear_terminal()
    print_team_selected(hm)
    press_any_key_to_continue()
    clear_terminal()
    aw, aw_abbr = print_away_team()

    # move to player and team calc phase
    press_any_key_to_continue()
    clear_terminal()

    # make player adj and calculate team values for the hm team
    hm_data_1, aw_data_1 = run_player_adj(hm, aw)

    # calculate team values for the teams
    hm_def_cnt, hm_mid_cnt, hm_att_cnt = calculate_team(hm_data_1, hm_abbr)
    aw_def_cnt, aw_mid_cnt, aw_att_cnt = calculate_team(aw_data_1, aw_abbr)

    # run the match
    run_match(hm_mid_cnt, aw_mid_cnt, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt, hm_data_1, aw_data_1)

main()
