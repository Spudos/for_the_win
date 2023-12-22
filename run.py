import gspread
import random
import os
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


# General functions ----------------------------------------------------------


def clear_terminal():
    """
    clear the terminal as required
    """
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def press_any_key_to_continue():
    """
    used to introduce a natural delay into the flow of the app
    """
    input(Fore.BLUE + "Press any key to continue...\n" +
          Style.RESET_ALL)


def press_any_key_for_outcome():
    """
    variation on the above but with different messaging
    """
    input(Fore.BLUE + "Press any key to see the match result...\n" +
          Style.RESET_ALL)


def print_centered(text):
    """
    center the text where used, primarily for the welcome string
    """
    terminal_width = 80
    centered_text = text.center(terminal_width)
    print(centered_text)


# Header and instructions print -----------------------------------------------


def print_for_the_win():
    """
    print the header for the game
    """
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
                lines[i] += f"{Fore.YELLOW}{letter[i]}{Style.RESET_ALL}" + ' '
        else:
            for i in range(len(lines)):
                lines[i] += ' ' * 7  # Add 7 spaces for unknown characters

    for line in lines:
        print_centered(line)


def print_instructions():
    """
    print the instructions for the game
    """
    print()
    print_centered(Fore.RED + '=' * 70 + ' v1.82' + Style.RESET_ALL)
    print_centered(Fore.GREEN + 'The football management game where you pick')
    print_centered('the team to take on the mighty Liverpool FC.')
    print()
    print_centered('In the team selection screen, you will be able to select')
    print_centered('11 players from a list of those that are available.')
    print_centered('Simply input the id for each player when and the match')
    print_centered('engine will calculate the outcome by using the comlex')
    print_centered('hidden stats for each player.')
    print_centered('The only rules are that you cannot pick a player twice')
    print_centered('and you must pick 11 players.  The formation will be')
    print_centered('determined based on what players you pick.  You will')
    print_centered('then be able to see the match outcome.')
    print_centered('I hope you enjoy "For the Win!"' + Style.RESET_ALL)
    print()
    press_any_key_to_continue()

    clear_terminal()


# Login and authenticate user -------------------------------------------------


def login(username, password):
    """
    gets the username and password from the
    google sheet and returns true or false depending
    on what the user has entered
    """
    try:
        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open('for_the_win')

        users = SHEET.worksheet('users')

        data = users.get_all_records(empty2zero=False)
        for row in data:
            if row['username'] == username and row['password'] == password:
                return True
        return False
    except Exception as e:
        print(f"An error occurred during login: {str(e)}")
        return False


def get_login_from_user():
    """
    asks if you have login details and if not allows
    you to save some.  validates response and ensures
    both are enetered on login
    """
    while True:
        print()
        print_centered(Fore.RED + '=' * 79 + Style.RESET_ALL)
        has_login_details = input("Do you have login details? (y/n):\n")
        has_login_details = has_login_details.lower()
        if has_login_details == "y":
            username = input("Enter your username:\n")
            password = input("Enter your password:\n")
            if username and password:
                try:
                    if login(username, password):
                        print("Login successful!")
                        break
                    else:
                        print("Invalid username or password.")
                except Exception as e:
                    print(f"An error occurred during login: {str(e)}")
            else:
                print("Please enter both a username and password.")
        elif has_login_details == "n":
            new_username = input("Enter a new username:\n")
            new_password = input("Enter a new password (letters only):\n")
            try:
                add_user(new_username, new_password)
                print("Login details saved successfully!")
            except Exception as e:
                print(f"An error occurred while saving details: {str(e)}")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def add_user(username, password):
    """
    saves the new user details in the sheet
    """

    try:
        CREDS = Credentials.from_service_account_file('creds.json')
        SCOPED_CREDS = CREDS.with_scopes(SCOPE)
        GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
        SHEET = GSPREAD_CLIENT.open('for_the_win')

        users = SHEET.worksheet('users')

        users.append_row([username, password])
    except Exception as e:
        print(f"An error occurred while adding a new user: {str(e)}")


# Load Teams ------------------------------------------------------------------


