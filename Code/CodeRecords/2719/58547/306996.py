def func():
    op_num = int(input())

    i = 0
    schedule = {}  # time_point: id   means who occupy the time point
    available = []  # store available ids
    expired = []  # store expired ids
    unique_id = 1
    while i < op_num:
        op = input()

        if op == "B":
            print(len(available))
        else:
            op = op.split()
            start = int(op[1])
            end = int(op[2])

            expire_num = 0
            now_time = start
            while now_time <= end:
                if now_time in schedule.keys():
                    if schedule[now_time] in expired:
                        schedule[now_time] = unique_id
                    else:
                        expire_num += 1
                        expired.append(schedule[now_time])
                        available.remove(schedule[now_time])
                        schedule[now_time] = unique_id
                else:
                    schedule[now_time] = unique_id
                now_time += 1

            available.append(unique_id)
            unique_id += 1
            print(expire_num)

        i += 1


func()
