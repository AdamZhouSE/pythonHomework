def findmin(lst):
    mi=lst[0]
    for e in lst:
        mi=min(mi,e)
    return mi

def eval(eles):
    return findmin(eles)*len(eles)

for b in range(int(input())):
    size=int(input())
    
    eles=list(map(int,input().split()))
    ma=0
    for aa in range(size-1):
        for bb in range(aa+1,size):
            ma=max(ma,eval(eles[aa:bb]))
    print(ma)





