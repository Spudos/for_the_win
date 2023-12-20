import random

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