from datetime import datetime
import time
import subprocess

while(True):
    now = datetime.now()
    seconds_str = f"0{now.second}" if now.second < 10 else str(now.second)
    print(str(chr(16)) + "\t" + str(now.hour) + ":" + str(now.minute) + ":" + seconds_str + "\t" + str(chr(17)))
    time.sleep(0.9)
    subprocess.call('clear')