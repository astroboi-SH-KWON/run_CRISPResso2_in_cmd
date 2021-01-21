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
OU = "output/"

TOTAL_CPU = mp.cpu_count()
# MULTI_CNT = int(TOTAL_CPU*0.5)
# MULTI_CNT = 5
# PROCESS_NAME = "python"
DELAY_MIN = 120
CONST1 = "AGTACGTACGAGTC"  # 14 bp
CONST2 = "GTACTCGCAGTAGTC"  # 15 bp
############### end setting env ################


# conda install -c bioconda ea-utils
def multi_join_fastq_by_ea_utils():
    print 'multi_join_fastq_by_ea_utils()'
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()

    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq, output_path],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT', '253_1_Trp53'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    var_set = set()
    for val_arr in var_list:
        fstq_r1 = val_arr[1]
        fstq_r2 = val_arr[2]
        tu_fastq_pair = (fstq_r1, fstq_r2)
        var_set.add(tu_fastq_pair)

    for var_tu in var_set:
        fstq_r1 = var_tu[0]
        fstq_r2 = var_tu[1]
        fstq_arr = fstq_r1.split(".")
        proc = Process(target=run_crispresso.join_fastq_by_ea_utils,
                       args=(FASTQ + fstq_r1, FASTQ + fstq_r2, FASTQ + fstq_arr[0] + '_%.' + fstq_arr[1]))
        proc.start()
        print fstq_r1


def multi_CRISPResso2_after_ea_utils_fastq_join():
    print 'multi_CRISPResso2_after_ea_utils_fastq_join()'
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()

    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq, output_path],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT', '253_1_Trp53'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    for var_arr in var_list:
        # gene_nm = var_arr[0]
        fstq_r1 = var_arr[1]
        # fstq_r2 = var_arr[2]
        fstq_arr = fstq_r1.split(".")
        amp_seq = var_arr[3]
        guid_se = var_arr[4]
        out_path = var_arr[5].strip() + '/'
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1,
                       args=(OU + out_path, FASTQ + fstq_arr[0] + '_join.fastq', amp_seq, guid_se))
        proc.start()
        print fstq_r1
        time.sleep(60 * DELAY_MIN)


def multi_CRISPResso2_w_opt_after_ea_utils_fastq_join():
    print 'multi_CRISPResso2__w_opt_after_ea_utils_fastq_join()'
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()

    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq, output_path],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT', '253_1_Trp53'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    for var_arr in var_list:
        # gene_nm = var_arr[0]
        fstq_r1 = var_arr[1]
        # fstq_r2 = var_arr[2]
        fstq_arr = fstq_r1.split(".")
        amp_seq = var_arr[3]
        guid_se = var_arr[4]
        out_path = var_arr[5].strip() + '/'
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1_w_opt,
                       args=(OU + out_path, FASTQ + fstq_arr[0] + '_join.fastq', amp_seq, guid_se, '-wc -17'))
        proc.start()
        print fstq_r1
        time.sleep(60 * DELAY_MIN)


def multi_processing_plan_B():
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()

    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    for var_arr in var_list:
        fstq_r1 = var_arr[1]
        fstq_r2 = var_arr[2]
        amp_seq = var_arr[3]
        guid_se = var_arr[4]
        out_path = var_arr[5].strip() + '/'
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1_r2_w_flash,
                       args=(OU + out_path, FASTQ + fstq_r1 + ".gz", FASTQ + fstq_r2 + ".gz", amp_seq, guid_se))
        proc.start()
        time.sleep(60*DELAY_MIN)


# extract FASTQ files without .gz ext
def multi_processing_plan_B_wo_gz():
    print 'multi_processing_plan_B_wo_gz(): extract FASTQ files without .gz ext'
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()

    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    for var_arr in var_list:
        fstq_r1 = var_arr[1]
        fstq_r2 = var_arr[2]
        amp_seq = var_arr[3]
        guid_se = var_arr[4]
        out_path = var_arr[5].strip() + '/'
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1_r2_w_flash,
                       args=(OU + out_path, FASTQ + fstq_r1, FASTQ + fstq_r2, amp_seq, guid_se))
        proc.start()
        time.sleep(60*DELAY_MIN)


