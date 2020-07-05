import math


num= int(input())
lognum = math.log(num, 4)
part = math.floor(lognum)
if lognum - part == 0:
    print('true')
else:
    print('false')