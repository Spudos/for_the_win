from functions import import_team, player_adj, team_calc, match_calc, db_update, match_output, gsheet

def main():
    player_data = gsheet.get_players()
    hm, hm_abbr,aw ,aw_abbr = gsheet.select_team(player_data)
    
    # make player adj and calculate team values for the hm team
    hm_data_1, aw_data_1 = player_adj.run_player_adj(hm, aw)

    # calculate team values for the teams
    hm_def_cnt, hm_mid_cnt, hm_att_cnt = team_calc.calculate_team(hm_data_1)
    aw_def_cnt, aw_mid_cnt, aw_att_cnt = team_calc.calculate_team(aw_data_1)

    # run the match
    hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list = match_calc.run_match(hm_mid_cnt, aw_mid_cnt, hm_att_cnt, hm_def_cnt, aw_att_cnt, aw_def_cnt, hm_data_1, aw_data_1)

    # output match data to a text file
    match_output.text_file_match_output(hm_abbr, aw_abbr, hm_data_1, aw_data_1, hm_def_cnt, hm_mid_cnt, hm_att_cnt, aw_def_cnt, aw_mid_cnt, aw_att_cnt, hm_cha, aw_cha, hm_on_tar, aw_on_tar, hm_poss, aw_poss, hm_gls, aw_gls, hm_motm, aw_motm, goal_list)

main()
