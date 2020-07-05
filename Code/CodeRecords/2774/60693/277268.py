cases=int(input())
nt=input().split()
n,t=int(nt[0]),int(nt[1])
costs=list(map(int,input().split()))
costs.sort()
sum=0
for i in range(n):
    if((sum+costs[i])>t):
        print(i)
        break
    else:
        sum+=costs[i]