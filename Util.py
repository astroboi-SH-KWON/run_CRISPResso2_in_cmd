import psutil
import time

class Utils:
    def __init__(self):
        self.ext_txt = ".txt"
        self.ext_dat = ".dat"
        self.ext_xlsx = ".xlsx"

    def read_tb_txt_wout_header(self, path):
        result_list = []
        with open(path, "r") as f:
            print ("header : ", f.readline().replace("\n", ""))
            while True:
                tmp_line = f.readline().replace("\n", "")
                if tmp_line == "":
                    break

                tmp_arr = tmp_line.split("\t")

                result_list.append(tmp_arr)

        return result_list

    def check_limit_cpu(self, max_cpu_cnt, proc_nm):
        proc_cnt = 0
        for process in psutil.process_iter():
            if proc_nm in process.name():
                proc_cnt += 1
        if proc_cnt > max_cpu_cnt:
            time.sleep(600)
            self.check_limit_cpu(max_cpu_cnt, proc_nm)
        else:
            return

    def check_limit_cpu_test(self, max_cpu_cnt, proc_nm):
        proc_cnt = 0
        for process in psutil.process_iter():
            if proc_nm in process.name():
                # self.kill_done_process(process)
                proc_cnt += 1
        if proc_cnt > max_cpu_cnt:
            time.sleep(3)
            self.check_limit_cpu(max_cpu_cnt, proc_nm)
        else:
            return

    def kill_done_process(self, process):
        try:
            process_dict = process.as_dict()
            print "cpu_percent : ", process.cpu_percent()
            print "cmdline : ", process.cmdline()
            print "pid : ", process.pid
            print "parent : ", process.parent()
            print "connections : ", process.connections()
            # print "cpu_affinity : ", process.
            print "cpu_affinity : ", process.wait()
            # print "cpu_affinity : ", process.
            # print "cpu_affinity : ", process.
            # print "cpu_affinity : ", process.
            # print "cpu_affinity : ", process.
            print "memory_percent : ", process.memory_percent()
            # print process_dict
        except psutil.NoSuchProcess :
            print "psutil.NoSuchProcess"
