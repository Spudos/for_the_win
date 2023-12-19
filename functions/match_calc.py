import random

def calc_cha(mid_cnt_hm, mid_cnt_aw):
    print()
    print("Calculating the number of cha for each team.....")
    print()

    hm_mid = mid_cnt_hm
    aw_mid = mid_cnt_aw

    hm_random = random.randint(-5, 5)
    aw_random = random.randint(-5, 5)
    
    hm_cha = int((hm_mid / (hm_mid + aw_mid)) * 30) + hm_random
    aw_cha = int((aw_mid / (hm_mid + aw_mid)) * 30) + aw_random

    print()
    print("Team cha calculated")
    print(f"hm cha: ", hm_cha, " aw cha: ", aw_cha)
    print()

    return hm_cha, aw_cha

def calc_on_tar(hm_cha, aw_cha, att_cnt_hm, def_cnt_hm, att_cnt_aw, def_cnt_aw):
    print()
    print("Calculating the number of on tar for each team.....")
    print()
    
    hm_on_tar = int(hm_cha  * 0.75 * (att_cnt_hm / def_cnt_aw))
    aw_on_tar = int(aw_cha  * 0.75 * (att_cnt_aw / def_cnt_hm))
    
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

def calc_gls(hm_on_tar, aw_on_tar, def_cnt_hm, att_cnt_hm, def_cnt_aw, att_cnt_aw):
    print()
    print("Calculating gls scored for each team.....")
    print() 

    hm_gls = int(((att_cnt_hm / def_cnt_aw) * 0.7 * hm_on_tar)/2)
    aw_gls = int(((att_cnt_aw / def_cnt_hm) * 0.7 * aw_on_tar)/2)

    print()
    print("gls scored calculated")
    print("hm gls: ", hm_gls, " aw gls: ", aw_gls)
    print()

    return hm_gls, aw_gls