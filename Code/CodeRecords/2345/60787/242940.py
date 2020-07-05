k=int(input())
for p in range(0,k):
    n=int(input())
    num=[int(i) for i in input().split()]
    num=sorted(num)
    A,B=0,0
    flagA=False
    flagB=False
    if num[0]>1:
        flagA=True
        A=1
    for i in range(0,n-1):
        if num[i]==num[i+1] and not flagB:
            B=num[i]
            flagB=True
        if num[i]+1<num[i+1] and not flagA:
            A=num[i]+1
            flagA=True
        if flagA and flagB:
            break
    print(B,A)