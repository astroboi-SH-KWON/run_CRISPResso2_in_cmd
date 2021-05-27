import time
import os
import multiprocessing as mp
# from multiprocessing import Process


# import Util
# import run_CRISPResso2
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

############### end setting env ################


def trimmer_test():
    unjoined_fastq_pair_list = [['328_S0_L001_R1_001.fastq.gz', '328_S0_L001_R2_001.fastq.gz']]
    tmp_ext = '.fastq.gz'

    for fastq_pair_arr in unjoined_fastq_pair_list:
        fastq_r1_nm = fastq_pair_arr[0]
        fastq_r2_nm = fastq_pair_arr[1]
        fastq_r1 = WORK_DIR + FASTQ + fastq_r1_nm
        fastq_r2 = WORK_DIR + FASTQ + fastq_r2_nm
        fastq_r1_paired = WORK_DIR + FASTQ + fastq_r1_nm.replace(tmp_ext, '_paired' + tmp_ext)
        fastq_r1_unpaired = WORK_DIR + FASTQ + fastq_r1_nm.replace(tmp_ext, '_unpaired' + tmp_ext)
        fastq_r2_paired = WORK_DIR + FASTQ + fastq_r2_nm.replace(tmp_ext, '_paired' + tmp_ext)
        fastq_r2_unpaired = WORK_DIR + FASTQ + fastq_r2_nm.replace(tmp_ext, '_unpaired' + tmp_ext)
        os.system('java -jar ./Trimmomatic-0.36/trimmomatic-0.36.jar PE {} {} {} {} {} {} ILLUMINACLIP:./Trimmomatic-0.36/adapters/NexteraPE-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'.format(fastq_r1, fastq_r2, fastq_r1_paired, fastq_r1_unpaired, fastq_r2_paired, fastq_r2_unpaired))


if __name__ == '__main__':
    start_time = time.time()
    print("start >>>>>>>>>>>>>>>>>>")
    trimmer_test()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.time() - start_time))