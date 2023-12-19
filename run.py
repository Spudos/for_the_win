from functions import import_team, player_adj, team_calc, match_calc, db_update, match_output
import os, sqlite3

def main():
    # load the teams based on player selections
    hm, aw, hm_abbr, aw_abbr = import_team.player_load()
    
    # make player adj and calculate team values for the hm team
    hm_data_1, aw_data_1 = player_adj.run_player_adj(hm, aw)

    # calculate team values for the teams
    hm_def_cnt, hm_mid_cnt, hm_att_cnt = team_calc.calculate_team(hm_data_1)
    aw_def_cnt, aw_mid_cnt, aw_att_cnt = team_calc.calculate_team(aw_data_1)

    # run the match
    hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list = match_calc.run_match(hm_mid_cnt, aw_mid_cnt, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt, hm_data_1, aw_data_1)

    # output match data to a text file
    match_output.text_file_match_output(hm_abbr, aw_abbr, hm_data_1, aw_data_1, hm_def_cnt, hm_mid_cnt, hm_att_cnt, aw_def_cnt, aw_mid_cnt, aw_att_cnt, hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list)

    # update player stats in the db
    db_update.update_player_stats(goal_list, hm_data_1, aw_data_1)

main()
