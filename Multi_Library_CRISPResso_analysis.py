import time
import multiprocessing as mp
import numpy as np
import os
import platform


import Util
############### st env ###############
"""
::::::: Library_CRISPResso_analysis :::::::

D:/000_WORK/YuGooSang/20210527_CRISPResso2/

Workstation B206
/extdata1/GS/PE_byproduct/PECV_CRISPResso/

::::::: Library_CRISPResso_analysis :::::::
"""
WORK_DIR = os.getcwd() + "/"
SYSTEM_NM = platform.system()

CMD_FL = "../CRISPResso_command_210628_new.txt"

OU = './output/'
if not os.path.exists(OU):
    os.makedirs(OU)
TOTAL_CPU = mp.cpu_count()
MULTI_CNT = int(TOTAL_CPU*0.8)
############### en env ################


def run_cmd(cmd_list):
    print 'st : run_cmd'
    for cmd_arr in cmd_list:
        # tmp_cmd = cmd_arr[1].replace("\n", "").replace("\t", "") + " -o " + OU
        tmp_cmd = cmd_arr[1].replace("\n", "").replace("\t", "")
        os.system(tmp_cmd)
    print 'DONE : run_cmd'


def multi_Library_CRISPResso_analysis():
    os.system('clear')
    print 'st : test()'
    print 'this is not error, it\'s reminder'
    print 'check input text file and set it for linux. cmd [:set ff=unix]'
    print 'this is not error, it\'s reminder'
    val = raw_input('did you REALLY check input file??? then processes will start in 5 seconds [ y / N ]')
    if val.upper() == 'N':
        exit()
    for i in range(5, 0, -1):
        print str(i)
        time.sleep(1)
        if i == 1:
            print 'INITIATE!!!'
            time.sleep(3)
    util = Util.Utils()

    cmd_list = util.read_tb_txt_wout_header(CMD_FL)

    # divide data_list by MULTI_CNT
    splited_cmd_list = np.array_split(cmd_list, MULTI_CNT)

    print("platform.system() : ", SYSTEM_NM)
    print("total cpu_count : ", str(TOTAL_CPU))
    print("will use : ", str(MULTI_CNT))
    pool = mp.Pool(processes=MULTI_CNT)
    # # run command lines
    pool.map(run_cmd, splited_cmd_list)


if __name__ == '__main__':
    start_time = time.time()
    print("start >>>>>>>>>>>>>>>>>>")
    multi_Library_CRISPResso_analysis()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.time() - start_time))