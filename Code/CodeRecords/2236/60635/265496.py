static=[]
rank=[]
n=int(input())
for i in range(n):
    info=input().split()
    op=int(info[0])
    oprand=int(info[1])
    rank=sorted(static)
    if op==1:
        static.append(oprand)
    elif op==2:
        static.remove(oprand)
    elif op==3:
        print(rank.index(oprand)+1)
    elif op==4:
        print(rank[oprand-1])
    elif op==5:
        tmp=[x for x in static if x<oprand]
        print(max(tmp))
    else:
        tmp = [x for x in static if x > oprand]
        print(min(tmp))
        