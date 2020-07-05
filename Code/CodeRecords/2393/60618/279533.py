t=int(input())
for m in range(t):
    a,b=map(int,input().split())
    x=[int(a) for a in input().split()]
    y=[int(b) for b in input().split()]
    sum=0
    for i in range(0,a):
        for j in range(0,b):
            if x[i]**y[j]>y[j]**x[i]:
                sum+=1
    print(sum)