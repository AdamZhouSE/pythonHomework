n = int(input())
abilities = input().split()
for i in range(0, n):
    abilities[i] = int(abilities[i])
abilities.sort()
groups = []
for i in range(0, n // 2):
    groups.append(abilities[2 * i:2 * i + 2])
count = 0
for i in groups:
    count += abs(i[0] - i[1])
print(count)