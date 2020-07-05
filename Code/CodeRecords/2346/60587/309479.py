T = int(input())
while T > 0:
    T -= 1
    m, n = input().split(' ')
    m = int(m)
    n = int(n)
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]

    matrix = [[] for i in range(m)]
    for i in range(m):
        for j in range(n):
            matrix[i].append(num[i * n + j])
            
    # print(len(matrix[0]))
    # res = ''
    # for i in range(m):
    #     for j in range(n):
    #         res += str(matrix[m][n]) + ' '
    # print(res)
    res = []
    while matrix:
        res += matrix.pop(0)
        matrix = list(map(list, zip(*matrix)))[::-1]

    ans = ''
    for i in range(0, len(num)):
        ans += str(res[i]) + ' '
    print(ans)
