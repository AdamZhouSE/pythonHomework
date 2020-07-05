import sys

def post_order(pre_str,in_str):
    if len(pre_str) == 1:
        return pre_str
    if len(pre_str) == 2:
        return pre_str[1] + pre_str[0]

    root = pre_str[0]
    position = in_str.index(root)
    if len(pre_str) == 3:
        if position == 1:
            return pre_str[1] + pre_str[2] + pre_str[0]
        else:
            return pre_str[2] + pre_str[1] + pre_str[0]

    if position == 0:
        return post_order(pre_str[1:],in_str[1:]) + root
    if position == len(pre_str) - 1:
        return post_order(pre_str[1:],in_str[:len(pre_str) - 1]) + root
    else:
        return post_order(pre_str[1:position + 1],in_str[:position]) + post_order(pre_str[position + 1:],in_str[position + 1:]) + root

def solve():
    res = []
    lines = sys.stdin.readlines()
    read_one = False
    pre_line = ''
    in_line = ''

    for data in lines:
        if not read_one:
            pre_line = data.strip()
            read_one = True
            continue
        if read_one:
            in_line = data.strip()
            res.append(post_order(pre_line,in_line))
            read_one = False

    for i in range(0,len(res)):
        print(res[i])

solve()


