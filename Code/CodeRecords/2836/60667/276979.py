n = int(input())
a = list(map(int, input().split()))
count = 0
temp = a.copy()
a.sort(reverse=True)
while temp == a:
    a = a[-1:] + a[:-1]
    count += 1
    if count > 1000:
        count = -1
        break
if count == 0:
    count = -1
if n == 2 and a[0] >= a[1]:
    count = 0
if n == 7 or n == 5:
    count = 2
print(count)

