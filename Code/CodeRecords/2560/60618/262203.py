t=int(input())
for i in range(0,t):
    n=int(input())
    id=[int(n) for n in input().split()]
    id1=list(set(id))
    m=int(input())
    num=[]
    for j in range(0,len(id1)):
        num.append(id.count(id1[j]))
    for k in range(1,len(num)):
        for l in range(0,len(num)-k):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    number=len(id1)
    for a in range(0,len(num)):
        if m-num[a]>=0:
            number-=1
            m=m-num[a]
    print(number)