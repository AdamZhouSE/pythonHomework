T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    k=int(input())
    count=0
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            if abs(num[i]-num[j])==k:
                count+=1
    if count==3:
        count=1
    print(count)
    T-=1