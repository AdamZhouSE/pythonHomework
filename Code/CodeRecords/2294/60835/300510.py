def solve(pre_order, in_order):
    if len(pre_order) <= 1:
        return pre_order
    node = pre_order[0]
    index = in_order.index(node)
    left_in = in_order[0: index]
    right_in = in_order[index + 1: len(in_order)]
    index = pre_order.index(right_in[0])
    left_pre = pre_order[1: index]
    right_pre = pre_order[index: len(pre_order)]
    return solve(left_pre,left_in) + solve(right_pre,right_in) + node
pre_order = input()
in_order = input()
print(solve(pre_order, in_order))
pre_order = input()
in_order = input()
print(solve(pre_order, in_order))