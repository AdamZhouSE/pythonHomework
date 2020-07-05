def linerlist_4_pr(n):
    co = []
    re = n
    co.append(re)
    if re > 0:
        re -= 5
        co.append(re)
    else:
        re += 5
        co.append(re)
    while re != n:
        if re > 0:
            re -= 5
        else:
            re += 5
        co.append(re)
    for i in range(len(co) - 1):
        print(co[i], end=' ')
    print(co[len(co) - 1])


if __name__ == '__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_4_pr(int(n))