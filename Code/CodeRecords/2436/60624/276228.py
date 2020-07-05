def func5():
    a = input()[1:-1]
    intervals = []
    i = 0
    while i < len(a):
        temp = ""
        if a[i] == "[":
            j = i
            while True:
                if a[j] == "]":
                    i = j + 2
                    break
                j += 1
                temp += a[j]
        intervals.append(list(map(int, temp[:-1].split(","))))
    new_interval = list(map(int, input()[1:-1].split(",")))
    i = 0
    length = len(intervals)
    while i < length and new_interval[0] > intervals[i][1]:
        i += 1
    left = i
    while i < length and new_interval[1] >= intervals[i][0]:
        i += 1
    right = i
    if left >= length:
        res = intervals + [new_interval]
    elif left == right:
        intervals.insert(left, new_interval)
        res = intervals
    else:
        res = intervals[:left] + [[min(intervals[left][0],new_interval[0]), max(intervals[right-1][1],new_interval[1])]]+intervals[right:]
    print(res)
    return
func5()