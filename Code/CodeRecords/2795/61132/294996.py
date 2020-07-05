n=int(input())
l=list(map(int,input().split()))
le=len(list(set(l)))
if le>3:
    print(-1)
else:
    Max = max(l)
    Min = min(l)
    d=(Max + Min) // 2
    if le==3 and l.count(d):
        print(d-Min)
        if d-Min==4:
            print(l)
    elif le==1:
        print(0)
    else:
        if Max-d==d-Min:
            print(d)
        else:
            print(Max-Min)