
class LogicPreps:
    def __init__(self):
        self.FASTQ = "FASTQ/"

    def make_cmd_var_list(self, barcd_list, fastq_list):
        result_list = []

        for fastq_pair in fastq_list:
            fastq_r1 = fastq_pair[0]
            fastq_r2 = ""
            if len(fastq_pair) > 1:
                fastq_r2 = fastq_pair[1]
            for barcd_arr in barcd_list:
                output_dir = barcd_arr[0]
                guide_seq = barcd_arr[0]
                amplicon_seq = barcd_arr[1]
                result_list.append([output_dir, amplicon_seq, guide_seq, self.FASTQ + fastq_r1, self.FASTQ + fastq_r2])

        return result_list