# 字符串替换
import re
N = int(input())
aList = []
for i in range(N):
    tmp = ''.join(input().strip())
    tmp = tmp.replace('-', '')
    tmp = re.sub('[A-C]', '2', tmp)
    tmp = re.sub('[D-F]', '3', tmp)
    tmp = re.sub('[G-I]', '4', tmp)
    tmp = re.sub('[J-L]', '5', tmp)
    tmp = re.sub('[M-O]', '6', tmp)
    tmp = re.sub('[PRS]', '7', tmp)
    tmp = re.sub('[T-V]', '8', tmp)
    tmp = re.sub('[W-Y]', '9', tmp)
    aList.append(tmp)
aList.sort()
dict1 = {}
for i in aList:
    if aList.count(i) > 1:
        dict1[i] = aList.count(i)
for i in dict1:
    print(i[0:3]+'-'+i[3:]+' '+str(dict1[i]))
if dict1 == {}:
    print('No duplicates.',end='')