# run_CRISPResso2_in_cmd
python2 Multi_run_CRISPResso2.py

1. make 'Alleles_frequency_table.txt' by CRISPResso2
    input file : 
        [./input/var_list.txt](./input/var_list.txt)
        ./FASTQ/[FASTQ files]
        
    python2 Multi_run_CRISPResso2.py
    
    output file :
        ./output/{guide_seq}/{fatq_1 fastq_2}/Alleles_frequency_table.txt
        
2. analyze output file by get_indel_fr_CRISPResso2_Alleles_frequency_table

