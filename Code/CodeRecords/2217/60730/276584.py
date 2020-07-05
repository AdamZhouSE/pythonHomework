from itertools import permutations

num = 4
test = [[None] * 4] * 4  # 把六条线长度平方算出来，如果有4条是相等的，且剩余两条是这四条的两倍，
tmp = []
for i in range(num):
    test[i] = eval(input())


def dis(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


tmp.append(dis(test[0], test[1]))
tmp.append(dis(test[0], test[2]))
tmp.append(dis(test[0], test[3]))
tmp.append(dis(test[2], test[1]))
tmp.append(dis(test[3], test[1]))
tmp.append(dis(test[2], test[3]))
tmp.sort()
if tmp[0] != 0 and tmp[1] == tmp[0] and tmp[2] == tmp[1] and tmp[3] == tmp[2] and tmp[4] == tmp[3] * 2 and tmp[5] == \
        tmp[4]:
    print("True")
else:
    print("False")
