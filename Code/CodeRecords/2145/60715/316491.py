T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    maxArea = 0;
    for i in range(len(num)):
        s=i
        e=i+1
        while s>=0 and num[s]>=num[i]:
            s-=1
        while e<len(num) and num[e]>=num[i]:
            e+=1
        maxArea=max(maxArea,num[i]*(e-s-1))
    print(maxArea)
    T-=1