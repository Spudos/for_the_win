from datetime import datetime

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