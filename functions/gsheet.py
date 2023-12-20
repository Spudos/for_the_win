import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

def get_aw():
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('for_the_win')

    players_worksheet = SHEET.worksheet('players')

    aw = []
    for row in players_worksheet.get_all_records():
        if row.get('id') != '' and row.get('club') == 'ALV':
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
            print(player)
            player_data.append(player)
    return player_data
    
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


