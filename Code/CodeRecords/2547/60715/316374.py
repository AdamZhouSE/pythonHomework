T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    k=int(input())
    a=[]
    count=0
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            b=[]
            b.append(num[i])
            b.append(num[j])
            if b not in a:
                a.append(b)
    for i in a:
        if abs(i[0]-i[1])==k:
            count+=1
    print(count)
    T-=1