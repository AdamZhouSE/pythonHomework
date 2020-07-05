t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print(1 if n>sum(range(1,x+1))else 0)