t=int(input())
while(t>0):
    n=int(input())
    a=[]
    num=input()
    for x in num.split():
        a.append(int(x))
    P=[]
    i=0
    p=1
    for x in a:
        p=p*x
    while i<n:
        P.insert(i,p//a[i])
        i=i+1
    for x in P:
        print(x,end=" ")
    print()
    t=t-1
        