def get_aw():
    """
    access the gsheet and look for any rows where
    the player is LIV and the row is not blank.
    set the aw variable as the team selected above
    and ser the team name using aw_abbr
    """

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
    """
    Look up players from the gsheet selecting
    all player who are not from club LIV and
    where the row isnt blank
    """
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
    """
    print all GKs
    """
    print(Fore.RED + "=========== AVAILABLE PLAYERS ===========" +
          Style.RESET_ALL)
    print(Fore.RED + "Goalkeepers" + '-' * 30 + Style.RESET_ALL)
    for player in player:
        if player['pos'] == "GK":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} Skl")


def print_def(player):
    """
    print all DEFs
    """
    print(Fore.RED + "Defenders" + '-' * 32 + Style.RESET_ALL)
    for player in player:
        if player['pos'] == "DEF":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} Skl")


def print_mid(player):
    """
    print all MIDs
    """
    print(Fore.RED + "Midfielders" + '-' * 31 + Style.RESET_ALL)
    for player in player:
        if player['pos'] == "MID":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} Skl")


def print_att(player):
    """
    print all ATTs
    """
    print(Fore.RED + "Attackers" + '-' * 33 + Style.RESET_ALL)
    for player in player:
        if player['pos'] == "ATT":
            print(f"Id: {player['id']}, {player['name']}, {player['ts']} Skl")


def select_team(player_data):
    """
    from the player_data selected in get_players()
    give the user the chance to select what players
    they want in their team.  includes validation
    for only pisking a player once, only putting
    in valid ids and picking 11 players.  The view
    is refreshed each time to utilise the terminal
    size
    """
    print(Fore.RED + "============= TEAM SELECTION =============" +
          Style.RESET_ALL)

    hm = []
    selected_ids = set()
    for i in range(1, 12):
        while True:
            try:
                player_id = int(input(f"Player {i}: Select an ID:\n"))
                if player_id < 1 or player_id > len(player_data):
                    print("Invalid player ID.")
                elif player_id in selected_ids:
                    print("Player already selected.")
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
        print(Fore.RED + "============= TEAM SELECTION =============" +
              Style.RESET_ALL)

    hm_abbr = "Your team"

    return hm, hm_abbr


def print_team_selected(hm):
    """
    output the user selected team
    """
    print()
    print(Fore.YELLOW + "This is the team you selected ------------")
    for player in hm:
        name = player['name']
        formatted_name = f"{name:<20}"
        print(f"{formatted_name} : {player['pos']} : {player['ts']}")
    print("------------------------------------------" + Style.RESET_ALL)


def print_away_team():
    """
    output the computer selected team
    """
    aw, aw_abbr = get_aw()

    print()
    print(Fore.RED + "This is the Liverpool team you are playing")
    for player in aw:
        name = player['name']
        formatted_name = f"{name:<20}"
        print(f"{formatted_name} : {player['pos']} : {player['ts']}")
    print("------------------------------------------" + Style.RESET_ALL)

    return aw, aw_abbr


# Perform player adjustments---------------------------------------------------


def calc_on_player_fitness(data):
    """
    load individual player skills and calculate
    a base performance figure based on what skills
    are most important for that position.  fitness
    also taken into account but the program does
    not adjust fitness.  this would be in V2
    """
    for record in data:
        pos = record['pos']
        fit = record['fit']
        if pos == "GK":
            perf = int(((record['pa'] + record['co'] + record['sh']) +
                        (record['he'] + record['st'] + record['tk']) +
                        (record['ru'] + record['fl']) +
                        (record['cr']) / 2) * fit / 100)
        elif pos == "DEF":
            perf = int(((record['co'] + record['tk'] + record['ru']) +
                        (record['he'] + record['st'] + record['pa']) +
                        (record['sh'] + record['fl']) +
                        (record['cr']) / 2) * fit / 100)
        elif pos == "MID":
            perf = int(((record['pa'] + record['co'] + record['ru']) +
                        (record['fl'] + record['cr']) + (record['tk']) +
                        (record['sh'] + record['he']) +
                        (record['st']) / 2) * fit / 100)
        else:
            perf = int(((record['co'] + record['ru'] + record['sh']) +
                        (record['fl'] + record['st']) + (record['pa']) +
                        (record['tk'] + record['he']) +
                        (record['cr']) / 2) * fit / 100)

        record['perf'] = perf

    return data


