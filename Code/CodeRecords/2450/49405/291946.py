a = [-1] + list(map(int, input().split(","))) + [-1]
t = int(input())
b = []
for i in range(len(a)):
    if a[i] == t and a[i - 1] != t: b.append(i - 1)
    if a[i] == t and a[i + 1] != t: b.append(i - 1)
print(b)