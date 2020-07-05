def get_indexes(a, b, c):
    res = 0
    for i in range(len(a)):
        if str(int(a[i]) - int(b[i])) in c:
            res += 1
    return res


if __name__ == '__main__':
    result = []
    for i in range(int(input())):
        a = input()
        result.append(get_indexes(input().split(), input().split(), input().split()))
    for i in range(len(result)):
        print(result[i])