n=int(input())
for i in range(0,n):
    s=int(input())
    res=0
    for j in range(1,s+1):
        if s%j==0:
            res+=j
    if res<2*s:
        print(1)
    else:
        print(0)