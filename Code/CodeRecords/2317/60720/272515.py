list0 = input().split(',')
list0 = [int(list0[i]) for i in range(len(list0))]
list0.sort()
count = 0
for i in range(len(list0)):
    for j in range(i + 1, len(list0)):
        count += (list0[j] - list0[i]) * pow(2, j - i - 1)
print(count % (pow(10, 9) + 7))

