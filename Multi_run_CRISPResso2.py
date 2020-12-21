import time
import os
import multiprocessing as mp
from multiprocessing import Process


import Util
import run_CRISPResso2
############### start to set env ###############
WORK_DIR = os.getcwd() + "/"
FASTQ = "FASTQ/"
INPUT_BARCD = "input/pre_cancer_barcode.txt"
INPUT_FASTQ = "input/fastq_pairs.txt"
INPUT_VAR_LIST = "input/var_list.txt"
OUTPUT_PATH = "output/"

TOTAL_CPU = mp.cpu_count()
# MULTI_CNT = int(TOTAL_CPU*0.5)
# MULTI_CNT = 5
# PROCESS_NAME = "python"
DELAY_MIN = 60
CONST1 = "AGTACGTACGAGTC"  # 14 bp
CONST2 = "GTACTCGCAGTAGTC"  # 15 bp
############### end setting env ################

def multi_processing_plan_B():
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()


    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    for init_arr in var_list:
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1_r2_w_flash,
                       args=(OUTPUT_PATH, FASTQ + init_arr[1] + ".gz", FASTQ + init_arr[2] + ".gz", init_arr[3], init_arr[4]))
        proc.start()
        time.sleep(60*DELAY_MIN)

# extract FASTQ files without .gz ext
def multi_processing_plan_B_wo_gz():
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()


    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    for init_arr in var_list:
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1_r2_w_flash,
                       args=(OUTPUT_PATH, FASTQ + init_arr[1], FASTQ + init_arr[2], init_arr[3], init_arr[4]))
        proc.start()
        time.sleep(60*DELAY_MIN)


def multi_processing_plan_C():
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()


    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    for init_arr in var_list:
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1_r2_w_flash_extra_opt, args=(
        OUTPUT_PATH, FASTQ + init_arr[1] + ".gz", FASTQ + init_arr[2] + ".gz", init_arr[3], init_arr[4], CONST2))
        proc.start()
        time.sleep(60*DELAY_MIN)


def run_solo_CRISPResso2():
    run_crispresso = run_CRISPResso2.run_CRISPResso2()
    init_arr = ['Trp53', '253_1_S6_L001_R1_001.fastq', '253_1_S6_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT']
    run_crispresso.run_CRISPResso_fastq_r1_r2_w_flash(OUTPUT_PATH, FASTQ + init_arr[1], FASTQ + init_arr[2],
                                                      init_arr[3], init_arr[4])


if __name__ == '__main__':
    start_time = time.time()
    print("start >>>>>>>>>>>>>>>>>>")
    # run_solo_CRISPResso2()
    # multi_processing_plan_B()
    multi_processing_plan_B_wo_gz()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.time() - start_time))
