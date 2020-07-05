import re

num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    limit = 0
    j = 2
    while True:
        if pow(2, j) - 2 >= num:
            limit = j
            break
        j = j + 1
    bitNum = limit - 1
    length = int(pow(2, bitNum))
    order = num - int(pow(2, bitNum)) + 2
    valid_list = []
    while length > 1:
        if order % length == 0 or order % length > int(length / 2):
            valid_list.append('7')
            length = int(length / 2)
            order = int(order / 2)
        else:
            valid_list.append('4')
            length = int(length / 2)
    res = ''.join(valid_list)
    print(res)