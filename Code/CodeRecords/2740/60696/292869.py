def cal_difference(time1:str, time2:str):
    hour1, minute1 = int(time1.split(':')[0]), int(time1.split(':')[1])
    hour2, minute2 = int(time2.split(':')[0]), int(time2.split(':')[1])
    if abs(hour1-hour2)>=12:
        res = 24*60 - abs(hour1*60+minute1-(hour2*60+minute2))
    else:
        res = abs(hour1*60+minute1-(hour2*60+minute2))
    return res


if __name__ == '__main__':
    times = eval(input())
    res = 24*60
    n = len(times)
    for i in range(n-1):
        for j in range(i+1, n):
            res = min(res, cal_difference(times[i], times[j]))
    print(res)
