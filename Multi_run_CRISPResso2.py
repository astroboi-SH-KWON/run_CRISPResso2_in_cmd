import time
import os
import multiprocessing as mp
from multiprocessing import Process
import numpy as np


import Util
import LogicPrep
import Logic
import run_CRISPResso2
############### start to set env ###############
WORK_DIR = os.getcwd() + "/"
INPUT_BARCD = "input/pre_cancer_barcode.txt"
INPUT_FASTQ = "input/fastq_pairs.txt"
OUTPUT_PATH = "output/"

TOTAL_CPU = mp.cpu_count()
# MULTI_CNT = int(TOTAL_CPU*0.5)
# MULTI_CNT = 5
# PROCESS_NAME = "python"
DELAY_MIN = 30
############### end setting env ################

def multi_processing_plan_B():
    util = Util.Utils()
    logic_prep = LogicPrep.LogicPreps()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()


    # read [[spacer without PAM_+strand, total_amplicon_seq], ...]
    barcd_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_BARCD)

    # read [[fastq_r1 file nm, fastq_r2 file nm], [GE_319_Pool_S0_L001_R1_001.fastq.gz, GE_319_Pool_S0_L001_R2_001.fastq.gz], ...]
    fastq_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_FASTQ)

    var_list = logic_prep.make_cmd_var_list(barcd_list, fastq_list)

    for init_arr in var_list:
        # util.check_limit_cpu(MULTI_CNT, PROCESS_NAME)
        # proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1, args=(OUTPUT_PATH, init_arr[1], init_arr[2], init_arr[3]))
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1_r2_w_falsh,
                       args=(OUTPUT_PATH, init_arr[1], init_arr[2], init_arr[3], init_arr[4]))
        proc.start()
        time.sleep(60*DELAY_MIN)

if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start >>>>>>>>>>>>>>>>>>")
    multi_processing_plan_B()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))
