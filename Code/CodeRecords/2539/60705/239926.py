# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 你找到的子数组应是最短的，请输出它的长度。


def minimum(a):
    m = a[0]
    for i in range(0, len(a)):
        if a[i] < m:
            m = a[i]
    return m


def maximum(a):
    m = a[0]
    for i in range(0, len(a)):
        if a[i] > m:
            m = a[i]
    return m


def is_perfect(a):
    if len(a) == 1:
        return True
    perfect = True
    for i in range(0, len(a)-1):
        if a[i+1] < a[i]:
            perfect = False
    return perfect


if __name__ == "__main__":
    a = list(map(int, input()[1:-1].split(",")))
    if is_perfect(a):
        print(0)
    min_len = len(a)
    # 先遍历所有不含a[0]和a[len(a)-1]的子数组
    for i in range(1, len(a)-2):
        for j in range(2, len(a)-1):
            if is_perfect(a[0:i]) and is_perfect(a[j:len(a)]) and j-i+1 < min_len and a[i-1] <= minimum(a[i:j+1]) <= maximum(a[i:j+1]) <= a[j+1]:
                min_len = j - i + 1

    # 再遍历所有含有a[0]但不含a[len(a)-1]的子数组
    for j in range(1, len(a)-1):
        if is_perfect(a[j+1:len(a)]) and maximum(a[0:j+1]) < a[j+1] and j+1 < min_len:
            min_len = j + 1

    # 最后遍历所有不含a[0]但含a[len(a)-1]的子数组
    for i in range(1, len(a)-2):
        if is_perfect(a[0:i]) and a[i-1] <= minimum(a[i:len(a)]) and len(a)-i < min_len:
            min_len = len(a) - i

    # 最后只剩一个全数组了

    print(min_len)
