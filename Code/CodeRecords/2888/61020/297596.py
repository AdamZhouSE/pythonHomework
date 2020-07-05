line_0 = input()
n = int(line_0.split()[0])
m = int(line_0.split()[1])

line_1 = input().split()

l_and_r_s = []
for i in range(n):
    line = input()

    l_and_r_s.append((int(line.split()[0]), int(line.split()[1])))

num_of_1 = line_1.count('1')
num_of_neg1 = line_1.count('-1')

results = []
for l_r in l_and_r_s:
    num_of_contained_num = l_r[1] - l_r[0] + 1

    if (num_of_contained_num) % 2 != 0:
        results.append(0)
        break

    if (num_of_contained_num <= min(num_of_1, num_of_neg1)):
        results.append(1)
        break

    results.append(0)

for res in results:
    print(res)