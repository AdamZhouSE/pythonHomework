def test():
    n = int(input())
    segSet = []
    for _ in range(0, n):
        seg = input().split(',')
        seg = list(map(int, seg))
        segSet.append(seg)
    ans = []
    for i in range(0, len(segSet)):
        res = []
        index = -1
        for j in range(0, len(segSet)):
            if segSet[i][1] <= segSet[j][0]:
                if res == []:
                    res = segSet[j]
                    index = j
                else:
                    if segSet[j][0] < res[0]:
                        res = segSet[j]
                        index = j
        ans.append(index)
    print(ans)


test()