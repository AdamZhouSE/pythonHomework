pre_order = ""
in_order = ""


def post_order(l1, l2, r1, r2):
    if l1 > r1 or r1 > len(pre_order)-1 or r2 > len(in_order)-1:
        return
    cnt = 0
    i = l2
    while pre_order[l1] != in_order[i]:
        cnt += 1
        i += 1
    post_order(l1+1, l2, l1+cnt, l2+cnt-1)
    post_order(l1+cnt+1, l2+cnt+1, r1, r2)
    print(pre_order[l1], end='')


if __name__ == '__main__':
    try:
        while True:
            pre_order = input()
            in_order = input()
            post_order(0, 0, pre_order.__len__()-1, in_order.__len__()-1)
            print()
    except EOFError:
        pass
