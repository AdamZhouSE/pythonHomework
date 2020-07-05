T = int(input())
for i in range(0, T):
    n, m, l, r = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    times = dict()
    for item in nums:
        if item in times:
            times[item] += 1
        else:
            times[item] = 1
    temp = []
    for j in range(l, r + 1):
        if j in times:
            temp.append(times[j])
        else:
            temp.append(0)
    for j in range(0, m):
        temp[temp.index(min(temp))] += 1
    ans = 1
    for item in times:
        if item not in range(l, r + 1):
            for j in range(1, times[item] + 1):
                ans = ans * j
    for item in temp:
        for j in range(1, item + 1):
            ans = ans * j
    temp = 1
    for j in range(1, n + m + 1):
        temp = temp * j
    print(temp // ans % 998244353)
