def linerlist_27_minormax(lis=[]):
    nStart = 0
    nEnd = (1 << len(lis)) - 1
    re = []
    co = []
    ma = 0
    for j in range(nStart, nEnd + 1):
        for n in range(0, len(lis)):
            if ((1 << n) & j) != 0:
                co.append(lis[n])
        re.append(co)
        co = []
    res = []
    ree = []
    for i in range(1,len(lis)+1):
        for item in re:
            if len(item)==i:
                res.append(min(item))
        ree.append(max(res))
        res = []
    for i in range(len(ree)-1):
        print(ree[i],end=' ')
    print(ree[len(ree)-1],end='\n')
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        lis = [int(i) for i in input().split()]
        linerlist_27_minormax(lis)