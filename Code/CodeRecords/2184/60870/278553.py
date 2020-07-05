num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    acc = -1
    res = 0
    for j in range(num):
        acc = acc + 4
        res = res + acc
    print(res)