import ast

def minDelay():
    data = ast.literal_eval(input())
    for i in range(0,len(data)):
        if data[i] == '00:00':
            data[i] = '24:00'
    data.sort()
    res = -1
    minute = 0
    hour = 0
    for i in range(0,len(data) - 1):
        minute = int(data[i + 1][3:]) - int(data[i][3:])
        hour = int(data[i+1][:2]) - int(data[i][:2])
        if minute < 0:
            hour = hour - 1
            minute = minute + 60
        tmp = minute + hour * 60
        if res == -1:
            res = min(tmp,(24*60 - tmp))
        elif res > min(tmp,(24*60 - tmp)):
            res = min(tmp,(24*60 - tmp))


    print(res)

minDelay()
