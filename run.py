from functions import import_team, player_adj, team_calc, match_calc, db_update
from datetime import datetime
import os
import sqlite3

class Match():
    def __init__(self,hm_abbr, aw_abbr, hm_def_cnt, hm_mid_cnt, hm_att_cnt, aw_def_cnt, aw_mid_cnt, aw_att_cnt, hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls):
        self.hm_abbr = hm_abbr
        self.aw_abbr = aw_abbr
        self.hm_def_cnt = hm_def_cnt
        self.hm_mid_cnt = hm_mid_cnt
        self.hm_att_cnt = hm_att_cnt
        self.aw_def_cnt = aw_def_cnt
        self.aw_mid_cnt = aw_mid_cnt
        self.aw_att_cnt = aw_att_cnt
        self.hm_cha = hm_cha
        self.aw_cha = aw_cha
        self.hm_on_tar = hm_on_tar
        self.aw_on_tar = aw_on_tar
        self.hm_poss = hm_poss
        self.aw_poss = aw_poss
        self.hm_gls = hm_gls
        self.aw_gls = aw_gls

def text_file_match_output(hm_abbr, aw_abbr, hm_data_1, aw_data_1, hm_def_cnt, hm_mid_cnt, hm_att_cnt, aw_def_cnt, aw_mid_cnt, aw_att_cnt, hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list):
    
    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M")

    # Construct the file name with the current date and time
    file_name = f"match_reports/match_output_{hm_abbr}_v_{aw_abbr}_{current_datetime}.txt"
    
    with open(file_name, "w") as file:
        file.write(f"hm team abbr: {hm_abbr}\n")
        for item in hm_data_1:
            file.write(f"Pos: {item[5]} - Player: {item[1]} - TS: {item[20]} - Perf: {item[21]}\n")
        file.write(f" \n")
        file.write(f"aw team abbr: {aw_abbr}\n")
        for item in aw_data_1:
            file.write(f"Pos: {item[5]} - Player: {item[1]} - TS: {item[20]} - Perf: {item[21]}\n")
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
        file.write(f"motm - hm: {hm_motm[1]} perf {hm_motm[21]} - aw: {aw_motm[1]} perf {aw_motm[21]}\n")

def main():
    # load the teams based on player selections
    hm, aw, hm_abbr, aw_abbr = import_team.player_load()
    
    # make player adj and calculate team values for the hm team
    hm_data = player_adj.calc_on_player_fitness(hm)
    hm_data_1 = player_adj.calc_on_player_random_perf(hm_data)
    hm_def_cnt, hm_mid_cnt, hm_att_cnt = team_calc.calculate_team(hm_data_1)
    
    # make player adj and calculate team values for the aw team
    aw_data = player_adj.calc_on_player_fitness(aw)
    aw_data_1 = player_adj.calc_on_player_random_perf(aw_data)
    aw_def_cnt, aw_mid_cnt, aw_att_cnt = team_calc.calculate_team(aw_data_1)

    # calculate the number of cha per team
    hm_cha, aw_cha = match_calc.calc_cha(hm_mid_cnt, aw_mid_cnt)

    # claculate how many cha are on tar
    hm_on_tar, aw_on_tar = match_calc.calc_on_tar(hm_cha, aw_cha, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt)

    # calculate the possesion stats
    hm_poss, aw_poss = match_calc.calc_poss(hm_cha, aw_cha)

    # calculate how many gls are scored
    hm_gls, aw_gls = match_calc.calc_gls(hm_on_tar, aw_on_tar, hm_def_cnt, hm_att_cnt, aw_att_cnt, aw_def_cnt)
    
    # calculate who made and scored goals
    goal_list = match_calc.goals(hm_gls, aw_gls, hm_data_1, aw_data_1)

    # calculate motm for each team
    hm_motm, aw_motm = match_calc.motm(hm_data_1, aw_data_1)

    # output match data to a text file
    text_file_match_output(hm_abbr, aw_abbr, hm_data_1, aw_data_1, hm_def_cnt, hm_mid_cnt, hm_att_cnt, aw_def_cnt, aw_mid_cnt, aw_att_cnt, hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list)

    db_update.update_player_stats(goal_list)

main()

