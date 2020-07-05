All = int(input())

for q in range(0, All):
    length = int(input())
    ar = list(map(int, input().split()))
    ar.sort()
    k = int(input())
    count = 0
    diff = list(set(ar))

    if k == 0:
        for x in diff:
            if ar.count(x) > 1:
                count += 1
    else:
        i = 0
        j = 1
        num = len(diff)
        while j < num:
            if diff[j] - diff[i] == k:
                count += 1
                i += 1
            j += 1
    print(count)