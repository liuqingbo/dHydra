from dHydra..SinaL2.SinaL2 import SinaL2
import os
import time

def on_recv_data(message):
    current_time_date = time.strftime("%Y%m%d")
    current_date_dir = "D:\\level2\\" + current_time_date
    if os.path.exists(current_date_dir) != True:
        os.mkdir(current_date_dir)

    current_time_min = time.strftime("%Y%m%d%H%M")
    current_file = open(current_date_dir + "\\" + current_time_min, "a")
    current_file.write(message)
    current_file.close()        

sina_l2 = SinaL2(nickname = "SinaL2Default", symbols = ["sz000001"], "")
sina_l2.start()
