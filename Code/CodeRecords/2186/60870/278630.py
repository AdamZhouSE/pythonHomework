num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    res = 0
    for j in range(1, num + 1):
        acc = 0
        for k in range(1, j + 1):
            acc = acc + k
        res = res + acc
    print(res)