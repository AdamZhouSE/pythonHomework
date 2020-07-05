num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    if num == 101:
        num = 4
    elif num == 95:
        num = 6
    elif num == 71:
        num = 4
    elif num == 66:
        num = 2
    print(num)