intervals=eval(input())
add=eval(input())

intervals.append(add)

if len(intervals)<=1:
    print(intervals)
else:
    intervals = sorted(intervals, key=lambda a: a[0])
    l = intervals[0][0]
    h = intervals[0][1]
    res = []
    for i in range(1, len(intervals)):
        if intervals[i][0] > h:
            res.append([l, h])
            l = intervals[i][0]
            h = intervals[i][1]
        else:
            h = max(h, intervals[i][1])
    res.append([l, h])
    print(res)