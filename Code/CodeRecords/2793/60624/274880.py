def func33():
    temp = list(map(int, input().split(" ")))
    time_limit = temp[1]
    times = list(map(int, input().split(" ")))
    res = 1
    for i in range(1,len(times)):
        if times[i]-times[i-1] > time_limit:
            res = 1
        else:
            res += 1
    if time_limit == 0:
        print(0)
    else:
        print(res)
    return
func33()