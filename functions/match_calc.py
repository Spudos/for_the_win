import random

def calc_cha(hm_mid_cnt, aw_mid_cnt):
    print()
    print("Calculating the number of cha for each team.....")
    print()

    hm_mid = hm_mid_cnt
    aw_mid = aw_mid_cnt

    hm_random = random.randint(-5, 5)
    aw_random = random.randint(-5, 5)
    
    hm_cha = int((hm_mid / (hm_mid + aw_mid)) * 30) + hm_random
    aw_cha = int((aw_mid / (hm_mid + aw_mid)) * 30) + aw_random

    print()
    print("Team cha calculated")
    print(f"hm cha: ", hm_cha, " aw cha: ", aw_cha)
    print()

    return hm_cha, aw_cha

def calc_on_tar(hm_cha, aw_cha, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt):
    print()
    print("Calculating the number of on tar for each team.....")
    print()
    
    hm_on_tar = int(hm_cha  * 0.75 * (hm_att_cnt / aw_def_cnt))
    aw_on_tar = int(aw_cha  * 0.75 * (aw_att_cnt / hm_def_cnt))
    
    print()
    print("On tar calculated")
    print("hm on tar: ", hm_on_tar, " aw on tar: ", aw_on_tar)
    print()

    return hm_on_tar, aw_on_tar

def calc_poss(hm_cha, aw_cha):
    print()
    print("Calculating poss for each team.....")
    print() 

    hm_poss = 0
    aw_poss = 0

    poss_random = random.randint(-10, 10)
    hm_poss = (int(hm_cha / (aw_cha + hm_cha) * 100) + poss_random)

    aw_poss = 100 - hm_poss

    print()
    print("poss calculated")
    print("hm poss: ", hm_poss, " aw poss: ", aw_poss)
    print()

    return hm_poss, aw_poss

def calc_gls(hm_on_tar, aw_on_tar, hm_def_cnt, hm_att_cnt, aw_def_cnt, aw_att_cnt):
    print()
    print("Calculating gls scored for each team.....")
    print() 

    hm_gls = int(((hm_att_cnt / aw_def_cnt) * 0.7 * hm_on_tar)/2)
    aw_gls = int(((aw_att_cnt / hm_def_cnt) * 0.7 * aw_on_tar)/2)

    print()
    print("gls scored calculated")
    print("hm gls: ", hm_gls, " aw gls: ", aw_gls)
    print()

    return hm_gls, aw_gls

def motm(hm_data_1, aw_data_1):
    print()
    print("Calculating motm for each team.....")
    print() 
    
    hm_motm = max(hm_data_1, key=lambda x: x[17])
    aw_motm = max(aw_data_1, key=lambda x: x[17])

    print()
    print("motm calculated")
    print(f"hm motm: {hm_motm[1]}  - perf {hm_motm[17]}  aw motm: {aw_motm[1]} - perf {aw_motm[17]}")
    print()

    return hm_motm, aw_motm

def generate_top_5(team_list, mid_adj, att_adj):    
    new_list = []
    for item in team_list:
        item = list(item)
        if item[5] == 'MID':
            item.append(item[17] + mid_adj)
            new_list.append(item)
        elif item[5] == 'ATT':
            item.append(item[17] + att_adj)
            new_list.append(item)
        else:
            item.append(item[17] + 0)
            new_list.append(item)    

    sort_hm_data_1 = sorted(new_list, key=lambda x: x[18], reverse=True)   
    top_5 = [player for player in sort_hm_data_1[:5] if player[5] != 'GK']
    
    return top_5
    
def goals(hm_gls, aw_gls, hm_data_1, aw_data_1):
    goal_list = []

    hm_ass = generate_top_5(hm_data_1, 30, 15)
    hm_scr = generate_top_5(hm_data_1, 15, 30)

    for i in range(hm_gls):
        hm_pl_ass = random.choice(hm_ass)
        hm_pl_gls = random.choice(hm_scr)

        # Check if the scorer is the same as the assister
        while hm_pl_gls[1] == hm_pl_ass[1]:
            hm_pl_gls = random.choice(hm_scr)

        print(f"hm goal {i + 1} assisted by {hm_pl_ass[1]} and scored by {hm_pl_gls[1]}")
        goal_info = {
            "goal_number": i + 1,
            "team": "hm",
            "assisted_by": hm_pl_ass[1],
            "scored_by": hm_pl_gls[1]
        }
        goal_list.append(goal_info)

    aw_ass = generate_top_5(aw_data_1, 30, 15)
    aw_scr = generate_top_5(aw_data_1, 15, 30)

    for i in range(aw_gls):
        aw_pl_ass = random.choice(aw_ass)
        aw_pl_gls = random.choice(aw_scr)

        # Check if the scorer is the same as the assister
        while aw_pl_gls[1] == aw_pl_ass[1]:
            aw_pl_gls = random.choice(aw_scr)

        print(f"aw goal {i + 1} assisted by {aw_pl_ass[1]} and scored by {aw_pl_gls[1]}")
        goal_info = {
            "goal_number": i + 1,
            "team": "aw",
            "assisted_by": aw_pl_ass[1],
            "scored_by": aw_pl_gls[1]
        }
        goal_list.append(goal_info)

    return goal_list
