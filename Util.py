
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