string = input()
alist = list(map(int, string.lstrip("[").rstrip("]").split(",")))
length = len(alist)
n = int(input())
alist = sorted(alist)
m = []
for i in range(length - 1):
    for j in range(i + 1, length):
        m.append(alist[j] - alist[i])
m = sorted(m)
print(m[n - 1])


