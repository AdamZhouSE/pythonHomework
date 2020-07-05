import math

t = int(input())
result = []
for i in range(t):
    n, m, l, r = map(int, input().split(' '))
    data = list(map(int, input().strip().split(' ')))
    ad = [x for x in range(l, r + 1)]  # 要添加的数
    times = [0 for x in range(r - l + 1)]  # ad中的数在原数据中出现的次数
    for j in range(len(ad)):
        times[j] = data.count(ad[j])  # 统计出现次数
    for j in range(m):
        index = times.index(min(times))
        tmp = ad[index]
        data.append(tmp)
        times[index] += 1
    total = math.factorial(n + m)
    sup = []  # 统计添加结束后各数字出现的次数
    nums = list(set(data))
    for j in nums:
        sup.append(data.count(j))
    atom = 1
    for j in sup:
        atom *= math.factorial(j)
    result.append((total // atom) % 998244353)
for i in result:
    print(i)
