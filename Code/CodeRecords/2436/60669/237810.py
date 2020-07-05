def merge(intervals):
    result = []
    if len(intervals) == 0:
        return []
    if len(intervals) == 1:
        return intervals

    # 先排序,降低复杂度
    intervals = sorted(intervals, key=lambda x: x[0])

    left = intervals[0][0]  # 记录字区间左边界
    right = intervals[0][1]  # 用于记录子区间的右边界

    for i in range(1, len(intervals)):
        if right >= intervals[i][0]:
            right = max(intervals[i][1], right)  # 取当前右边区间和之前记录的right右区间的值谁#大,取较大值
        else:
            result.append([left, right])
            left = intervals[i][0]
            right = intervals[i][1]
    result.append([left, right])

    return result


arr=eval(input())
intervals=eval(input())
arr.append(intervals)
print(merge(arr))