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
    order = num - int(pow(2, bitNum)) + 2
    valid_list = []
    start = int(pow(10, bitNum - 1))
    end = int(pow(10, bitNum))
    for j in range(start, end):
        str_check = str(j)
        if re.match(r'^[4|7]*$', str_check) is not None:
            valid_list.append(j)
    print(valid_list[order - 1])