
import run_CRISPResso2
class Logics:
    def __init__(self):
        self.tmp = ""

    def run_crispresso_w_list(self, input_list):
        print "run_crispresso_w_list START"
        run_crispresso = run_CRISPResso2.run_CRISPResso2()
        for init in input_list:
            run_crispresso.run_CRISPResso_fastq_r1(init)
