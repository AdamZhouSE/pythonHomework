num_test = int(input())
info_list = []
for i in range(num_test):
    num = int(input())
    info = input().split()
    info_list.append(info)
for i in range(num_test):
    info = info_list[i]
    res = num_test
    for ch in info:
        res = res + ch
    print(res)