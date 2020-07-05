# 交换数组a的第i个元素和第j个元素
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


# 判断a是否已经满足题意
def is_perfect(a):
    perfect = True
    for i in range(0, len(a), 2):
        if abs(a[i] - a[i+1]) > 1:
            perfect = False
    return perfect


if __name__ == '__main__':
    a = list(map(int, input()[1:-1].split(",")))
    b = sorted(a)
    count = 0
    while not is_perfect(a):
        for i in range(0, len(a), 2):
            if a[i] % 2 == 0:  # a[i]是偶数，a[i+1]应为a[i] + 1
                if a[i+1] != a[i] + 1:
                    for j in range(0, len(a)):
                        if a[j] == a[i] + 1:
                            swap(a, i+1, j)
                            count += 1
            else:  # a[i] 是奇数，a[i+1]应为 a[i] - 1
                if a[i+1] != a[i] - 1:
                    for j in range(0, len(a)):
                        if a[j] == a[i] - 1:
                            swap(a, i+1, j)
                            count += 1
    print(count)
