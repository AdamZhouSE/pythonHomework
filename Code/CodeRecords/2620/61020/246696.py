def sum_of(N):
    sum = 0
    for i in range(1, N + 1):
        sum += i ** 5

    return sum


num_of_cases = int(input())
case_list = []
for i in range(0, num_of_cases):
    case_list.append(int(input()))

for case_int in case_list:
    print(sum_of(case_int))
