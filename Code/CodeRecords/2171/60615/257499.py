
time=int(input())
result=[]

while time>0:
    length=int(input())
    num=list(map(int,input().split()))
    even=[]
    i=0
    while i<length:
        if num[i]%2==0:
            even.append(num[i])
            num[i]='none'
        i=i+1
    for item in num:
        if item!='none':
            even.append(item)
    time=time-1
    result.append(even)
for res in result:
    print(' '.join(str(r) for r in res)+' ')

