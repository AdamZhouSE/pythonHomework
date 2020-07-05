


T = int(input())
for t in range(T):
    n = int(input())
    nums = [int(x) for x in input().split(' ')]
    all = []
    count = []
    printed = False
    for x in nums:
        if x not in all:
            all.append(x)
            count.append(1)
        else:
            count[all.index(x)] += 1
    for i in range(len(count)):
        if count[i] > n // 2:
            printed = True
            print(all[i])
            break
    if not printed:
        print(-1)
