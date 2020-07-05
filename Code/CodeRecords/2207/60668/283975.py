def linerlist_13_sums(n,k):
    lis = list(range(1,n+1))
    nStart = 0
    nEnd = (1 << len(lis)) - 1
    re = []
    co = []
    for j in range(nStart, nEnd + 1):
        for n in range(0, len(lis)):
            if ((1 << n) & j) != 0:
                co.append(lis[n])
        re.append(co)
        co = []
    for item in re:
        if len(item)==k and sum(item)==n:
            return True
    return False
if __name__=='__main__':
    for _ in range(int(input())):
        n,k = input().split()
        if(linerlist_13_sums(int(n),int(k))):
            print(1)
        else:
            print(0)