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

def solve():
    line1 = list(map(int,input().split(' ')))
    n = line1[0]
    root = line1[1]
    line2 = list(map(int,input().split(' ')))
    data = []

    for j in range(0, n - 1):
        line = list(map(int, input().split(' ')))
        data.append(line)

    def pre_order(r,l_node,r_node):
        final = []
        final.append(r)

        if len(l_node) == 0:
            a = 0
        elif len(l_node) == 1:
            final.append(l_node[0][0])
        elif len(l_node) == 2:
            final.append(l_node[0][0])
            final.append(l_node[1][0])
        elif len(l_node) == 3 and l_node[0][1] != 0 and l_node[0][2] != 0:
            final.append(l_node[0][0])
            final.append(l_node[0][1])
            final.append(l_node[0][2])
        else:
            tmp = left_list(l_node[0], l_node[1:])
            index = tmp.index('+')
            left = tmp[:index]
            right = tmp[index + 1:]
            final += pre_order(l_node[0][0], left, right)

        if len(r_node) == 0:
            a = 0
        elif len(r_node) == 1:
            final.append(r_node[0][0])
        elif len(r_node) == 2:
            final.append(r_node[0][0])
            final.append(r_node[1][0])
        elif len(r_node) == 3 and r_node[0][1] != 0 and r_node[0][2] != 0:
            final.append(r_node[0][0])
            final.append(r_node[0][1])
            final.append(r_node[0][2])
        else:
            tmp = left_list(r_node[0], r_node[1:])
            index = tmp.index('+')
            left = tmp[:index]
            right = tmp[index + 1:]
            final += pre_order(r_node[0][0], left, right)
        return final

    def in_order(r,l_node,r_node):
        final = []

        if len(l_node) == 0:
            a = 0
        elif len(l_node) == 1:
            final.append(l_node[0][0])
        elif len(l_node) == 2:
            if l_node[0][2] == 0:
                final.append(l_node[1][0])
                final.append(l_node[0][0])
            elif l_node[0][1] == 0:
                final.append(l_node[0][0])
                final.append(l_node[1][0])
        elif len(l_node) == 3 and l_node[0][1] != 0 and l_node[0][2] != 0:
            final.append(l_node[0][1])
            final.append(l_node[0][0])
            final.append(l_node[0][2])
        else:
            tmp = left_list(l_node[0],l_node[1:])
            index = tmp.index('+')
            left = tmp[:index]
            right = tmp[index+ 1:]
            final += in_order(l_node[0][0],left,right)

        final.append(r)

        if len(r_node) == 0:
            a = 0
        elif len(r_node) == 1:
            final.append(r_node[0][0])
        elif len(r_node) == 2:
            if r_node[0][2] == 0:
                final.append(r_node[1][0])
                final.append(r_node[0][0])
            elif r_node[0][1] == 0:
                final.append(r_node[0][0])
                final.append(r_node[1][0])
        elif len(r_node) == 3 and r_node[0][1] != 0 and r_node[0][2] != 0:
            final.append(r_node[0][1])
            final.append(r_node[0][0])
            final.append(r_node[0][2])
        else:
            tmp = left_list(r_node[0], r_node[1:])
            index = tmp.index('+')
            left = tmp[:index]
            right = tmp[index + 1:]
            final += in_order(r_node[0][0], left, right)
        return final

    def post_order(r,l_node,r_node):
        final = []

        if len(l_node) == 0:
            a = 0
        elif len(l_node) == 1:
            final.append(l_node[0][0])
        elif len(l_node) == 2:
            final.append(l_node[1][0])
            final.append(l_node[0][0])
        elif len(l_node) == 3 and l_node[0][1] != 0 and l_node[0][2] != 0:
            final.append(l_node[0][1])
            final.append(l_node[0][2])
            final.append(l_node[0][0])
        else:
            tmp = left_list(l_node[0], l_node[1:])
            index = tmp.index('+')
            left = tmp[:index]
            right = tmp[index + 1:]
            final += post_order(l_node[0][0], left, right)

        if len(r_node) == 0:
            a = 0
        elif len(r_node) == 1:
            final.append(r_node[0][0])
        elif len(r_node) == 2:
            final.append(r_node[1][0])
            final.append(r_node[0][0])
        elif len(r_node) == 3 and r_node[0][1] != 0 and r_node[0][2] != 0:
            final.append(r_node[0][1])
            final.append(r_node[0][2])
            final.append(r_node[0][0])
        else:
            tmp = left_list(r_node[0], r_node[1:])
            index = tmp.index('+')
            left = tmp[:index]
            right = tmp[index + 1:]
            final += post_order(r_node[0][0], left, right)

        final.append(r)
        return final

    first = left_list(line2, data)
    plus_index = first.index('+')
    lch = first[:plus_index]
    rch = first[plus_index + 1:]

    order_pre = pre_order(root,lch,rch)
    for m in range(0,n):
        print(order_pre[m],end = ' ')
    print()

    order_in = in_order(root,lch,rch)
    for m in range(0,n):
        print(order_in[m],end = ' ')
    print()

    order_post = post_order(root,lch,rch)
    for m in range(0,n - 1):
        print(order_post[m],end = ' ')
    print(order_post[n - 1])
solve()
