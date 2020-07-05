D={}
while True:
    op=list(map(int,input().split()))
    if op[0]==-1:
        break
    elif op[0]==1:
        W,C=op[1],op[2]
        if C not in D:
            D[C]=W
    elif op[0]==2:
        del D[max(D.keys())]
    elif op[0]==3:
        del D[min(D.keys())]
print("%d %d" %(sum(D.values()),sum(D)),end="")