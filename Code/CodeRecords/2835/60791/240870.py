import math
num = int(input())
a = [int(i) for i in input().split()]
count_zero=0
total=0
str = ''
for item in a:
    if(item == 0):
        count_zero +=1
if(count_zero > 0):
    for item in a:
        total += item
    if(total%9 == 0):
        for i in range(int(total/5)):
            str += '5'
        for i in range(count_zero):
            str += '0'
        print(str)
    elif(total > 45):
        n = math.floor(total/9)
        for i in range(int(n*9/5)):
            str += '5'
        for i in range(count_zero):
            str += '0'
        print(str)
    else:
        print(0)
else:
    print(-1)
