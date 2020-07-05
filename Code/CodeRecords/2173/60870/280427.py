num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    acc_list = []
    for j in range(1, num + 1):
        acc_list.append(j * j)
    res = 0
    for ch in acc_list:
        res = res + ch
    print(res)