# extract FASTQ files without .gz ext
# for large indel, (option) --amplicon_min_alignment_score = 40
def multi_processing_plan_B_wo_gz_with_amplicon_min_alignment_score():
    print 'multi_processing_plan_B_wo_gz(): extract FASTQ files without .gz ext'
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()

    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    for var_arr in var_list:
        fstq_r1 = var_arr[1]
        fstq_r2 = var_arr[2]
        amp_seq = var_arr[3]
        guid_se = var_arr[4]
        out_path = var_arr[5].strip() + '/'
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1_r2_w_flash_for_large_indel, args=(
        OU + out_path, FASTQ + fstq_r1, FASTQ + fstq_r2, amp_seq, guid_se, 50))
        proc.start()
        time.sleep(60*DELAY_MIN)


def multi_processing_plan_C():
    util = Util.Utils()
    run_crispresso = run_CRISPResso2.run_CRISPResso2()

    # read [[gene, fastq_r1, fastq_r2, amplicon_seq, guide_seq],
    #       ['Trp53', 'GE_327_Pool_S0_L001_R1_001.fastq', 'GE_327_Pool_S0_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT'], ...]
    var_list = util.read_tb_txt_wout_header(WORK_DIR + INPUT_VAR_LIST)

    for var_arr in var_list:
        fstq_r1 = var_arr[1]
        fstq_r2 = var_arr[2]
        amp_seq = var_arr[3]
        guid_se = var_arr[4]
        out_path = var_arr[5].strip() + '/'
        proc = Process(target=run_crispresso.run_CRISPResso_fastq_r1_r2_w_flash_extra_opt,
                       args=(OU + out_path, FASTQ + fstq_r1 + ".gz", FASTQ + fstq_r2 + ".gz", amp_seq, guid_se, CONST2))
        proc.start()
        time.sleep(60*DELAY_MIN)


def run_solo_CRISPResso2_w_flash():
    print 'run_solo_CRISPResso2_w_flash()'
    run_crispresso = run_CRISPResso2.run_CRISPResso2()
    var_arr = ['Trp53', '253_1_S6_L001_R1_001.fastq', '253_1_S6_L001_R2_001.fastq', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT', 'Trp53_253_1_S6_L001_R1_001']
    print str(var_arr)
    fstq_r1 = var_arr[1]
    fstq_r2 = var_arr[2]
    amp_seq = var_arr[3]
    guid_se = var_arr[4]
    out_path = var_arr[5].strip() + '/'
    run_crispresso.run_CRISPResso_fastq_r1_r2_w_flash(OU + out_path, FASTQ + fstq_r1, FASTQ + fstq_r2, amp_seq, guid_se)


def run_solo_CRISPResso2_w_r1():
    print 'run_solo_CRISPResso2_w_r1()'
    run_crispresso = run_CRISPResso2.run_CRISPResso2()
    var_arr = ['Trp53', '253_2_join.fq', '', 'CCTACACTTTCAGAATTTAATTTCCCTACTGGATGTCCCACCTTCTTTTTATTCTACCCTTTCCTATAAGCCATAGGGGTTTGTTTGTTTGTATGTTTTTTAATTGACAAGTTATGCATCCATACAGTACACAATCTCTTCTCTCTACAGATGACTGCCATGGAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTCTGAGCCAGGAGACATTTTCAGGCTTATGGAAACTGTGAGTGGATCTT', 'TGCCATGGAGGAGTCACAGT', 'Trp53_253_2_join']
    print str(var_arr)
    fstq_r1 = var_arr[1]
    fstq_r2 = var_arr[2]
    amp_seq = var_arr[3]
    guid_se = var_arr[4]
    out_path = var_arr[5].strip() + '/'
    run_crispresso.run_CRISPResso_fastq_r1(OU + out_path, FASTQ + fstq_r1, amp_seq, guid_se)


if __name__ == '__main__':
    start_time = time.time()
    print("start >>>>>>>>>>>>>>>>>>")
    # # st by ea-utils
    # multi_join_fastq_by_ea_utils()
    # multi_CRISPResso2_after_ea_utils_fastq_join()
    multi_CRISPResso2_w_opt_after_ea_utils_fastq_join()
    # # en by ea-utils
    # run_solo_CRISPResso2_w_r1()
    # multi_processing_plan_B()
    # multi_processing_plan_B_wo_gz()
    # multi_processing_plan_B_wo_gz_with_amplicon_min_alignment_score()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.time() - start_time))
