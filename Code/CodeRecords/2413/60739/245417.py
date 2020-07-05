def circularPermutation(n, start):
    res = list()
    for i in range(1 << n):
        res.append(i ^ (i >> 1))
    while res[0] != start:
        res.append(res.pop(0))
    return res


if __name__ == '__main__':
    n = int(input())
    start = int(input())
    a = circularPermutation(n, start)
    print(a);
