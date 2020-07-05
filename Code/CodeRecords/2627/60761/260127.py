t=int(input())
for i in range(t):
    p,s=map(int,input().split(" "))
    x=min(p/12,(s/6)**0.5)
    print(x**3,p,s)