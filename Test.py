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
############### end setting env ################

def multi_processing_plan_B():
    util = Util.Utils()
    for idx in range(10):
        util.check_limit_cpu(MULTI_CNT, PROCESS_NAME)
        proc = Process(target=test)
        proc.start()
        print "idx >>>>>>>>>>>>>>>>>>>>>> ", str(idx)


def test():
    print "test is running ++++++++++++++++++++++++++++++++++"
    time.sleep(5)
    print "test is done --------------------------------------"
    # print "::::::::::::::::"


if __name__ == '__main__':
    start_time = time.time()
    print("start >>>>>>>>>>>>>>>>>>")
    # multi_processing()
    multi_processing_plan_B()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.time() - start_time))
