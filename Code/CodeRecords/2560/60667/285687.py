t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    m = int(input())
    uni = []
    counting = []
    for j in li:
        if j not in uni:
            uni.append(j)
    for j in uni:
        counting.append(li.count(j))
    counting.sort()
    result = len(uni)
    for j in counting:
        if m >= j:
            m = m - j
            result -= 1
        else:
            break
    print(result)