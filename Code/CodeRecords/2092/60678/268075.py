counts = []
count = 0
people_num = int(input())
tellers = input().split()
for i in range(0, people_num):
    tellers[i] = int(tellers[i])

for i in range(0, people_num):
    count = 1
    index = tellers[i] - 1
    while index != i:
        index = tellers[index] - 1
        count += 1
        if count > 100:
            break
    counts.append(count)
counts.sort()
print(counts[0])