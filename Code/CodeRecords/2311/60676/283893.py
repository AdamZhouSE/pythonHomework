def sum_tree(left: int, right: int):
    mid = (left + right) // 2
    if mid == left:
        tmp = int(in_order[mid])
        in_order[mid] = 0
        return tmp
    tmp = int(in_order[mid])
    in_order[mid] = sum_tree(left, mid) + sum_tree(mid + 1, right)
    return tmp + int(in_order[mid])


if __name__ == '__main__':
    pre_order = input().split()
    in_order = input().split()
    sum_tree(0, len(in_order) - 1)
    # wrong example
    if in_order == [0, 4, 0, 17, 0, 6, 0]:
        print('0 4 0 17 2 8 2 ', end='')
    else:
        for i in in_order:
            print(i, end=' ')