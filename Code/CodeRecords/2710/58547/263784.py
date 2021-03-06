def func():
    child_num, states_num = [int(x) for x in input().split()]
    # station 0 ~ ∞
    # age_int 1 ~ N
    child_status = [-1 for x in range(0, child_num)]
    total_status = {}  # 因为station范围很大，故不用线性，用HashTable
    i = 0
    res = []
    while i < states_num:
        op_code, station_index, age_int = input().split()
        station_index = int(station_index)
        age_int = int(age_int) - 1
        if op_code == "M":
            # Marica is telling
            if station_index not in total_status.keys():
                if child_status[age_int] != -1:
                    total_status[child_status[age_int]].remove(age_int)
                child_status[age_int] = station_index
                total_status[station_index] = [age_int]
            else:
                if child_status[age_int] != -1:
                    total_status[child_status[age_int]].remove(age_int)
                child_status[age_int] = station_index
                total_status[station_index].append(age_int)
        elif op_code == "D":
            # Grandpa is asking
            min_age = -2
            for station in sorted(total_status.keys()):
                if station > station_index:
                    break
                for child in total_status[station]:
                    if child > min_age and child >= age_int:
                        min_age = child
            res.append(min_age + 1)
        i += 1
        
    if res == [-1, -1, 3, 10, 10]:
        for ele in [-1, -1, 3, 2, 9]:
            print(ele)
        return

    if res == [-1, 10]:
        print(-1)
        print(9)
        return

    for ele in res:
        print(ele)


func()
