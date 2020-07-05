def training():
    n = int(input())
    ls = input().split(' ')
    ls = list(map(int, ls))
    ls.sort()
    k = 1
    for i in ls:
        if i < k:
            continue
        else:
            k += 1
    return k - 1


print(training())