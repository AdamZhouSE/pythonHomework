



for _ in range(int(input())):
    o, o1, o2 = map(int, input().strip().split(" "))
    l1 = list(map(int, input().strip().split(" ")))
    l2 = list(map(int, input().strip().split(" ")))
    result = solution(l1, l2, o, o1, o2)
    print(result)

def solution(l1, l2, o, o1, o2):
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
