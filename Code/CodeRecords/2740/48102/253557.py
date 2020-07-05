def min_time(ls: list) -> int:
    time = []
    res = 2**31-1
    for i in ls:
        time.append([int(i[0:2]), int(i[3:5])])
    time = sorted(time, key=lambda x: [x[0], x[1]])
    for i in range(len(ls)-1):
        res = min(res, time_dis(time[i], time[i+1]))
    res = min(res, time_dis(time[0], time[len(ls)-1]))
    return res


def time_dis(time1: list, time2: list) -> int:
    hour = time2[0] - time1[0]
    minute = (time2[1] - time1[1]) + hour * 60
    if minute > 720:
        return 1440 - minute
    else:
        return minute


lst = eval(input())
print(min_time(lst))