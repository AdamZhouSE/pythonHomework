t=int(input())
for i in range(t):
    inlist=input().split()
    a=int(inlist[0])
    b=int(inlist[1])
    d=b-a
    n=int(input())
    s=a+(n-1)*d
    print(s)