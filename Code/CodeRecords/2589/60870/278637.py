def lucas(num):
    if num == 0:
        return 2
    elif num == 1:
        return 1
    return lucas(num - 1) + lucas(num - 2)


num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    print(lucas(num))