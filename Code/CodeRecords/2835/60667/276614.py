import itertools
n = int(input())
a = list(input().split())
per = list(itertools.permutations(a))
temp = []
largest = -1
for i in per:
    s = ''
    if i[0] != '0':
        for j in range(n):
            s += i[j]
        temp.append(int(s))
for i in temp:
    if i % 90 == 0:
        if i > largest:
            largest = i
print(largest)