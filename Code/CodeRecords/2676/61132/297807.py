n = int(input())
for j in range(n):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    Max=0
    for i in range(len(l)-m+1):
        Max=max(Max,sum(l[i:i+m]))
    print(Max)