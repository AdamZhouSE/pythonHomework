cases=int(input())
for i in range(cases):
    n=int(input())
    ropes=list(map(int,input().split()))
    res=0
    while ropes:
        ropes=sorted(ropes)
        new_len=ropes.pop(0)+ropes.pop(0)
        res+=new_len
        if len(ropes):
            ropes.append(new_len)
    print(res)