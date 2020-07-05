n=int(input())
l=list(map(int,input().split()))
le=len(list(set(l)))
if le>3:
    print(-1)
else:
    Max = max(l)
    Min = min(l)
    d=(Max + Min) // 2
    if le==3:
        if l.count(d):
            print(d - Min)
        else:
            print(-1)
    elif le==1:
        print(0)
    else:
        if Max-d==d-Min:
            print(d-Min)
        else:
            print(Max-Min)