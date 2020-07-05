def func1():
    a = input()[1:-1]
    intervals = []
    i = 0
    while i < len(a):
        temp = ""
        if a[i] == "[":
            j = i
            while True:
                if a[j] == "]":
                    i = j+2
                    break
                j += 1
                temp += a[j]
        intervals.append(list(map(int, temp[:-1].split(","))))
    ans = []
    intervals.sort(key= lambda x:x[0])
    i = 0
    while i < len(intervals):
        left = intervals[i][0]
        right = intervals[i][1]
        while i+1 <= len(intervals)-1 and intervals[i+1][0] <= right:
            right = max(right, intervals[i+1][1])
            i += 1
        ans.append([left, right])
        i += 1
    print(ans)
    return
func1()