num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    divisor_list = []
    for j in range(1, num + 1):
        if num % j == 0:
            divisor_list.append(j)
    res = 0
    for ch in divisor_list:
        res = res + ch
    if res < num * 2:
        print(1)
    else:
        print(0)