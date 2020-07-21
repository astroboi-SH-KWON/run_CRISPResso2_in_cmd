
class LogicPreps:
    def __init__(self):
        self.FASTQ = "FASTQ/"

    def make_cmd_var_list(self, barcd_list, fastq_list):
        result_list = []

        for fastq_pair in fastq_list:
            fastq_r1 = fastq_pair[0].strip()
            fastq_r2 = ""
            if len(fastq_pair) > 1:
                fastq_r2 = fastq_pair[1].strip()
            for barcd_arr in barcd_list:
                output_dir = barcd_arr[0].strip()
                guide_seq = barcd_arr[0].strip()
                amplicon_seq = barcd_arr[1].strip()
                result_list.append([output_dir, guide_seq, amplicon_seq, self.FASTQ + fastq_r1, self.FASTQ + fastq_r2])

        return result_list