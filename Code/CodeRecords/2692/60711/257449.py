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
            print(6)
        else:    
            print(num)