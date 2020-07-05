t=int(input())
for _ in range(t):
    p,s=map(int,input().split())
    print(min(p/12,(s/6)**0.5)**3)