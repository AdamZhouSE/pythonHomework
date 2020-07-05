from collections import defaultdict
def isOverlap()->bool:
    r1=list(map(int,input().split(",")))
    r2=list(map(int,input().split(",")))
    lr=min(r1[0],r1[2])
    rr=max(r1[0],r1[2])
    lc=min(r1[3],r1[1])
    rc=max(r1[3],r1[1])
    x=[(lr,lc),(lr,rc),(rr,lc),(rr,rc)]
    for i,j in ((r2[0],r2[1]),(r2[0],r2[3]),(r2[2],r2[1]),(r2[2],r2[3])):
        if lr<=i<=rr and lc<=j<=rc and (i,j) not in x:
            return True
    return False

print(isOverlap())