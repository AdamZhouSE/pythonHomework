def point_cal(tar):
    total = 0
    while tar % 5 != 0:
        tar -= 3
    if tar < 0:
        return 0
    if tar == 0:
        return 1
    if tar % 10 == 0:
        total += (2 * point_cal(tar-10))
    if tar % 15 == 0:
        total += (3 * point_cal(tar-15))
    if tar % 10 != 0 and tar % 15 != 0:
        total += point_cal(tar-5)
    return total


def handle_each_use_case():
    tar = int(input())
    return point_cal(tar)


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)
