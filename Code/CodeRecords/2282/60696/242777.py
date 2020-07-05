def has_conflict(arrival_time1, leave_time1, arrival_time2, leave_time2):
    if arrival_time1 == arrival_time2:
        return True
    elif is_earlier(arrival_time1, arrival_time2):
        if arrival_time2 == leave_time1 or is_earlier(arrival_time2, leave_time1):
            return True
        else:
            return False
    else:
        if arrival_time1 == leave_time2 or is_earlier(arrival_time1, leave_time2):
            return True
        else:
            return False


def is_earlier(time1, time2):
    hour1 = int(time1[0:2])
    hour2 = int(time2[0:2])
    minute1 = int(time1[2:4])
    minute2 = int(time2[2:4])
    if hour1 < hour2:
        return True
    elif hour1 > hour2:
        return False
    else:
        if minute1 < minute2:
            return True
        else:
            return False


num_of_example = int(input())
for i in range(num_of_example):
    n = int(input())
    arrival_times = input().split()
    leave_times = input().split()
    platforms = [[0]]
    for j in range(1,n):
        is_enough = False
        for platform in platforms:
            is_able = True
            for train in platform:
                if has_conflict(arrival_times[train],leave_times[train],arrival_times[j],leave_times[j]):
                    is_able = False
                    break
            if is_able:
                platform.append(j)
                is_enough = True
                break
        if not is_enough:
            platforms.append([j])
    print(len(platforms))