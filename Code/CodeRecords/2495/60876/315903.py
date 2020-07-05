s=list(input())
dir=eval(input())
def findmax():
    maxlen=0
    maxs=""
    for item in dir:
        if len(item)>maxlen:
            maxlen=len(item)
            maxs=item
    return maxs
l=len(dir)
for i in range(0,l):
    target=findmax()
    ind=dir.index(target)
    temp=list(target)
    jud=True
    cur=0
    tem=s[:]
    for item in temp:
        if item not in tem:
            jud=False
            break
        else:
            inde=tem.index(item)
            tem=tem[inde:]
            continue
    if jud:
        print(target)
        break
    else:
        dir[ind]=""
        continue