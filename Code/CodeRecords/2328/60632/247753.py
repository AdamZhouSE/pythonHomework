import re

data = ''.join(sorted(list(input().split(','))))
time = ''
copy = data[:]  # 拷贝一个副本
if data.count('2') != 0:  # 如果有2，把副本中的2移到首位
    copy = list(data)
    copy.remove('2')
    copy = '2' + ''.join(copy)
# 对不同情况进行正则匹配
if re.match('2[0-3][0-5][0-9]', copy):
    time += '2'
    # 确定首位为2，对剩余3位的不同情况进行正则匹配
    if re.match('[0-3][0-3][0-3]', copy[1:]):
        time += copy[-1] + copy[-2] + copy[-3]
    elif re.match('[0-3][0-3][4-5]', copy[1:]):
        time += copy[-2] + copy[-1] + copy[-3]
    elif re.match('[0-3][0-3][6-9]', copy[1:]):
        time += copy[-2] + copy[-3] + copy[-1]
    elif re.match('[0-3][4-5][4-5]', copy[1:]):
        time += copy[-3] + copy[-1] + copy[-2]
    elif re.match('[0-3][4-5][6-9]', copy[1:]):
        time += copy[-3] + copy[-2] + copy[-1]
    print(time[:2] + ':' + time[2:])
elif re.match('[0-1][0-5][0-9][0-9]', data):
    time += data[0] + data[-1]
    if data[-2] >= '6':
        time += data[1] + data[-2]
    else:
        time += data[-2] + data[1]
    print(time[:2] + ':' + time[2:])
else:
    print('')
