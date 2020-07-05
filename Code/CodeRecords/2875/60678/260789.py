num = int(input())
a = input().split()
for i in range(0, len(a)):
    a[i] = int(a[i])

outcome = a.copy()
for i in range(0, num):
    outcome[a[i] - 1] = i + 1

for i in range(0, num):
    outcome[i] = str(outcome[i])
print(' '.join(outcome))