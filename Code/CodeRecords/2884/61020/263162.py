from itertools import permutations

first_line = input()
second_line = input()

n_and_d_list = first_line.split()
n = int(n_and_d_list[0])
d = int(n_and_d_list[1])

heights_list = second_line.split()

for i in range(0, len(heights_list)):
    heights_list[i] = int(heights_list[i])

    i += 1

result = 0

for unit in permutations(heights_list, 2):
    if d >= unit[0] - unit[1] >= -d:
        result += 1

print(result)
