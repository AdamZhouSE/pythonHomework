# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 你找到的子数组应是最短的，请输出它的长度。
def minimun(a):
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
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if i == 0 and j < len(a) and maximum(a[i:j])<a[j] and is_perfect(a[j:len(a)-1]) and  j-i < min_len:
                min_len = j - i
            elif j == len(a) -1 and i >= 1 and minimun(a[i:j]) > a[i-1] and is_perfect(a[0:i]) and j-i < min_len:
                min_len = j - i
            elif i > 0 and j<len(a)-1 and is_perfect(a[0:i]) and a[i-1] <= minimun(a[i:j]) <= maximum(a[i:j]) <= a[j] and j - i <= min_len:
                min_len = j - i
            
    print(min_len)
    