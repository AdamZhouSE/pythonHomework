def s29():
    nums = list(eval(input()))
    lists = []

    def permutation(num, p, q):
        if p == q:
            lists.append(list(num))
        else:
            for i in range(p, q):
                num[i], num[p] = num[p], num[i]
                permutation(num, p + 1, q)
                num[i], num[p] = num[p], num[i]

    permutation(nums, 0, len(nums))
    lists = list(set([tuple(t) for t in lists]))
    lists = [list(v) for v in lists]

    count = 0
    for s in lists:
        flag = True
        if len(s) == 1:
            continue
        for i in range(0, len(s)-1):
            if ((s[i] + s[i+1]) ** 0.5) % 1 != 0:
                flag = False
                break
        if flag:
            count = count + 1

    print(count)


s29()