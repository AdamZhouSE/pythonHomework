t=int(input())
for i in range(t):
    n,k=map(int,input().split(" "))
    cost=list(map(int,input().split(" ")))
    cost.append(k)
    cost.sort()
    print(cost.index(k))