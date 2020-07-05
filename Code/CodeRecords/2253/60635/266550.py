info=input().split()
n=int(info[0])
m=int(info[1])
static=[int(x)for x in input().split()]
def findk(src,k):
    src.sort()
    return src[k-1]
def rank(src,k):
    src.sort()
    return src.index(k)+1
for i in range(m):
    info=input().split()
    op=int(info[0])
    l=int(info[1])-1
    r=int(info[2])
    oprand=0
    if op!=3:
        oprand=int(info[3])
    if op==1:
        print(rank(static[l:r],oprand))
    elif op==2:
        print(findk(static[l:r],oprand))
    elif op==3:
        static[l-1]=r
    elif op==4:
        tmp = [x for x in static[l:r] if x < oprand]
        print(max(tmp))
    elif op==5:
        tmp = [x for x in static[l:r] if x > oprand]
        print(min(tmp))