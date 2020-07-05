num_test = int(input())
num_list = []
for i in range(num_test):
    num = int(input())
    num_list.append(num)
for i in range(num_test):
    num = num_list[i]
    start = int(1 + (num - 1) * num)
    length = num * 2
    end = start + length - 1
    res = int((start + end) * length / 2)
    print(res)
