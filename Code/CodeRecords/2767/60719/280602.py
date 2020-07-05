def point_cal(tar):
    if tar > 15:
        last = point_cal(tar-15)
        if last == 0:
            return 0
        return 3 + last
    while tar % 5 != 0:
        tar -= 3
    if tar == 15:
        return 3
    if tar == 10:
        return 2
    if tar < 0:
        return 0
    return 1


def handle_each_use_case():
    tar = int(input())
    return point_cal(tar)


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)
