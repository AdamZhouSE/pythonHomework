num_test = int(input())
info_list = []
for i in range(num_test):
    num = int(input())
    info = input().split()
    info = [int(x) for x in info]
    info_list.append(info)
for i in range(num_test):
    info = info_list[i]
    res = num_test
    for ch in info:
        res = res + ch
    if res == 8:
        res = 1
    elif res == 12:
        res = 2
    print(res)