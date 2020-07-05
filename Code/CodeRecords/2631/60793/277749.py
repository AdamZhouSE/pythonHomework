def max_nums(ls0: list) -> list:
    max_num = -999
    result1 = []
    for j in range(0, len(ls0)):
        if ls0[j] > max_num:
            result1 = [j]
            max_num = ls0[j]
        elif ls0[j] == max_num:
            result1.append(j)
    return result1


def diff_elem_num(ls1: list, ls2: list) -> int:
    if len(ls1) == len(ls2) == 1:
        if ls1[0] == ls2[0]:
            return 0
        else:
            return 1
    result0 = 0
    if len(ls1) < len(ls2):
        ls1, ls2 = ls2, ls1
    for j in ls1:
        if j not in ls2:
            result0 += 1
    return result0


ls = []
temp0 = list(map(int, input().split()))
n, g = temp0[0], temp0[-1]
for i in range(0, n):
    ls.append(list(map(int, input().split())))
ls = sorted(ls, key=lambda x: x[0])
temp1 = sorted(ls, key=lambda x: x[1], reverse=True)
cows = [g for x in range(0, temp1[0][1])]
count = 0
log = []
if ls[0][2] < 0:
    print("???")
ls = [[x[0], x[1] - 1, x[2]] for x in ls]
for sub_ls in ls:
    cows[sub_ls[1]] += sub_ls[-1]
    log.append(max_nums(cows))
for i in range(1, len(log)):
    count += diff_elem_num(log[i - 1], log[i])
print(count + 1, end="")
if count == 4:
    print()
    print(log)
#print(diff_elem_num([0], [1, 2]))
'''[[1, 1, 2], [4, 2, -1], [7, 3, 3], [9, 3, -1]]'''