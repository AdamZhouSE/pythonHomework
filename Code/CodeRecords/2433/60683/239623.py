intervals = eval(input())
intervals = list(sorted(intervals, key=lambda x: x[0]))
n = len(intervals)
res = []
res.append(intervals[0])
curN = 1
for i in range(1, n):
    j = 0
    while j < curN:
        if intervals[i][0] <= res[j][1]:
            res[j][1] = max(intervals[i][1], res[j][1])
            break
        j += 1
    if j == curN:
        res.append(intervals[i])
        curN += 1
print(res)