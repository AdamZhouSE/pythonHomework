list1 = input().split(",")
list1 = [int(i) for i in list1]


def clockwise(list_1: list):
    temp = list_1[len(list_1) - 1]
    list_1 = list_1[0:len(list_1) - 1]
    list_1.insert(0, temp)
    return list_1


def f(list_2: list) -> int:
    res = 0
    for i in range(len(list_2)):
        res += i * list_2[i]
    return res


max_num = f(list1)
for j in range(1, len(list1)):
    list1 = clockwise(list1)
    ans = f(list1)
    if ans > max_num:
        max_num = ans
print(max_num)