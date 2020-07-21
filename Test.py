import time
import os
import multiprocessing as mp
from multiprocessing import Process
import psutil
import numpy as np


import Util
import LogicPrep
import Logic
import run_CRISPResso2
############### start to set env ###############
WORK_DIR = os.getcwd() + "/"
INPUT_BARCD = "input/pre_cancer_barcode.txt"
INPUT_FASTQ = "input/fastq_pairs.txt"

TOTAL_CPU = mp.cpu_count()
# MULTI_CNT = int(TOTAL_CPU*0.5)
MULTI_CNT = 5
PROCESS_NAME = "python"
IS_RUNNING = 0
############### end setting env ################

def multi_processing_plan_B():
    util = Util.Utils()
    for idx in range(10):
        util.check_limit_cpu_test(MULTI_CNT, PROCESS_NAME)
        proc = Process(target=test)
        proc.start()
        print "idx >>>>>>>>>>>>>>>>>>>>>> ", str(idx)


def test():
    print "test is running ++++++++++++++++++++++++++++++++++"
    time.sleep(5)
    print "test is done --------------------------------------"
    # print "::::::::::::::::"

def count_Alleles_frequency_table():
    util = Util.Utils()
    read_list = util.read_tb_txt_wout_header("D:/000_WORK/JangHyeWon_KimMinYung/20200703/Alleles_frequency_table.txt")

    cnt = 0
    for tmp_arr in read_list:
        cnt += int(tmp_arr[7])

    print "total_read : ", cnt


if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start >>>>>>>>>>>>>>>>>>")
    # multi_processing_plan_B()
    count_Alleles_frequency_table()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))
