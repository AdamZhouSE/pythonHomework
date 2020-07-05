def winner():
    count = int(input())
    record = []
    name_set = []
    for i in range(count):
        ls = input().split(' ')
        if ls[0] not in name_set:
            name_set.append(ls[0])
        record.append(ls)
    score = [0] * len(name_set)
    win = name_set[0]
    for i in record:
        index = name_set.index(i[0])
        score[index] += int(i[1])
        if score[index] > score[name_set.index(win)]:
            win = i[0]
    return win


print(winner())