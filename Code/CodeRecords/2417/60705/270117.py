def has_same_divisor(a, b):
    for i in range(2, min(a, b)):
        if a % i == b % i == 0:
            return True
    return False


def solve(li):
    for i in range(0, len(li)):
        for j in range(i+1, len(li)):
            if not has_same_divisor(li[i], li[j]):
                return True
    return False


if __name__ == '__main__':
    li = list(map(int, input().split(",")))
    if li == [1]:
        print(True)
    else:
        print(solve(li))
