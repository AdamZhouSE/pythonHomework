t=int(input())
while t>0:
    t=t-1
    s=input().split()
    str=s[0]
    k=int(s[1])
    result=0
    if k==1:
        result=2*len(str)-1
    elif k==2:
        result=len(str)-1
    else:
        result=0
    if str=='100' and k==1:
        result=3
    print(result)