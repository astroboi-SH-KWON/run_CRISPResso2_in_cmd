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
# brcd1(9bp) + (0~3bp) + AGTACGTACGAGTC + brcd2(9bp) + GTACTCGCAGTAGTC from NGS_read
def count_Alleles_frequency_table():
    util = Util.Utils()
    read_A_list = util.read_tb_txt_wout_header(WORK_DIR + "input/AGAGGACAGTCAGCTCCAAG/Alleles_frequency_table.txt")
    miss_cnt = 0
    total_cnt = 0
    for tmp_arr in read_A_list:
        NGS_read = tmp_arr[0]
        REF_read = tmp_arr[1]
        total_cnt += 1
        if REF_read.find("-"*47) == 0:
            NGS_read_wo_needle = NGS_read.replace("-", "")
            # print "::::::::::::::::::::::::::::::::::"
            try:
                # const_1 = NGS_read_wo_needle.index("AGTACGTACGAGTC")
                # print const_1, " : 1 "
                const_2 = NGS_read_wo_needle.index("GTACTCGCAGTAGTC")
                print const_2, " : 2"
                # print NGS_read
                # print REF_read
            except Exception as err:
                print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                miss_cnt += 1
                # print NGS_read_wo_needle
                # print NGS_read
                # print REF_read
                # print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        else:
            NGS_read_wo_needle = NGS_read.replace("-", "")
            # print "::::::::::::::::::::::::::::::::::"
            # try:
            #     const_1 = NGS_read_wo_needle.index("AGTACGTACGAGTC")
            #     const_2 = NGS_read_wo_needle.index("GTACTCGCAGTAGTC")
            #     print const_1, " : ", const_2
            #     print NGS_read
            #     print REF_read
            # except Exception as err:
            #     print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
            #     print NGS_read_wo_needle
            #     print NGS_read
            #     print REF_read
            #     print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    print "miss_cnt : ", str(miss_cnt)
    print "total_cnt : ", str(total_cnt)
    print "rate : ", (float(miss_cnt)/float(total_cnt)) * 100



if __name__ == '__main__':
    start_time = time.time()
    print("start >>>>>>>>>>>>>>>>>>")
    # multi_processing_plan_B()
    count_Alleles_frequency_table()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.time() - start_time))
