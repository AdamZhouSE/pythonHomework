import math
num=int(input())
arr=[int(n) for n in input().split(' ')]
re=[]
for i in range(0, num):
    if arr[i]>=0:
        r=math.sqrt(arr[i])
        x=r-int(r)
        if x==0.0:
            continue
        else:
            re.append(arr[i])
    else:
        re.append(arr[i])
max=re[0]
for i in range(1,len(re)):
    if re[i]>max:
        max=re[i]
print(max)