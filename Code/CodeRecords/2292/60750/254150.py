def left_list(root_l_r, total):
    i = 0
    j = 0
    lch_root = root_l_r[1]
    rch_root = root_l_r[2]
    l_list = []
    r_list = []

    while i < len(total):
        if total[i][0] == lch_root:
            break
        i += 1
    while j < len(total):
        if total[j][0] == rch_root:
            break
        j += 1
    if i == 0:
        l_list = total[:j]
        if j < len(total):
            r_list = total[j:]
    if j == 0:
        r_list = total[:i]
        if i < len(total):
            l_list = total[i:]
    return l_list + ['+'] + r_list

def topology(nodes):
    res = 0
    if len(nodes) == 0:
        return 0
    if len(nodes) == 1:
        return 1
    if len(nodes) == 2:
        if nodes[0][1] <nodes[0][0] <nodes[0][2]:
            return 2
        if nodes[0][1] < nodes[0][0] and nodes[0][2] == 0:
            return 2
        else:
            return 1
    if len(nodes) == 3:
        if nodes[0][1] == nodes[1][0] and nodes[0][2] == nodes[2][0]:
            if nodes[0][1] <nodes[0][0] <nodes[0][2]:
                return 3
            elif nodes[0][1] < nodes[0][0]:
                return 2
            elif nodes[0][2] > nodes[0][0]:
                return 2
            else:
                return 1
        if nodes[0][1] == 0 and nodes[0][0] <nodes[0][2]:
            return 1 + topology(nodes[1:])
        if nodes[0][2] == 0 and nodes[0][0] >nodes[0][1]:
            return 1 + topology(nodes[1:])
        else:
            return 1

    root_line = nodes[0]
    if root_line[1] == 0:
        if root_line[0] < root_line[2]:
            return 1 + topology(nodes[1:])
        else:
            return 1
    if root_line[2] == 0:
        if root_line[0] > root_line[1]:
            return 1 + topology(nodes[1:])
        else:
            return 1
    tmp = left_list(root_line,nodes[1:])
    index = tmp.index('+')
    lch = tmp[:index]
    rch = tmp[index + 1:]
    if root_line[1] < root_line[0] <root_line[2]:
        return 1 + topology(lch) + topology(rch)
    if root_line[1] < root_line[0]:
        return 1 + topology(lch)
    if root_line[2] > root_line[0]:
        return 1 + topology(rch)
    else:
        return 1

def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    root = line1[1]
    data = []
    res = []
    lch = []
    rch = []
    for i in range(0,n):
        data.append(list(map(int,input().split(' '))))

    print(topology(data))

solve()