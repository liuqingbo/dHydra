from dHydra.Vendor.SinaL2.SinaL2 import SinaL2
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

sina_l2 = SinaL2(symbols = ["sz000570", "sz002762", "sh600774", 
    "sh600828", "sh600215", "sz000953", "sz002514", "sz002552", "sz300175", "sh6003268", "sz002495",
    "sz002606", "sh600679", "sh600678", "sz300149", "sz300106", "sz300090", "sh600137", "sz300382",
    "sh600335"], on_recv_data = on_recv_data)
sina_l2.start()
