init=[int(x) for x in input().split()]
n=init[0]
m=init[1]
pairs=[]
for i in range(m):
    pairs.append([int(x) for x in input().split()])
def check(now,group):
    judge=True
    for i in group:
        if [i+1,now+1] in pairs:
            if i%2==0:
                temp=check(i+1,group)
                if temp[0]:
                    group=temp[1]
                    group.remove(i)
                    group.append(now)
                    group.sort()
                    return [True,group]
                else:
                    judge=False
                    break
            else:
                temp=check(i-1,group)
                if temp[0]:
                    group=temp[1]
                    group.remove(i)
                    group.append(now)
                    group.sort()
                    return [True, group]
                else:
                    judge = False
                    break
    if judge:
        group.append(now)
        group.sort()
        return [True, group]
    else:
        if now%2==0:
            return check(now+1,group)
        else:
            return [False,group]
result=True
group=[]
for i in range(0,2*n,2):
    temp=check(i,group)
    if not temp[0]:
        result=False
        break
    else:
        group=temp[1]
if result:
    for i in group:
        print(i)
else:
    print("NIE")