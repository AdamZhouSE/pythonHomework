import math

temp=[int(x) for x in input().split(',')]
thr=int(input())

res=sum(temp)
div=1

while(res>thr):
    div+=1
    out=[math.ceil(float(x)/div) for x in temp]
    res=sum(out)
    
print(div)