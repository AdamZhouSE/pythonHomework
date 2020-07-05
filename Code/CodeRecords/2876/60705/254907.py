n = int(input())
a = list(map(int, input().split(" ")))
l = []
for i in range(1, n-1):
    if a[i-1] == a[i+1] == 1 and a[i] == 0:
        l.append(i)
count = 0
for i in range(0, len(l)):
    if not ((l[i] + 2) in l[i+1:]):
        count += 1
print(count)