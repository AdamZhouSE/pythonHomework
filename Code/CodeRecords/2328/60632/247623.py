import re

data = ''.join(sorted(list(input().split(','))))
time = ''
if re.match('2[0-3][0-5][0-9]', data):
    if data[-1] >= '6':
        time = data
    else:
        time = data if data[-2] > data[-1] else data[:2] + data[-1] + data[-2]
    print(time[:2] + ':' + time[2:])
elif re.match('[0-1][0-5][0-9][0-9]', data):
    time += data[0] + max(data[-1], data[-2])
    if min(data[-1], data[-2]) >= '6':
        time += data[1] + min(data[-1], data[-2])
    else:
        time += max(data[1], min(data[-1], data[-2])) + min(data[1], min(data[-1], data[-2]))
    print(time[:2] + ':' + time[2:])
else:
    print('')
