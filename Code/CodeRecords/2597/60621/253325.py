w,c=0,0
f=[]
def sec(ele):
    return ele[1]
while True:
    a=[int(x) for x in input().split()]
    if(a[0]==-1):
        break
    elif a[0]==1:
        f.append([a[1],a[2]])
        w+=a[1]
        c+=a[2]
    elif a[0]==3:
        if(len(f)==0):
            continue
        f.sort(key=sec)
        te=f.pop(0)
        w-=te[0]
        c-=te[1]
    else:
        if (len(f) == 0):
            continue
        f.sort(key=sec)
        te = f.pop(len(f)-1)
        w -= te[0]
        c -= te[1]
print(w,c,end="")