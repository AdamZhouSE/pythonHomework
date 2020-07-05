from itertools import permutations
envelops = [list(map(int, input().split(","))) for x in range(0, int(input()))]
result = 1
all_cases = permutations(envelops)
for case in all_cases:
    temp_res = 1
    for i in range(0, len(case) - 1):
        if case[i][0] < case[i + 1][0] and case[i][1] < case[i + 1][1]:
            temp_res += 1
    result = max(result, temp_res)
print(result)