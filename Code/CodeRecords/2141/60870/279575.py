def toBinary(num):
    binary = []
    while num > 0:
        if num % 2 == 0:
            binary.append('0')
        else:
            binary.append('1')
        num = int(num / 2)
    res = ''.join(binary)
    res = res[::-1]
    return res


num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    str_list = []
    num = num_list[i]
    for j in range(1, num + 1):
        str_list.append(toBinary(j))
    for j in range(len(str_list)):
        if j == len(str_list) - 1:
            print(str_list[j], end = ' ')
        else:
            print(str_list[j], end = ' ')
    print()