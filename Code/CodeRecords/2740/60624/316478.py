def func12():
    s = input().strip()[1:-1].split(",")
    times = []
    for i in s:
        times.append(i[1:-1])
    MIN = 2000
    for i in range(len(times)-1):
        for j in range(i+1,len(times)):
            if times[i][:2]=="00":
                hour1 = 24
            else:
                hour1 = int(times[i][:2])
            if times[j][:2]=="00":
                hour2 = 24
            else:
                hour2 = int(times[j][:2])
            second1 = int(times[i][3:])
            second2 = int(times[j][3:])
            temp = abs((hour1-hour2)*60+second1-second2)
            MIN = min(MIN,temp)
    print(MIN)
    return
func12()