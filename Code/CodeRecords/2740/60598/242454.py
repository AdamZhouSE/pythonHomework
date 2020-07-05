times = input()[1:-1].split(",")


def cal(time1,time2):
    minutes1 = int(time1[0:2])*60+int(time1[3:5])
    minutes2 = int(time2[0:2])*60+int(time2[3:5])
    forward = max(minutes2, minutes1) - min(minutes1, minutes2)
    reverse = 1440-max(minutes2, minutes1) + min(minutes1, minutes2)
    return min(forward, reverse)


Min = 1440
for i in range(len(times)):
    for j in range(i+1, len(times)):
        Min = min(cal(times[i][1:-1], times[j][1:-1]), Min)
print(Min)

