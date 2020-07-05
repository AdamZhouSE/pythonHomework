def test():
    kn = input().split(',')
    k = int(kn[0])
    n = int(kn[1])
    group = [0] * k
    count = 0
    result = []
    for i in range(1,10):
        add(count, group, i, n, k, result)
    print(result)


def add(count, group, begin, n, k, result):
    if count < k:
        group[count] = begin
        if count+1==k:
            add(count + 1, group, 0, n, k, result)
        else:
            for i in range(begin + 1, 10):
                add(count + 1, group, i, n, k, result)
    else:
        sum = 0
        for j in range(0, k):
            sum = sum + group[j]
        if sum == n:
            okset=list(group)
            result.append(okset)

test()