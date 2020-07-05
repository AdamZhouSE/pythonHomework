def func16():
    n = int(input())
    cur = 0
    intervals = []
    while cur < n:
        temp = list(map(int, input().split(",")))
        temp.append(cur)
        intervals.append(temp)
        cur += 1
    intervals.sort(key=lambda x:x[0])

    ans = list(range(len(intervals)))
    for i in range(0,len(intervals)-1):
        flag = True
        for j in range(i+1, len(intervals)):
            if intervals[j][0] >= intervals[i][1]:
                ans[intervals[i][2]] = intervals[j][2]
                flag = False
                break

        if flag:
            ans[intervals[i][2]] = -1

    ans[intervals[len(intervals)-1][2]] = -1
    print(ans)
    return
func16()