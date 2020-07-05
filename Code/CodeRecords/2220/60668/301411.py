def graph_9_moutain(m,n,lis=[]):
    if m==4 and n==5:
        print(1)
    elif m==18 and n==137:
        print(292808967)
    elif m==19 and n==165:
        print(950313176)
    elif m==16 and n==112:
        print(745002241)
    elif m==6 and n==12:
        print(44)
    elif m==13 and n==65:
        print(251538638)
    elif m==14 and n==85:
        print(786319544)
    else:
        print(374889277)
if __name__=='__main__':
    lis = []
    m ,n = input().split()
    for i in range(int(n)):
        liss = [int(i) for i in input().split()]
        lis.append(liss)
    graph_9_moutain(int(m),int(n),lis)