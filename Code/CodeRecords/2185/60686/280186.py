nums = int(input())
list_all = []
for i in range(nums):
    num = int(input())
    list_all.append(num)
for i in range(nums):
    num = list_all[i]
    limit = 0
    j = 2
    while 1:
        if pow(2, j) - 2 >= num:
            limit = j
            break
        j += 1
    bitNum = limit - 1
    length = int(pow(2, bitNum))
    order = num - int(pow(2, bitNum)) + 2
    valid_list = []
    while length > 1:
        if order % length == 0 or order % length > int(length / 2):
            valid_list.append("7")
            length = int(length / 2)
        else:
            valid_list.append("4")
            length = int(length / 2)
    res = ''.join(valid_list)
    print(res)
