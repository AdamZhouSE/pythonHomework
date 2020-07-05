def count_diff(this_sum, num_lst):
    res = 0
    while len(num_lst) != 0:
        if num_lst[0] > this_sum:
            break
        elif num_lst[0] == this_sum:
            res += 1
        else:
            res += count_diff(this_sum - num_lst[0], num_lst[1:])
        num_lst.pop(0)
    return res


ts = int(input())
lst = []
for t in range(ts):
    n = int(input())
    lst.append(sorted(list(map(int, input().split(' ')))))
    add_sum = int(input())
    print(count_diff(add_sum, lst[t]))
