import os


class run_CRISPResso2:
    def __init__(self):
        pass

    # def __init__(self, init):
    #     self.output_dir = init[0]
    #     self.amplicon_seq = init[1]
    #     self.guide_seq = init[2]
    #     self.fastq_r1 = init[3]
    #     self.fastq_r2 = init[4]

    def run_CRISPResso_fastq_r1(self, output_path, fastq_r1, amplicon_seq, guide_seq):
        os.system('CRISPResso --fastq_r1 {} -o {} --amplicon_seq {} --guide_seq {}'.
                  format(fastq_r1, output_path + guide_seq, amplicon_seq, guide_seq))
        return

    def run_CRISPResso_fastq_r1_r2_w_flash(self, output_path, fastq_r1, fastq_r2, amplicon_seq, guide_seq):
        os.system('CRISPResso --fastq_r1 {} --fastq_r2 {} -o {} --amplicon_seq {} --guide_seq {}'.
                  format(fastq_r1, fastq_r2, output_path + guide_seq, amplicon_seq, guide_seq))
        return

    """
    --prime_editing_pegRNA_scaffold_seq: If given, reads containing any of this scaffold sequence before extension sequence (provided by --prime_editing_extension_seq) will be classified as 'Scaffold-incorporated'. The sequence should be given in the 5'->3' order such that the RT template directly follows this sequence. A common value ends with 'GGCACCGAGUCGGUGC'. (default: )
    -e or --expected_hdr_amplicon_seq: Amplicon sequence expected after HDR. The expected HDR amplicon sequence can be provided to quantify the number of reads showing a successful HDR repair. Note that the entire amplicon sequence must be provided, not just the donor template. CRISPResso2 will quantify identified instances of NHEJ, HDR, or mixed editing events. (default: )
    --exclude_bp_from_left 45
    """
    def run_CRISPResso_fastq_r1_r2_w_flash_extra_opt(self, output_path, fastq_r1, fastq_r2, amplicon_seq, guide_seq, const):
        os.system('CRISPResso --fastq_r1 {} --fastq_r2 {} -o {} --amplicon_seq {} --guide_seq {} --prime_editing_pegRNA_scaffold_seq {}'.
                  format(fastq_r1, fastq_r2, output_path + guide_seq, amplicon_seq, guide_seq, const))
        return