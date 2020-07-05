# string 12
def test():
    schedule = list(eval(input()))
    for i in range(0, len(schedule)):
        hm = schedule[i].split(':')
        hours = int(hm[0])
        minutes = int(hm[1])
        schedule[i] = hours * 60 + minutes
    minimum = 1440
    for i in range(0, len(schedule) - 1):
        for j in range(i + 1, len(schedule)):
            time_diff = diff(schedule[i], schedule[j])
            if time_diff < minimum:
                minimum = time_diff
    print(minimum)


def diff(time1, time2):
    if abs(time1 - time2) > 720:
        return 1440 - abs(time1 - time2)
    else:
        return abs(time1-time2)


test()