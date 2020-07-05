a = eval(input())

intervals = sorted(a, key=lambda x: x[0])
res = []
for i in range(len(a)-1):
    if intervals[i][1] >= intervals[i+1][0]:
        res.append([intervals[i][0], intervals[i+1][1]])
    else:
        res.append(intervals[i+1])

print(res)
