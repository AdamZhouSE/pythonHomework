def change(s):
    return int(s[0:2])*60+int(s[2:])


result = []
num = int(input())
for i in range(num):
    time = []
    n = int(input())
    for k in range(1440):
        time.append(0)
    come = input().split(" ")
    go = input().split(" ")
    res = 0
    for k in range(len(come)):
        flag = False
        for m in range(change(come[k]), change(go[k])):
            time[m] = time[m]+1
    for k in time:
        if k>res:
            res = k
    result.append(res)
for i in result:
    print(i)
