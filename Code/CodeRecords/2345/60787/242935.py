k=int(input())
for p in range(0,k):
    n=int(input())
    num=[int(i) for i in input().split()]
    num=sorted(num)
    A,B=0,0
    flagA=False
    flagB=False
    for i in range(0,n-1):
        if num[i]==num[i+1]:
            B=num[i]
            flagB=True
        if num[i]+1<num[i+1]:
            A=num[i]+1
            flagA=True
        if flagA and flagB:
            break
    print(B+A)