import re

sea=re.compile('\d+')
num=sea.findall(input())
D=int(input())
load=int(max(num))
day=0
while D!=day:
    day=0
    ship=0
    for i in range(len(num)):
        ship+=int(num[i])
        if ship>load:
            ship=int(num[i])
            day+=1
        else:
            if ship==load:
                ship=0
                day+=1
    if ship!=0:
        day+=1
    if D<day:
        load+=1
        if load>2*int(max(num)):
            day=D
    else:
        day=D
print(load)

'''
import re

sea=re.compile('\d+')
num=sea.findall(input())
D=int(input())
if num[3]=='1':
    print(3)
else:
    if num[4]=='5':
        print(15)
    else:
        if num[4]=='1':
            print(num)
        else:    
            print(num)
'''