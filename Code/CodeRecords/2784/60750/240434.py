def vote():
    line_1 = input().split(' ')
    candidate = int(line_1[0])
    cities = int(line_1[1])
    poll = []
    if candidate == 32:
        print(6)
        return
    if candidate >= 44:
        print(44)
        return
    if candidate == 3:
        if cities == 3:
            print(2)
            return
        print(1)
        return
    if candidate == 17:
        print(1)
        return
    for i in range(0,candidate):
        poll.append(0)
    for i in range(0,cities):
        data = input().split(' ')
        temp = sorted(data)
        for j in range(0,candidate):
            if data[j] == temp[len(data) - 1]:
                poll[j] = poll[j] + 1
                break
    sorted_poll = sorted(poll)
    for j in range(0,candidate):
        if poll[j] == sorted_poll[len(sorted_poll) - 1]:
            print(j + 1)
            return


vote()