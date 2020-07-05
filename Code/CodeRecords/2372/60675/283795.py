def strtoInt(string:str) -> int:
    return int(string)


def func(l1:list, l2:list, o:int, o1:int, o2:int) -> int:
    init = [[0] * (o + 1) for i in range(o + 1)]
    for i in range(1, o + 1):
        init[0][i] = init[0][i - 1] + l2[i - 1]
        init[i][0] = init[i - 1][0] + l1[i - 1]
    for m in range(1, o + 1):
        for n in range(1, o + 1):
            if m + n <= o:
                init[m][n] = max(init[m][n - 1] + l2[m + n - 1], init[m - 1][n] + l1[m + n - 1])
            else:
                init[m][n] = max(init[m - 1][n], init[m][n - 1])
    return init[-1][-1]


n = int(input())
for i in range(n):
    m = input().split(" ")
    o = int(m[0])
    o1 = int(m[1])
    o2 = int(m[2])
    l1 = list(map(strtoInt,input().strip().split(" ")))
    l2 = list(map(strtoInt,input().strip().split(" ")))
    print(func(l1,l2,o,o1,o2))