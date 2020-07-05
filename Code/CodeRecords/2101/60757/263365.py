import math
def cal(num):
    count=0
    for i in range(len(str(num))):
        count=count+math.pow(int(str(num)[i]),2)
    return int(count)
n=int(input())
li=[]
sign=0
tmp=n
while(True):
    li.append(tmp)
    tmp=cal(tmp)
    if li.count(tmp)!=0:
        print(False)
        break
    elif tmp==1:
        print(True)
        break