import itertools


def calculate(l):
    count = 0
    for i in range(len(l)):
        count += (l[i][0]+l[i][1])*(l[i][0]+l[i][1])

    return count


n = int(input())
s = input().split(' ')
l = []
for i in range(len(s)):
    l.append(int(s[i]))

l.sort()

storage = [[]for i in range(n//2)]

for i in range(n//2):
    storage[i].append(l[i])
    storage[i].append(l[n-1-i])

print(calculate(storage))