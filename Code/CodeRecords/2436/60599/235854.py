s=list(eval(input()))
k=list(eval(input()))
s.append(k)

#以上代码将arr变成list
intervals=s
if len(intervals) == 0:
    print([])
    exit()

res = []
intervals = list(sorted(intervals))

low = intervals[0][0]
high = intervals[0][1]

for i in range(1, len(intervals)):
    # 若当前区间和目前保存区间有交集，则进行判断后修改相应的区间参数；若当前区间和目前保存区间没有交集，则将目前保存区间放入到结果集合中，并将当前区间记录成目前保存区间
    if high >= intervals[i][0]:
        if high < intervals[i][1]:
            high = intervals[i][1]
    else:
        res.append([low, high])
        low = intervals[i][0]
        high = intervals[i][1]

res.append([low, high])
print(res)
