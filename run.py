from functions import import_team, player_adj, team_calc, match_calc
from datetime import datetime
import os

        

def text_file_match_output(hm_abbr, aw_abbr, data_hm1, data_aw1, def_cnt_hm, mid_cnt_hm, att_cnt_hm, def_cnt_aw, mid_cnt_aw, att_cnt_aw, hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls):
    
    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Construct the file name with the current date and time
    file_name = f"match_reports/match_output_{hm_abbr}_v_{aw_abbr}_{current_datetime}.txt"
    
    with open(file_name, "w") as file:
        file.write(f"hm team abbr: {hm_abbr}\n")
        for item in data_hm1:
            file.write(f"Pos: {item[5]} - Player: {item[1]} - TS: {item[16]} - Perf: {item[17]}\n")
        file.write(f" \n")
        file.write(f"aw team abbr: {aw_abbr}\n")
        for item in data_aw1:
            file.write(f"Pos: {item[5]} - Player: {item[1]} - TS: {item[16]} - Perf: {item[17]}\n")
        file.write(f" \n")        
        file.write(f"Defense - hm: {def_cnt_hm} aw: {def_cnt_aw}\n")
        file.write(f"Midfield - hm: {mid_cnt_hm} aw: {mid_cnt_aw}\n") 
        file.write(f"Attack - hm: {att_cnt_hm} aw: {att_cnt_aw}\n")       
        file.write(f" \n")
        file.write(f"poss - hm: {hm_poss} aw: {aw_poss}\n")        
        file.write(f"cha - hm: {hm_cha} aw: {aw_cha}\n")
        file.write(f"On tar - hm: {hm_on_tar} - aw: {aw_on_tar}\n")  
        file.write(f"gls - hm: {hm_gls} - aw: {aw_gls}\n")  

def main():
    # load the teams based on player selections
    hm, aw, hm_abbr, aw_abbr = import_team.player_load()
    
    # make player adj and calculate team values for the hm team
    data_hm = player_adj.calc_on_player_fitness(hm)
    data_hm1 = player_adj.calc_on_player_random_perf(data_hm)
    def_cnt_hm, mid_cnt_hm, att_cnt_hm = team_calc.calculate_team(data_hm1)
    
    # make player adj and calculate team values for the aw team
    data_aw = player_adj.calc_on_player_fitness(aw)
    data_aw1 = player_adj.calc_on_player_random_perf(data_aw)
    def_cnt_aw, mid_cnt_aw, att_cnt_aw = team_calc.calculate_team(data_aw1)

    # calculate the number of cha per team
    hm_cha, aw_cha = match_calc.calc_cha(mid_cnt_hm, mid_cnt_aw)

    # claculate how many cha are on tar
    hm_on_tar, aw_on_tar = match_calc.calc_on_tar(hm_cha, aw_cha, att_cnt_hm, def_cnt_hm, att_cnt_aw, def_cnt_aw)

    # calculate the possesion stats
    hm_poss, aw_poss = match_calc.calc_poss(hm_cha, aw_cha)

    # calculate how many gls are scored
    hm_gls, aw_gls = match_calc.calc_gls(hm_on_tar, aw_on_tar, def_cnt_hm, att_cnt_hm, att_cnt_aw, def_cnt_aw)
    
    # output match data to a text file
    text_file_match_output(hm_abbr, aw_abbr, data_hm1, data_aw1, def_cnt_hm, mid_cnt_hm, att_cnt_hm, def_cnt_aw, mid_cnt_aw, att_cnt_aw, hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls)

main()