def calc_on_player_random_perf(data):
    """
    to add a random element to outcomes a
    players rating is adjusted by +/- 20
    """
    for i in data:
        perf = i['perf']
        random_adjustment = random.randint(-20, 20)
        i['adj_perf'] = int(perf + random_adjustment)

    return data


def run_player_adj(hm, aw):
    """
    Summary function to run the player calcs
    above to that not everythign is included
    in the main function
    """
    hm_data = calc_on_player_fitness(hm)
    hm_data_1 = calc_on_player_random_perf(hm_data)

    aw_data = calc_on_player_fitness(aw)
    aw_data_1 = calc_on_player_random_perf(aw_data)

    return hm_data_1, aw_data_1


# Calculate team totals-------------------------------------------------------


def calculate_team(data, name):
    """
    so that match calcs can be done the player
    info is amalgamated into def/mid/att.  the
    two teams will use this to make comparisons.
    this also lists the player performances which
    are the base values plus the random element
    """
    print(Fore.BLUE + "============== MATCH PLAYED ==============" +
          Style.RESET_ALL)
    print()
    print(Fore.RED + f"{name}" + Style.RESET_ALL)
    print(Fore.RED + "Performance ratings ----------------------" +
          Style.RESET_ALL)

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
    print(Fore.RED + "------------------------------------------" +
          Style.RESET_ALL)
    print("Team values calculated")
    print("Def: ", def_count, " Midf: ", mid_count, " Att: ", att_count)
    print(Fore.RED + "==========================================" +
          Style.RESET_ALL)

    press_any_key_to_continue()
    clear_terminal()

    return def_count, mid_count, att_count


# Run the match----------------------------------------------------------------


def calc_cha(hm_mid_cnt, aw_mid_cnt):
    """
    using the team values the mids are compared with
    the team with the highest mid creating more chances
    up to a maximum of 30.  a randomelement of +/- 5
    is the added to both teams to keep it more unpredictable
    """
    print()
    print(Fore.BLUE + "============== MATCH STATS ===============" +
          Style.RESET_ALL)
    hm_mid = hm_mid_cnt
    aw_mid = aw_mid_cnt

    hm_random = random.randint(-5, 5)
    aw_random = random.randint(-5, 5)

    hm_cha = int((hm_mid / (hm_mid + aw_mid)) * 30) + hm_random
    aw_cha = int((aw_mid / (hm_mid + aw_mid)) * 30) + aw_random

    print()
    print(Fore.GREEN + "Chances created---------------------------" +
          Style.RESET_ALL)
    print(f"Home: ", hm_cha, " Away: ", aw_cha)

    return hm_cha, aw_cha


def calc_on_tar(hm_cha, aw_cha, hm_att_cnt, hm_def_cnt,
                aw_att_cnt, aw_def_cnt):
    """
    a teams att is compared to the oppositions def
    to decide how many of the chances are on target.
    the higher the difference the more chances a team
    will get
    """
    hm_on_tar = int(hm_cha * 0.75 * (hm_att_cnt / aw_def_cnt))
    aw_on_tar = int(aw_cha * 0.75 * (aw_att_cnt / hm_def_cnt))

    print()
    print(Fore.GREEN + "Chances on target-------------------------" +
          Style.RESET_ALL)
    print("Home: ", hm_on_tar, " Away: ", aw_on_tar)

    return hm_on_tar, aw_on_tar


def calc_poss(hm_cha, aw_cha):
    """
    possesion is calculated using the number of
    chances created and applying a +/- 10 value
    """
    hm_poss = 0
    aw_poss = 0

    poss_random = random.randint(-10, 10)
    hm_poss = (int(hm_cha / (aw_cha + hm_cha) * 100) + poss_random)

    aw_poss = 100 - hm_poss

    print()
    print(Fore.GREEN + "Possession--------------------------------" +
          Style.RESET_ALL)
    print("Home: ", hm_poss, " Away: ", aw_poss)

    return hm_poss, aw_poss


def calc_gls(hm_on_tar, aw_on_tar, hm_def_cnt, hm_att_cnt,
             aw_def_cnt, aw_att_cnt):
    """
    att v def is taken into account to decide
    how many of the on target chances are converted
    into goals.  goals are adjusted by .7 then /2
    after play testing revealed this is the best
    way to get realistic outcomes
    """
    press_any_key_for_outcome()
    hm_gls = int(((hm_att_cnt / aw_def_cnt) * 0.7 * hm_on_tar)/2)
    aw_gls = int(((aw_att_cnt / hm_def_cnt) * 0.7 * aw_on_tar)/2)

    print()
    print(Fore.GREEN + "Goals scored------------------------------" +
          Style.RESET_ALL)
    print("Home: ", hm_gls, " Away: ", aw_gls)

    return hm_gls, aw_gls


