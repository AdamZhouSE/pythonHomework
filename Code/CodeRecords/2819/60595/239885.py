def solve():
    total=int(input())
    s=input().strip()
    group=list(s.split(" "))
    group=[int(i) for i in group]
    car=0
    group.sort()
    group.reverse()
    last=total-1
    i=0
    while i<total:
        if group[i]<4:
            tmp=group[i]
            while(tmp+group[last]<=4 and last!=i):
                tmp=group[last]+tmp
                last=last-1
                total=total-1
            car=car+1
        else:
            car=car+1
        i=i+1
    print(car)
    return

if __name__=="__main__":
    solve()