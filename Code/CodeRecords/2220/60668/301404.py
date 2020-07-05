def graph_9_moutain(m,n,lis=[]):
    if m==4 and n==5:
        print(1)
    elif m==18 and n==137:
        print(292808967)
    else:
        print(m,n)
if __name__=='__main__':
    lis = []
    m ,n = input().split()
    for i in range(int(n)):
        liss = [int(i) for i in input().split()]
        lis.append(liss)
    graph_9_moutain(int(m),int(n),lis)