def motm(hm_data_1, aw_data_1):
    """
    the player for each team with the highest
    perf is selected as motm
    """
    hm_motm = max(hm_data_1, key=lambda x: x['adj_perf'])
    aw_motm = max(aw_data_1, key=lambda x: x['adj_perf'])

    print()
    print(Fore.GREEN + "Man of the Match---------------------------" +
          Style.RESET_ALL)
    print(f"Home: {hm_motm['name']} - perf {hm_motm['adj_perf']}"
          f"  Away: {aw_motm['name']} - perf {aw_motm['adj_perf']}")

    print()

    return hm_motm, aw_motm


def generate_top_5(team_list, mid_adj, att_adj):
    """
    to decide on assists and scorers the top 5
    performing players from each side are slected
    and put in a list.  GKs are excluded.  for
    assists there is an a big adjustment to perf
    and for att a smaller adj and the reverse
    for goals.  this is to make mids more likely
    to be selected for assists and atts more
    likely to be selected for goals
    """
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
    """
    output goal info
    """
    goal_info = {
        "team": team_name,
        "scored_by": player_score['name'],
        "assisted_by": player_assist['name']
    }
    return goal_info


def generate_goals(team_gls, team_data, team_name):
    """
    pass the info in the top_5 calculator the select
    a assist and scorer for every goal based on
    random selection from the 5 best players. one
    player cannot score and assist the same goal as
    per the while loop
    """
    goal_list = []
    team_ass = generate_top_5(team_data, 30, 15)
    team_scr = generate_top_5(team_data, 15, 30)

    for i in range(team_gls):
        pl_ass = random.choice(team_ass)
        pl_gls = random.choice(team_scr)

        while pl_gls['name'] == pl_ass['name']:
            pl_gls = random.choice(team_scr)

        print(f"{team_name} goal {i + 1} assisted by {pl_ass['name']}"
              f" and scored by {pl_gls['name']}")
        goal_info = generate_goal_info(pl_ass, pl_gls, team_name)
        goal_list.append(goal_info)

    return goal_list


def goals(hm_gls, aw_gls, hm_data_1, aw_data_1):
    """
    pass the info into the goal info generator
    """
    hm_goals = generate_goals(hm_gls, hm_data_1, "Home")
    aw_goals = generate_goals(aw_gls, aw_data_1, "Away")
    return hm_goals + aw_goals


def run_match(hm_mid_cnt, aw_mid_cnt, hm_att_cnt, hm_def_cnt,
              aw_att_cnt, aw_def_cnt, hm_data_1, aw_data_1):
    hm_cha, aw_cha = calc_cha(hm_mid_cnt, aw_mid_cnt)
    """
    summary function to run all of the match calc
    functions.  this mehtod makes it easier to
    see the distinct modules in the code without
    importing other files
    """

    # claculate how many cha are on tar
    hm_on_tar, aw_on_tar = calc_on_tar(hm_cha, aw_cha, hm_att_cnt,
                                       hm_def_cnt, aw_att_cnt, aw_def_cnt)

    # calculate the possesion stats
    calc_poss(hm_cha, aw_cha)

    # calculate how many gls are scored
    hm_gls, aw_gls = calc_gls(hm_on_tar, aw_on_tar, hm_def_cnt,
                              hm_att_cnt, aw_att_cnt, aw_def_cnt)

    # calculate who made and scored goals
    goals(hm_gls, aw_gls, hm_data_1, aw_data_1)

    # calculate motm for each team
    motm(hm_data_1, aw_data_1)


# Run all functions============================================================


def main():
    """
    run all functions required for the game
    """
    clear_terminal()

    print_for_the_win()
    print_instructions()

    clear_terminal()
    print_for_the_win()
    get_login_from_user()

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
    run_match(hm_mid_cnt, aw_mid_cnt, hm_att_cnt, hm_def_cnt,
              aw_att_cnt, aw_def_cnt, hm_data_1, aw_data_1)


main()
