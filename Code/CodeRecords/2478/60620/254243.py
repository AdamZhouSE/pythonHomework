t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    n=int(input())
    d=b-a
    print(a+d*(n-1))