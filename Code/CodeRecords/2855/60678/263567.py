def goodTogo(nums, i, j):
    #     判断i, j 上下左右是否有偶数个o
    count = 0
    n = len(nums)

    # 上
    if i > 0 and nums[i - 1][j] == 'o':
        count += 1

    # 下
    if i < n - 1 and nums[i + 1][j] == 'o':
        count += 1

    # 左
    if j > 0 and nums[i][j - 1] == 'o':
        count += 1

    # right
    if j < n - 1 and nums[i][j + 1] == 'o':
        count += 1

    if count % 2 == 0:
        return True
    return False


def judge():
    n = int(input())
    table = []
    for i in range(0, n):
        table.append(input())
    for i in range(0, n):
        for j in range(0, n):
            if not goodTogo(table, i, j):
                print('NO')
                return
    print('YES')
    return


if __name__ == '__main__':
    judge()