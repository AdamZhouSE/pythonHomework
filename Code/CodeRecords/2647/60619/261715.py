def get_tree(k):
    if k == 1:
        return 1
    elif k == 0:
        return 0
    else:
        n = 0
        while 2**n <= k:
            n += 1
        return 1 + get_tree(k - 2**(n-1))


t = int(input())
for ind in range(t):
    target = int(input())
    print(get_tree(target))
