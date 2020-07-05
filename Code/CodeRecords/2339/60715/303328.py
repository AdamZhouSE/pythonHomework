T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    count=0
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            if num[i]>num[j]:
                count+=1
    print(count)
    T-=1