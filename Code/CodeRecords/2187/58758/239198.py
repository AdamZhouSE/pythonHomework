count = int(input())
num_list = []
for i in range(0, count):
    first_line = input().split()
    N = int(first_line[0])
    K = int(first_line[1])
    second_line = input().split()
    max_sum = 0
    for j in range(0, N-K+1):
        this_sum = 0
        for k in range(j, j+K):
            this_sum += int(second_line[k])
        if this_sum > max_sum:
            max_sum = this_sum
    num_list.append(max_sum)
for i in num_list:
    print(i)
