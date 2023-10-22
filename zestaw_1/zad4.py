import time
import subprocess

length = int(input('Insert bar length: '))
bar = '|'

while(len(bar) < length + 1):
    bar += '-'

bar += '|'

progress = 0

for i in range(1, length+1):
    loading = bar[progress+1:]
    print('|' + '='*progress + loading + ' ' + str(int((progress/length)*100)) + '%')
    progress += 1
    time.sleep(0.7)
    subprocess.call('clear')

print('|' + '='*progress + '|' + ' ' + str(int((progress/length)*100)) + '%')