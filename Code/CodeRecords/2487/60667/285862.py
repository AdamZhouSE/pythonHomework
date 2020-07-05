t = int(input())
for i in range(t):
    n = int(input())
    li = list(input().split())
    uni = []
    counting = []
    for j in li:
        if j not in uni:
            uni.append(j)
    for j in uni:
        counting.append(li.count(j))
    print(uni[counting.index(max(counting))], max(counting))