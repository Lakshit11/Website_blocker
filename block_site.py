from datetime import datetime as dt
import time
host_path=r"C:\Windows\System32\drivers\etc\hosts"
host_temp="hosts"
redirect="127.0.0.1"    
sites=["www.facebook.com","facebook.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(host_path,"r+") as file:
            content=file.read()
            for site in sites:
                if site in content:
                    pass
                else:
                    file.write(redirect+" " +site+"\n")
        print("Work Time")
    else:
        with open(host_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            # print(content)
            for line in content:
                if not any(site in line for site in sites):
                    file.write(line)
            file.truncate()
        print("Home Time")

    time.sleep(5)