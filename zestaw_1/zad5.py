import time
import subprocess
import os

text = input("Input text: ")

while(True):
    for i in range(0, os.get_terminal_size().lines):
        print(i*'\n'+ text)
        time.sleep(0.1)
        subprocess.call('clear')

    for i in reversed(range(0, os.get_terminal_size().lines)):
        print(i*'\n'+ text)
        time.sleep(0.05)
        subprocess.call('clear')