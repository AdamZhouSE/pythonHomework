def standard(str):
    '''给一个号码，返回其标准模式(不含‘-’)'''
    result = ''
    for e in str:
        if ord('0') <= ord(e) <= ord('9'):
            result += e
        elif e == 'A' or e == 'B' or e == 'C':
            result += '2'
        elif e == 'D' or e == 'E' or e == 'F':
            result += '3'
        elif e == 'G' or e == 'H' or e == 'I':
            result += '4'
        elif e == 'J' or e == 'K' or e == 'L':
            result += '5'
        elif e == 'M' or e == 'N' or e == 'O':
            result += '6'
        elif e == 'P' or e == 'R' or e == 'S':
            result += '7'
        elif e == 'T' or e == 'U' or e == 'V':
            result += '8'
        elif e == 'W' or e == 'X' or e == 'Y':
            result += '9'
    return result[0:3] +  result[3:]

num = int(input())
tele = [ standard(input()) for i in range(num)]
idx = []
times = []
tele2 = []

for i,n in enumerate(tele):
    if n not in tele2:
        tele2.append(n)
        times.append(1)
        idx.append(i)
    else:
        idx_tmp = tele2.index(n)
        times[idx_tmp] += 1

result = []
for i,n in enumerate(times):
    if n >= 2:
        result.append(int(tele2[i]))#将七位电话号码记为int

#排成字典序(int从小到大)
for i in range(1,len(result)):
    for j in range(i):
        if result[i] < result[j]:
            tmp = result[i]
            result[i] = result[j]
            result[j] = tmp
            break

#格式化输出
for e in result:
    print(str(e)[0:3] + '-' + str(e)[3:] + ' ' +str(times[tele2.index(str(e))]))
if len(result) == 0:
    print('No duplicates.',end ='')