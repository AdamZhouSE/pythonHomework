# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
input_array = list(map(int, input()[1:-1].split(",")))
i = 1
while True:
    if not input_array.__contains__(i):
        print(i)
        break
    i = i + 1
