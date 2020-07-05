def sum(num,x):
    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==x:
                return "Yes"
    return "No"
T=int(input())
while T>0:
    n,x=map(int,input().split())
    num=[int(n) for n in input().split()]
    print(sum(num,x))
    T-=1