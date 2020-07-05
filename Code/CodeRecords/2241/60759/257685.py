N = int(input())
lst = []
groups = 0
for n in range(1, N + 1):
    lst.append(n)
    while sum(lst) > N:
        lst.pop(0)
    if sum(lst) == N:
        groups += 1
print(groups)
