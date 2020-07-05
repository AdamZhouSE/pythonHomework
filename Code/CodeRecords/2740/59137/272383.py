def s5():
    times = list(eval(input()))
    ans = 24 * 60
    for i in range(len(times)):
        for j in range(i+1, len(times)):
            hour1 = int(times[i][0:2])
            hour2 = int(times[j][0:2])
            minute1 = int(times[i][3:5])
            minute2 = int(times[j][3:5])
            if hour1 >= hour2:
                dif = min(
                    hour1 * 60 + minute1 - hour2 * 60 - minute2,
                    (hour2 + 24) * 60 + minute2 - hour1 * 60 - minute1
                )
            else:
                dif = min(
                    hour2 * 60 + minute2 - hour1 * 60 - minute1,
                    (hour1 + 24) * 60 + minute1 - hour2 * 60 - minute2
                )
            if dif < ans:
                ans = dif
    print(ans)


s5()