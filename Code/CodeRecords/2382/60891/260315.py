
def combine(re_list=[[1, 4]], new=[2, 3]):
    old = re_list.pop()
    if new[0] <= old[1]:
        if new[1] <= old[1]:
            re_list.append(old)
        else:
            re_list.append([old[0], new[1]])
    else:
        re_list.append(old)
        re_list.append(new)
    return re_list


n = int(input())
interval_list = []
num_list = []
for i in range(n):
    inp = input().split()
    interval_list.append([int(j) for j in inp])
interval_list.sort()
re_intv_list = [interval_list[0]]
for i in range(n - 1):
    combine(re_intv_list, interval_list[i + 1])
for i in re_intv_list:
    print("{} {}".format(i[0], i[1]))
