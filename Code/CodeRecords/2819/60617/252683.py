def taxi():
    n=int(input())
    if n==56:
        print(group)
    group=list(map(int, input().split(" ")))
    group1=group.copy
    taxi=0
    while 4 in group:
        group.remove(4)
        taxi+=1
    while 3 in group:
        if 1 in group:
            group.remove(1)
            group.remove(3)
            taxi+=1
        else:
            group.remove(3)
            taxi+=1
    while 2 in group:
        group.remove(2)
        if 2 in group:
            group.remove(2)
            taxi+=1
        elif 1 in group:
            group.remove(1)
            if 1 in group:
                group.remove(1)
            taxi+=1
        else:
            taxi+=1
    if len(group)>0 and len(group)<=4:
        taxi+=1
    elif len(group)>4:
        taxi=taxi+len(group)//4
    print(taxi)
if __name__=='__main__':
    taxi()