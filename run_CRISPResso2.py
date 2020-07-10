import os


class run_CRISPResso2:
    def __init__(self):
        self.tmp = ""

    def execute (self):
        os.system('CRISPResso {}_S{}_L001_R1_001.fastq.gz {}_S{}_L001_R2_001.fastq.gz -M 400 -m 10 -O -o {}'.
                  format(self.file_No,self.file_No,self.file_No, self.file_No, self.output))

        return