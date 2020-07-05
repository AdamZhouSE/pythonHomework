num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    count = 0
    while num > 0:
        j = 0
        while True:
            if int(pow(2, j)) > num:
                break
            else:
                j = j + 1
        j = j - 1
        num = num - int(pow(2, j))
        count = count + 1
        if num == 1:
            count = count + 1
            break
    print(count)