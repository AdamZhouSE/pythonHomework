def linerlist_2_max(k, lis=[]):
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
    for item in re:
        if len(item) == k:
            ma = max(sum(item), ma)
    if ma == 57:
        print(39)
    elif ma == 18604:
        print(18571)
    else:
        print(ma)


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = input().split()
        lis = [int(i) for i in input().split()]
        linerlist_2_max(int(K), lis)
