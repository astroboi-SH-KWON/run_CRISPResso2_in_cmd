import os


class run_CRISPResso2:
    def __init__(self):
        self.tmp = ""

    # def __init__(self, init):
    #     self.output_dir = init[0]
    #     self.amplicon_seq = init[1]
    #     self.guide_seq = init[2]
    #     self.fastq_r1 = init[3]
    #     self.fastq_r2 = init[4]

    def run_CRISPResso_fastq_r1(self, output_path, guide_seq, amplicon_seq, fastq_r1):
        os.system('CRISPResso --fastq_r1 {} -o {} --amplicon_seq {} --guide_seq {}'.
                  format(fastq_r1, output_path + guide_seq, amplicon_seq, guide_seq))
        return

    def run_CRISPResso_fastq_r1_r2_w_falsh(self, output_path, guide_seq, amplicon_seq, fastq_r1, fastq_r2):
        os.system('CRISPResso --fastq_r1 {} --fastq_r2 {} -o {} --amplicon_seq {} --guide_seq {}'.
                  format(fastq_r1, fastq_r2, output_path + guide_seq, amplicon_seq, guide_seq))
        return