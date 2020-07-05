def get_index(s, n):
    for index, ss in enumerate(s):
        if ss == n:
            return index


def run(s):
    l = s[1:-1].split(', ')
    count = 0
    for i in range(0, len(l), 2):
        position = get_index(l, str(i))  # i的位置坐标
        position_1 = get_index(l, str(i + 1))
        if position % 2 == 1:
            if position - 1 == position_1:
                continue
            l[position - 1], l[position_1] = l[position_1], l[position - 1]
            count += 1
        else:
            if position + 1 == position_1:
                continue
            l[position + 1], l[position_1] = l[position_1], l[position + 1]
            count += 1
        #print(str(l))
    return count


print(run(input()))
