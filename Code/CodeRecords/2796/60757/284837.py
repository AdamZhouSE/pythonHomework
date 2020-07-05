import math
n=int(input())
li=list(map(int,input().split()))
maxc=-math.pow(10,6)
for i in range(len(li)):
    num=li[i]
    if num<0:
        if num>maxc:
            maxc=num
    elif math.pow(round(math.sqrt(num),0),2)!=num:
        if num>maxc:
            maxc=num
print(maxc)