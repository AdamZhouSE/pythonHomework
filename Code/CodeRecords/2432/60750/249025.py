
def solve(in_order,post_order):
    length = len(in_order)
    if length == 0:
        return 10000
    if length == 1:
        return in_order[0]
    if length == 2:
        return post_order[0]
    if length == 3 and post_order[2] == in_order[1]:
        return min(post_order[0],post_order[1])

    if in_order[length - 1] == post_order[length - 1]:
        return solve(in_order[:length - 1],post_order[:length - 1])
    else:
        index = in_order.index(post_order[length - 1])
        left = solve(in_order[:index],post_order[:index])
        right = solve(in_order[index + 1:],post_order[index:length - 1])
        return min(left,right)


in_order = list(map(int,input().split(' ')))
post_order = list(map(int,input().split(' ')))
print(solve(in_order,post_order))