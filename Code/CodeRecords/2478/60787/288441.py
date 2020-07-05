t=int(input())
for e in range(0,t):
    a,b=map(int,input().split(" "))
    d=b-a
    n=int(input())
    print(a+(n-1)*d)