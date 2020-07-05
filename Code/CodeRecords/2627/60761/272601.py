t=int(input())
for i in range(t):
    p,s=map(int,input().split(" "))
    a=(p-(p**2-24*s)**0.5)/12
    v=a*(s/2-a*(p/4-a))
   # x=min(p/12,(s/6)**0.5)
    print("{:.5f}".format(v))