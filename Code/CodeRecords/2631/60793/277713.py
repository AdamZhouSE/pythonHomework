def max_nums(ls0: list) -> list:
    max_num = -999
    result1 = []
    for x in ls0:
        if x > max_num:
            result1 = [ls0.index(x)]
            max_num = x
        elif x == max_num:
            result1.append(ls0.index(x))
    return result1


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
print(log)

'''[[1, 1, 2], [4, 2, -1], [7, 3, 3], [9, 3, -1]]'''