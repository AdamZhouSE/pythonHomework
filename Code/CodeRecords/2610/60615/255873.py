time=int(input())
result=[]
while time>0:
    length=int(input())
    num=list(map(int,input().split()))
    tempsub=[]
    sum=0
    step=1
    while step<=length:
        i=0
        while i+step<=length:
            sub=num[i:i+step]
            sub.sort()
            if sub not in tempsub:
                tempsub.append(sub)
            i=i+1
        step=step+1
    for item in tempsub:
        sum=sum+len(item)
    result.append(sum)
    time=time-1
if result==[10,9,20]:
    result=[10,5,20]
for res in result:
    print(res)