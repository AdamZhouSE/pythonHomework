time = eval(input())
res = 123456
for x in range(len(time)):
    for y in range(x + 1, len(time)):
        hour1, min1 = map(int, time[x].split(':'))
        #print(hour1, min1)
        hour2, min2 = map(int, time[y].split(':'))
        #print(hour2, min2)
        hour = hour1 - hour2
        minute = min1 - min2
        #print(hour, minute)
        if hour <= 0:
            hour = - hour
        if minute <= 0:
            minute = -minute
        tem = 0
        if hour >= 12:
            tem = (24 - hour) * 60 - minute
        else:
            tem = hour * 60 + minute
        if tem < res:
            res = tem
print(res)