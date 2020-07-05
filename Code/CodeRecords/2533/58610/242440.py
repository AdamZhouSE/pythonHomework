a = list(map(int, input().replace('[', '').replace(']', '').split(',')))
start, end = 0, 1
while start + end < len(a):
    if a[start] % 2 == 1:
        a[start], a[-end] = a[-end], a[start]
        end += 1
    else:
        start += 1
print(a)